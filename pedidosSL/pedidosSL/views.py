from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse("OLA MUNDAO! O PAULAO ESTA NO DJANGO")





