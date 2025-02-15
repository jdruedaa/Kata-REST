from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Image, Portfolio, Portfolio_Image
import json
from django.contrib.auth import authenticate, login


# Create your views here.
@csrf_exempt
def index(request):
    images_list = Image.objects.all()
    return HttpResponse(serializers.serialize("json", images_list))


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))


@csrf_exempt
def list_portfolios(request):
    portfolios_list = Portfolio.objects.all()
    for i in portfolios_list:
        publicimgs = Image.objects.filter(portfolio_image__portfolio_id=i.id, portfolio_image__privacidad=1)
        i.imagenesPublicas.set(publicimgs)
    return HttpResponse(serializers.serialize("json", portfolios_list))

@csrf_exempt
def log_user_view(request):
    
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        password = json_user['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
    return HttpResponse(serializers.serialize("json", [user]))
    
    