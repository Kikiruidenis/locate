# import package
import africastalking

def send_sms(message,receiver):
    username = "getme"
    api_key = "d1a86c35be3a3c646966e6d3595337c17fa2ff0c11884111091f3d6a960ca863"
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    response = sms.send(message, [receiver])
    
