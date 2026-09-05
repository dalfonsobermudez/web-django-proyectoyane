import logging
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from proyectoyanecontact.forms import ContactForm

logger = logging.getLogger(__name__)


# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data["name"]
            from_email = contact_form.cleaned_data["email"]
            content = contact_form.cleaned_data["content"]

            if not settings.DEFAULT_FROM_EMAIL or not settings.CONTACT_EMAIL:
                logger.error("Falta configurar el correo del formulario de contacto.")
                return redirect("/contact/?invalid")

            email = EmailMessage(
                "Mensaje de app Django",
                f"Mensaje de {name}:\n\n{content}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                reply_to=[from_email],
            )

            try:
                email.send()
                return redirect("/contact/?valid")
            except SMTPException:
                logger.exception("No se pudo enviar el mensaje de contacto.")
                return redirect("/contact/?invalid")

    return render(
        request,
        "proyectoyanecontact/contact.html",
        {"contact_form": contact_form},
    )
