from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from website.forms import DocumentForm
from .models import Create


# Create your views here.

class DocumentListView(ListView):
    model = Create
    template_name = 'view.html'
    context_object_name = "documents"


class HomeView(ListView):
    model = Create
    template_name = 'home.html'
    context_object_name = "documents"


def delete(request, document_id):
    document = get_object_or_404(Create, pk=document_id)
    document.delete()
    return redirect('view')


def pdf_view(request, document_id):
    document = get_object_or_404(Create, pk=document_id)
    response = HttpResponse(document.File.read(),
                            content_type='application/pdf')
    response['Content-Disposition'] = f'inline ; filename ="{document.File.name}"'
    return response


def download(request, document_id):
    document = get_object_or_404(Create, pk=document_id)
    response = HttpResponse(document.File, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment ; filename ="{document.File.name}"'
    return response


def create(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view')

    else:
        form = DocumentForm()
        return render(request, "create.html", {'form': form})


def changer(request):

    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        verified = (username == "John" and pass1 == "Smith")

        if verified:
            return redirect("view")
        else:
            messages.error(request, "Bad Credential! Sign Up or contact Admin")
            return redirect("changer")

    return render(request, "admin.html")


def signin(request):

    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            messages.error(request, "Bad Credential! Sign Up or contact Admin")
            return redirect("signup")

    return render(request, "signin.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(username, email, pass1)

        myuser.save()

        messages.success(request, "Congrats ! You are one of the users .")

        return redirect("signin")

    return render(request, "signup.html")
