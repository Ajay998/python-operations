from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from login_project import settings
from django.core.mail import send_mail
#
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
# Create your views here.


def home(request):
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist. Please try another")
            return redirect('home')
        #
        # if User.objects.filter(email=email):
        #     messages.error(request,"Email already exist. Please try another")
        #     return redirect('home')

        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")

        if pass1!=pass2:
            messages.error(request,"Password didnt match")

        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('home')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has successfully created. Please confirm the confirmation from your email")

        #################### Confirmation of message ########################
        subject = "Welcome to Company Confirmation email"
        message = "Hello "+ myuser.first_name+" !! "+"Thank you for visiting our website.\nPlease confirm your email and activate ur account"
        from_email = settings.EMAIL_HOST_USER
        print(myuser.email)
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

        mail_subject = 'Activate your user account.'
        message = render_to_string('email_confirmation.html', {
            'user': myuser.username,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': account_activation_token.make_token(myuser),
            'protocol': 'https' if request.is_secure() else 'http'
        })
        email = EmailMessage(mail_subject, message, to=to_list)
        if email.send():
            messages.success(request, f'Dear <b>{myuser}</b>, please go to you email <b>{to_list}</b> inbox and click on \
                    received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
        else:
            messages.error(request,
                           f'Problem sending confirmation email to {to_list}, check if you typed it correctly.')

        return redirect('signin')
    return render(request, "signup.html")
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        print(username)
        user = authenticate(username=username,password=pass1)
        print(user)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,'index.html',{'fname':fname})
        else:
            messages.error(request,"Wrong Credentials")
            return redirect('home')

    return render(request,"signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect('homepage')