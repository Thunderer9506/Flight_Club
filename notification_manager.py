from twilio.rest import Client
import smtplib
import requests
from dotenv import load_dotenv
import os
load_dotenv()

acc_sid = os.getenv("TWILIO_ACC_SID")                                    
auth_token = os.getenv("TWILIO_ACC_TOKEN")

class NotificationManager:
    def send_msg(self,body):
        client = Client(acc_sid,auth_token)
        message = client.messages.create(
            body=body,
            from_=os.getenv("TWILIO_PHONE_FROM"),
            to =os.getenv("TWILIO_PHONE_TO")
        )
        
        print(message.body)
    def send_email(self,body,link):
        myemail =os.getenv("MY_EMAIL")
        password =os.getenv("MY_EMAIL_PASSWORD")

        sheety_endpoint = os.getenv("SHEETY_ENDPOINT")+"/user"
        head_sheety = {
            "Authorization":os.getenv("SHEETY_AUTHORIZATION")
        }
        response = requests.get(url=sheety_endpoint,headers=head_sheety)
        data = response.json()
        
        for i in data['user']:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=myemail,password=password)
                    connection.sendmail(
                        from_addr=myemail,to_addrs=i['email'],
                        msg=("Subject:Flight Alert!\n\n"+body+f"\n{link}")
                        )
                    print('MSG SENT')