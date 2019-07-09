from django.shortcuts import render,redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from core.models import Banners
from viajes.models import Paquete 

bn = Banners.objects.get(id=1)
# Create your views here.
def contact(request):
	contact_form = ContactForm()


	if request.method == 'POST':

		paqueteid = request.POST.get('pedirinfo')

		if paqueteid:
			status = Paquete.objects.get(pk=paqueteid)
			return render(request,'contact/contact.html',{'form':contact_form,'banners':bn,'destino':status})

		contact_form = ContactForm(data=request.POST)
		if contact_form.is_valid():
			name = request.POST.get('name','')
			email = request.POST.get('email','')
			content = request.POST.get('content','')
			destino = request.POST.get('destino')

			#Eviamos email
			email2 = EmailMessage(

				"Urrea Tours: Nuevo mensaje de contacto",
				"De {} <{}>\n\nEscribio:\n\n{}\n\nMandar informe sobre el destino: {}\n\n".format(name,email,content,destino),
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

