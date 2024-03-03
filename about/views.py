from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages


def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests.

    Displays an individual instance of the `About` model.

    **Context**

    * `about`: The most recent instance of the `About` model.
    * `collaborate_form`: An instance of the `CollaborateForm` form.

    **Template**

    `about/about.html`
    """

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I aim to reply in 48 hours.")

    return render(
        request, "about/about.html",
        context={"about": about, "collaborate_form": collaborate_form})
