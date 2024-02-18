from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
import requests


def index(request):
    form = CheckVinForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        vin = form.cleaned_data.get('vin')
        context['vin'] = vin

        url = f"http://parser-api.com/parser/gibdd_api/?key=149339b96d45b7c8cef65c0503b7ccbe&vin=JN1FANF15U0109775&vin={vin}&types=history,dtp,wanted,restrict"
        response = requests.get(url)
        print(response.status_code)  # Выводит код состояния HTTP, например, 200
        vin_info = response.json()
        context['vin_info'] = vin_info

    return render(request, "vincheck/index.html", context)