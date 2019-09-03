from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
import base64,ast
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class User(AbstractUser):

	first_name = None
	last_name = None
	organization_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	# is_checker = models.BooleanField(default=False)
    # is_maker = models.BooleanField(default=False)
	def get_absolute_url(self):
		return reverse('userdetail',kwargs={"id":self.id})
	
class UserKeys(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	public_key = models.CharField(max_length=30, blank=False)
	private_key = models.CharField(max_length=30, blank=False)

	def generate_keys(self):
	    privatekey = RSA.generate(1024,Random.new().read)
	    publickey = privatekey.publickey()
	    privkey=privatekey.exportKey().decode()
	    pubkey=publickey.exportKey().decode()
	    return privkey,pubkey

	def create(self,user):
		privatekey,publickey=self.generate_keys()
		self.user = user
		self.public_key = publickey
		self.private_key = privatekey
		self.save()
	def __str__(self):
		return '---- publickey, privatekey ----' + str(self.user)
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        ukeys=UserKeys()
        ukeys.create(user=instance)

















# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def sending_mail(request):
# 	sub='ckYC registration successfull'
# 	mail
# 	send_mail('got mail from cKYC '+"\n"
#                 "email:"+str()+"\n"
#                 "subject: "+str(sub)+"\n"
#                 "message :"+ str(message),
#                 settings.EMAIL_HOST_USER,
#                 ['djangotest25@gmail.com'], 
#                 fail_silently=False )

# 	return render(request, 'mail.html', {'form': form})














































# class cKYC_policy(models.Model):
# 	policy_name = models.CharField(max_length=16,unique=True)
# 	policy = models.TextField()

# 	def __str__(self):
# 		return self.policy_name


    # email = models.EmailField(_('email address'), unique=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['organization_name',]
