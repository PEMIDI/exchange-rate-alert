import requests
import json
from config import RULES, EMAIL_RECEIVER
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

    if RULES['prefer'] is not None:
        tmp = dict()

        for exc in RULES['prefer']:
            tmp['exc'] = rates['rates'][exc]

        rates = tmp

    smtp_mail(rates, EMAIL_RECEIVER, '22')

    

    


if __name__ == "__main__":
    res = get_rates()

    if RULES['archive']:
        archive(res['timestamp'], res['rates'])

    if RULES['send_mail']:        
        send_mail(res)
