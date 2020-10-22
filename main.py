import requests
import json
from config import rules
from mail import smtp_mail
from config import url
from local_config import SMS_API_KEY,sms_receptor, sms_sender
from sms_api import send_sms


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

    if rules['prefer']['on'] is not None:
        tmp = dict()
        for exc in rules['prefer']['cur']:
            tmp[exc] = rates['rates'][exc]
        rates = json.dumps(tmp)
        
    print(rates)

    smtp_mail(rates=rates, subject=subject)


def sms_notifier(rates):
    prefer = rules['prefer']['cur']['AMD']

    msg = ''

    if rates['AMD'] >= prefer['max']:
        msg += f"max touched : AMD is {rates['AMD']}"
        

    if rates['AMD'] <= prefer['min']:
        msg += f"min touched : AMD is {rates['AMD']}"
        


    return msg





if __name__ == "__main__":
    rates = get_rates()

    if rules['archive']:
        archive(rates['timestamp'], rates['rates'])

    if rules['email']:        
        send_mail(rates)

    message = sms_notifier(rates['rates'])
    print(message)

    if message:
        send_sms(SMS_API_KEY,sms_sender ,sms_receptor, message)
