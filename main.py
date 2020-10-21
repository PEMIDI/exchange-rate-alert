import requests
import json
from config import RULES
from mail import smtp_mail
from config import url


def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None



def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(rates):
    subject = str(rates['timestamp'])
    print(subject)

    if RULES['prefer'] is not None:
        tmp = dict()
        for exc in RULES['prefer']:
            tmp[exc] = rates['rates'][exc]
        rates = json.dumps(tmp)
        
    print(rates)

    smtp_mail(rates=rates, subject=subject)



if __name__ == "__main__":
    rates = get_rates()

    if RULES['archive']:
        archive(rates['timestamp'], rates['rates'])

    if RULES['send_mail']:        
        send_mail(rates)
