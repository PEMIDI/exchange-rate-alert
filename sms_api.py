from kavenegar import *



def send_sms(sms_api_key,sms_sender,receptor, message):
    api = KavenegarAPI(sms_api_key)
    params = { 'sender':sms_sender, 'receptor':receptor, 'message':message}
    response = api.sms_send(params) 