from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team


def index(request):
    obj = Place.objects.all()
    team = Team.objects.all()
    return render(request, "index.html", {'data': obj, 'data2': team})


"""def operations(request):
    n1 = int(request.GET['num1'])
    n2 = int(request.GET['num2'])
    add = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    div = n1 / n2

    return render(request, "result.html", {"sum": add, "difference": sub, "product": mul, "quotient": div})
"""
