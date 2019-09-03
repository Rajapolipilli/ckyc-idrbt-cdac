# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import UserRegisterForm,NewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework.authtoken.models import Token
from cKYC_Policy.models import Policy
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.core.mail import EmailMessage


def PolicyView(request):
	policies=Policy.objects.all()
	return render (request,'view-policy.html',{'policies' : policies })

def user_signup(request):
	policies=Policy.objects.all()
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			u = form.save(commit=False)
			u.save()
			username=form.cleaned_data['username']
			return render(request,'registration/signup-success.html',{'user':username})

	else:
		form = UserRegisterForm()
	return render(request,'registration/register.html',{'form':form , 'policies':policies })

def register(request):
	policies=Policy.objects.all()
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.set_unusable_password()
			user.save()

			# Send an email to the user with the token:
			mail_subject = 'Activate your account.'
			current_site = get_current_site(request)
			uid = urlsafe_base64_encode(force_bytes(user.pk))
			token = account_activation_token.make_token(user)
			activation_link = "{0}/?uid={1}&token{2}".format(current_site, uid, token)
			message = "Hello {0},\n {1}".format(user.username, activation_link)
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(mail_subject, message, to=[to_email])
			email.send()
			return HttpResponse('Please confirm your email address to complete the registration')

	else:
		form = UserRegisterForm()
	return render(request,'registration/register.html',{'form':form , 'policies':policies })

from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.views import View

User = get_user_model()

class Activate(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            # activate user and login:
            user.is_active = True
            user.save()
            login(request, user)

            form = PasswordChangeForm(request.user)
            return render(request, 'activation.html', {'form': form})

        else:
            return HttpResponse('Activation link is invalid!')

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # Important, to update the session with the new password
            return HttpResponse('Password changed successfully')

# class Signup(View):
#     def get(self, request):
#         form = SignupForm()
#         return render(request, 'signup.html', {'form': form})

#     def post(self, request):
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             # Create an inactive user with no password:
#             user = form.save(commit=False)
#             user.is_active = False
#             user.set_unusable_password()
#             user.save()

#             # Send an email to the user with the token:
#             mail_subject = 'Activate your account.'
#             current_site = get_current_site(request)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             token = account_activation_token.make_token(user)
#             activation_link = "{0}/?uid={1}&token{2}".format(current_site, uid, token)
#             message = "Hello {0},\n {1}".format(user.username, activation_link)
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(mail_subject, message, to=[to_email])
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')


@login_required
def user_detail(request,username=None):
	instance = get_object_or_404(User,username=username)
	context ={
			'instance' : instance,

	}
	return  render (request,"registration/profile.html" , context)



@login_required
def user_update(request,username=None):
	
	username1=request.user.username
	if username !=username1:
		return HttpResponseRedirect('/myprofile/'+str(username1)+'/edit')

	instance = get_object_or_404(User,username=username)
	form = NewForm(request.POST or None,request.FILES or None ,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context ={
			  'instance' : instance,
			  'form':form ,
	}
	return  render (request,"registration/edit.html" , context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

def user_settings(request):
	return render(request,'registration/settings.html')








