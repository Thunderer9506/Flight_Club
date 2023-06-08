from twilio.rest import Client
import smtplib
import requests

acc_sid = "your account sid"                                        
auth_token = "your authentication token"

class NotificationManager:
    def send_msg(self,body):
        client = Client(acc_sid,auth_token)
        message = client.messages.create(
            body=body,
            from_= "number that is provided to you",
            to = "your number"
        )
        
        print(message.sid)
    def send_email(self,body,link):
        myemail = "Your email address"
        password = "your password"

        sheety_endpoint = "your sheety endpoint"
        head_sheety = {
            "Authorization":"your authorization code"
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