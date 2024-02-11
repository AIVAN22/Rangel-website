from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import PurchaseEmail, Product

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def dashboard(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "dashboard.html", context)


def about(request):
    return render(request, "about.html")


def support(request):
    return render(request, "support.html")


def purchase(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        content = request.POST["context"]
        save = PurchaseEmail(name=name, email=email, content=content)
        save.save()
        return render(
            request, "purchase.html", {"error_message": "You send email successfully!"}
        )
    else:
        return render(request, "purchase.html", {"error_message": "Error?"})


def redirect(request):
    return dashboard(request)


def logout_view(request):
    logout(request)
    return redirect(request)


def loginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request)
        else:
            return render(request, "login.html", {"error_message": "Invalid login"})

    else:
        return render(request, "login.html")

    # context = {}
    # return render(request, "login.html")


def upload(request):
    context = {
        "categories": Product.CATEGORIES,
        "canvas": Product.CANVAS_,
        "products": Product.objects.all(),
    }

    if request.method == "POST":
        img = request.FILES["images"]
        canvas = request.POST["canvas"]
        categories = request.POST["categories"]
        content = request.POST["content"]

        title = request.POST["title"]

        save = Product(
            title=title,
            canvas=canvas,
            content=content,
            categories=categories,
            img=img,
        )
        save.save()
        context["message"] = "Uploaded Successfully"
        return render(request, "upload.html", context)

    return render(request, "upload.html", context)


def product(request, product_id):
    product_ = get_object_or_404(Product, id=product_id)
    return render(request, "product.html", {"product": product_})


def categories(request):
    categories = Product.CATEGORIES
    return render(request, "categories.html", {"categories": categories})


def oil_painting(request):
    products = Product.objects.filter(categories="Oil-Painting")
    return render(request, "category.html", {"products": products})


def Watercolors(request):
    products = Product.objects.filter(categories="Watercolors")
    return render(request, "category.html", {"products": products})


def Dry_Crayons(request):
    products = Product.objects.filter(categories="Dry-Crayons")
    return render(request, "category.html", {"products": products})


def Oil_Crayons(request):
    products = Product.objects.filter(categories="Oil-Crayons")
    return render(request, "category.html", {"products": products})


def handler404(request, exception):
    return render(request, "404.html", status=404)
