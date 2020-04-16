from django.shortcuts import render
from .utils import Currency, Contests
from sys import platform
import json

# Create your views here.
def index(request):
    if (platform == "win32"):
        path = "D:\\work\\python\\newtab\\cron\\currency.json"
    else:
        path = "/home/denvilk/code/newtab/cron/currency.json"

    with open(path, "r") as read_file:
        data = json.load(read_file)

    usd = data['usd']
    usd_val = usd['value']
    usd_count = usd['scale']
    
    eur = data['eur']
    eur_val = eur['value']
    eur_count = eur['scale']

    rub = data['rub']
    rub_val = rub['value']
    rub_count = rub['scale']

    uah = data['uah']
    uah_val = uah['value']
    uah_count = uah['scale']

    contests = Contests()
    contests.reverse()

    return render(request, 'main/index.html', {'usd':usd_val, 'eur':eur_val, 'rub':rub_val, 'uah':uah_val,
                                               'usdc':usd_count, 'eurc':eur_count, 'rubc':rub_count, 'uahc':uah_count,
                                               'contests':contests})