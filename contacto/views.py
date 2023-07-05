from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.


def Contact(request):
    contact_form = ContactForm()

    if request.method=="POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            nombres=request.POST.get("nombres")
            correo=request.POST.get("correo")
            celular=request.POST.get("celular")
            ruc=request.POST.get("ruc")
            direccion= request.POST.get("direccion")
            mensaje=request.POST.get("mensaje")
            aceptar_condiciones= request.POST.get("aceptar_condiciones")


            email=EmailMessage("Mensaje desde App Django",
            "Usuario interesado en comprar productos para la venta, comunicándose mediante la web, con los siguientes datos:\n Nombre: {}\n Dirección gmail: {}\n celular: {}\n Ruc: {}\n Dirección: {}\n Mensaje: {}\n".format(nombres,correo,celular,ruc,direccion,mensaje),
            "",["gjeremy0229@gmail.com"])

            try:
                email.send()
                
                return redirect("/contacto/?valido")
        
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contact/contact.html", {'form':contact_form})
