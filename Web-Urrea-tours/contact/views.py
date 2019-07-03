from django.shortcuts import render,redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from core.models import Banners 

bn = Banners.objects.get(id=1)

# Create your views here.
def contact(request):
	contact_form = ContactForm()

	if request.method == 'POST':
		contact_form = ContactForm(data=request.POST)
		if contact_form.is_valid():
			name = request.POST.get('name','')
			email = request.POST.get('email','')
			content = request.POST.get('content','')

			#Eviamos email
			email2 = EmailMessage(

				"Urrea Tours: Nuevo mensaje de contacto",
				"De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
				"pruebaurreatours@gmail.com",
				["dany_magadan@hotmail.com"],
				reply_to=[email]
			)

			try:
				email2.send()
				return redirect(reverse('core-contact')+"?ok")
			except:
				return redirect(reverse('core-contact')+"?fail")

		

	return render(request,'contact/contact.html',{'form':contact_form,'banners':bn})

