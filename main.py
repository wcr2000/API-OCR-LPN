import requests

URL = "http://127.0.0.1:5000/imageurl?url=https://www.myhappyenglish.com/free-english-lesson/wp-content/uploads/2019/05/Shadowing-08-Acme-1024x576.jpg"
read = requests.get(url = URL)
data = read.json()

print(data)