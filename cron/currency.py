import requests
import json
import time

bank_url = "https://nbrb.by/API/ExRates/Rates/"

def Currency(cid):
    req = bank_url + str(cid)
    r = requests.get(req)
    time.sleep(5)
    print(req)
    rj = r.json()
    value = str(int(rj['Cur_OfficialRate']*100)/100)
    scale = str(rj['Cur_Scale'])
    return {'value': value, 'scale': scale}

def main():
    usd = Currency(145)
    usd_val = usd['value']
    usd_count = usd['scale']
    eur = Currency(292)
    eur_val = eur['value']
    eur_count = eur['scale']
    rub = Currency(298)
    rub_val = rub['value']
    rub_count = rub['scale']
    uah = Currency(290)
    uah_val = uah['value']
    uah_count = uah['scale']

    data = {
        'usd' : usd,
        'eur' : eur,
        'rub' : rub,
        'uah' : uah
    }

    with open("currency.json", "w") as write_file:
        json.dump(data, write_file)


main()