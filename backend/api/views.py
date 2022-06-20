import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers  import ProductSerializers

# Create your views here.

@api_view(["GET",'POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW"""
    instance= Product.objects.all().order_by("?").first()
    data={}
    if instance:
        data=ProductSerializers(instance).data
    #when you take a model instance and turn it into a python dictionary then return a JSON to the client it called serialization
    return Response(data)

@api_view(["POST"])
def api_home1(request):
    body= request.GET
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
       instance= serializer.save()
       print(instance)
       print(body)
    return Response(serializer.data)
