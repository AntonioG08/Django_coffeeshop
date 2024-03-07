from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
""" def contact(request):
    # print("Tipo de petición: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            'Si todo ha salido bien, podemos redireccionar al usuario'
            return redirect(reverse('Contacto') + '?ok')

    return render(request, "contact/contact.html", {'form': contact_form}) """


def contact(request):
    # print("Tipo de petición: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email2 = request.POST.get('email', '')
            content = request.POST.get('content', '')

            'Enviamos el correo y redireccionamos'
            email = EmailMessage(
                subject="La caffettiera: Nuevo mensaje de contacto",
                body=f"De {name} <{email2}>\n\nEscribió:\n\n{content}",
                from_email="no-contestar@gmail.com",
                to=["togoruiz10@gmail.com"],
                reply_to=[email2]
            )

            try:
                # Si sale bien:
                email.send()
                return redirect(reverse('Contacto') + '?ok')
            except:
                # Algo no ha ido bien
                return redirect(reverse('Contacto') + '?fail')

    return render(request, "contact/contact.html", {'form': contact_form})
