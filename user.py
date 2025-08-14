import requests
from dotenv import load_dotenv
import os
load_dotenv()

endpoint = "https://api.sheety.co/4a4614d6c902f66b63975acc1b55ba06/flightclub/user"
head = {
    "Authorization":"Bearer 1DW6fJPnWotRlBNYv7SWeBd2xg8"
}
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email address: ")
email_again = input("Enter your email address again for validation: ")

para = {
    "user":{
        "firstname":first_name,
        "lastname":last_name,
        "email":email,
    }
}
response = requests.post(url=endpoint,headers=head,json=para)
print(response.text)