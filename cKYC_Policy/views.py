from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import PolicyForm,PolicyFieldsForm,PolicyFieldsFormset
from django.contrib.auth.decorators import login_required
from .models import Policy,PolicyField
from django import forms
from django.forms import formset_factory
from django.conf import settings
from . import generatepolicy

def index(request):
	policies_set=Policy.objects.all()
	if policies_set:
		if request.user.is_staff:
			return render(request,'admin.html',{'policies_set' : policies_set })
		return render(request,'home.html')

	return render(request,'config.html')

@login_required(login_url='/login')
def ckyc_create_policy(request):
	if request.user.is_staff:
		if request.method == 'POST':
			form = PolicyForm(request.POST)
			form.policy_field_instances = PolicyFieldsFormset(request.POST)

			if form.is_valid():
				print(form.cleaned_data['policy_name'])
				pol_name=Policy(policy_name=form.cleaned_data['policy_name'],
					policy_description=form.cleaned_data['policy_description'])
				
				pol_name.save()

				if form.policy_field_instances.cleaned_data is not None:

					for player_instance in form.policy_field_instances.cleaned_data:
						proof_ds=','.join(player_instance['proof'])
						pfield=PolicyField(
							name = player_instance['name'],
							meta = player_instance['meta'],
							datatype = player_instance['datatype'],
							pattern = player_instance['pattern'],
							message = player_instance['message'],
							proof = proof_ds,
							policy=pol_name
							)
						pfield.save()
					pol_name.save()

					return HttpResponseRedirect('/confirm-policy/'+str(pol_name.pk))

		else:
			form = PolicyForm()
		return render(request,'create-policy.html',{'form':form })

	return render(request,'home.html')

def ckyc_comfirm_policy(request,pk=None):
	instance = get_object_or_404(Policy,pk=pk)
	context ={
			'instance' : instance,
	}
	polxml=generatepolicy.getXML(pk)
	return  render (request, 'confirm-policy.html', context)

def ckyc_delete_policy(request,pk=None):
	instance =get_object_or_404(Policy,pk=pk)
	instance.delete()
	return HttpResponseRedirect('/')


def testing(request):
	pol_id=6
	val=generatepolicy.getXML(pol_id)
	return HttpResponse(val)



