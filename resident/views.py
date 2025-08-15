from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
from rest_framework.response import Response


@api_view()
def create_resident(request):
    return Response("create resident")