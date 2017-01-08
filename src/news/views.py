from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Regis

# Create your views here.
def start(request):
	title ="Subscrite to the Strijp-s newsletter"
	if request.user.is_authenticated():
		title = "Welcome back %s" %(request.user)
	form = RegModelForm(request.POST or None)

	context = {
		"title": title,
		"the_form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		name = form.cleaned_data.get("name")
		email = form.cleaned_data.get("email")
		if not instance.name:
			instance.name = "PERSON"
		instance.save()

		context = {
			"title": "thank you %s!" %(name)
		}

		if not name:
			context={
			"title": "thank you no name person!"
			}
		

		print (instance)
		print (instance.timestamp)
		#form_data = (form.cleaned_data)
		#abc = form_data.get("email")
		#abc2 = form_data.get("name")
		#obj = Regis.objects.create(email = abc, name=abc2)
		
	
	if request.user.is_authenticated() and request.user.is_staff:
		queryset = Regis.objects.all().order_by("-timestamp") 
		context = {
			"queryset": queryset,
		}



	return render(request, "start.html", context)


def contact(request):
	title = "Contact us"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#for key in form.cleaned_data:
		#	print (key,form.cleaned_data.get(key))
			#print (form.cleaned_data.get(key))
		from_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_name = form.cleaned_data.get("name")
		subject = 'Form of contact'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "otheremail@gmail.com"]
		email_message = "%s: %s sent by %s" %(form_name, form_message, from_email)

		send_mail(subject,
			email_message,
			email_from,
			email_to,
#CAMBIAR A TRUE PARA QUE NO SALGA ERROR, SOLO A FALSE PARA TESTING
			fail_silently = False)
		#print  (email, message, name)
	context = {
		"form": form,
		"title": title,
	}
	return render(request, "forms.html", context)