from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'index.html', {})