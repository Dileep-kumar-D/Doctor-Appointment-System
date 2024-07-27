from django.shortcuts import render, redirect
from django.contrib import messages
from .models import registration, patients
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.deprecation import MiddlewareMixin

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ureg(request):
    Doctors_lst = registration.objects.all()
    context = {
        'Doctors_lst': Doctors_lst
    }
    if request.method == 'POST':
        pname = request.POST.get('name')
        page = request.POST.get('age')
        pemail = request.POST.get('email')
        paddress = request.POST.get('address')
        ppin = request.POST.get('pin')
        pgender = request.POST.get('gender')
        pdob = request.POST.get('dob')
        pdoctor_id = request.POST.get('doctor')

        if not pname or not page or not pemail or not paddress or not ppin or not pgender or not pdob or not pdoctor_id:
            messages.error(request, 'All fields are required.')
        else:
            pdoctor = registration.objects.get(id=pdoctor_id)
            pat_obj = patients(
                name=pname,
                age=page,
                email=pemail,
                address=paddress,
                pin=ppin,
                gender=pgender,
                dob=pdob,
                doctor=pdoctor
            )
            pat_obj.save()
            print(pname, page, pemail, paddress, ppin, pgender, pdob, pdoctor_id, pdoctor)
            context['success'] = True  # Set success flag

    return render(request, 'ureg.html', context)

@login_required(login_url='login')
def dhome(request):
    return render(request, 'dhome.html')

def login(request):
    if request.method == "POST":
        lmail = request.POST.get('email')
        pas = request.POST.get('password')

        try:
            user = registration.objects.get(email=lmail, password=pas)
            request.session['user_id'] = user.id  # Save user ID in session
            pat = patients.objects.filter(doctor=user.id)
            return render(request, 'dhome.html', {'user': user, 'patients': pat})
        except registration.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        uage = request.POST.get('age')
        udep = request.POST.get('dep')
        upas = request.POST.get('pass')

        # Check if any field is empty
        if not uname or not uemail or not uage or not udep or not upas:
            messages.error(request, 'All fields are required.')
        else:
            reg_obj = registration(name=uname, email=uemail, age=uage, dep=udep, password=upas)
            reg_obj.save()
            messages.success(request, 'Registration successful!')
            return redirect('register')

    return render(request, 'register.html')

def Logout(request):
    logout(request)
    request.session.flush()  # Clear the session data
    return redirect('login')

# Middleware to enforce login
class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated and request.path != '/login/':
            return redirect('login')
