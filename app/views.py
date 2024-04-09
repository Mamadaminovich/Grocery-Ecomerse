from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import *
from django.core.mail import EmailMessage
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import *

@api_view(['GET'])
def home(context):
    return render(context, "index.html", {})

@api_view(['GET'])
def about(context):
    return render(context, "about.html", {})

@api_view(['GET'])
def not_found(context):
    return render(context, "404.html", {})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def cart(request):
    if request.user.is_authenticated:
        return render(request, 'cart.html')
    else:
        return redirect('login')

@api_view(['GET'])
def checkout(context):
    return render(context, "checkout.html", {})

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html', {}) 
  
@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        form = ProductUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = ProductUserCreationForm()
    return render(request, 'register.html', {'form': form})

@api_view(['GET', 'POST'])
def contact(request):
    if request.method == 'GET':
        return render(request, "contact.html", {})
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            email = EmailMessage(
                subject=subject,
                body=f"Name: {name}\nEmail: {mail}\nPhone: {phone}\nMessage: {message}",
                from_email=mail,
                to=['mamadaminov001@gmail.com'],
            )

            email.send()
            
            return render(request, "contact.html", {'message': 'Message sent successfully'})
        except Exception as e:
            return HttpResponse("Message not sent: " + str(e))

    return render(request, "contact.html", {})

@api_view(['GET'])
def home_2(context):
    return render(context, "index_2.html", {})

@api_view(['GET'])
def news(context):
    return render(context, "news.html", {})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def shop(request):
    if request.user.is_authenticated:
        products = Product.objects.all()  # Retrieve all products
        context = {'products': products}  # Pass products to the template context
        return render(request, 'shop.html', context)
    else:
        return redirect('login')

@api_view(['GET'])
def single_news(context):
    return render(context, "single-news.html", {})

@api_view(['GET'])
def single_product(context):
    return render(context, "single-product.html", {})

@api_view(['GET', 'POST'])   
def logout(request):
    auth_logout(request)
    return redirect('home') 