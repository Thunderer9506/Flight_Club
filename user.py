import requests

endpoint = "your shetty endpoint"
head = {
    "Authorization":"your authorization code"
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