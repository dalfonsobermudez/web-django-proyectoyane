from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from proyectoyanecontact.forms import ContactForm


# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name")
            from_email = request.POST.get("email")
            content = request.POST.get("content")

            email = EmailMessage(
                "Mensaje de app Django",
                f"Mensaje de {name}:\n\n{content}",
                from_email,
                ["diorkidd10@gmail.com"],
                reply_to=[from_email],
            )

            try:
                email.send()
                return redirect("/contact/?valid")
            except Exception as e:  # noqa: E722
                print(e)
                return redirect("/contact/?invalid")

    return render(
        request,
        "proyectoyanecontact/contact.html",
        {"contact_form": contact_form},
    )
