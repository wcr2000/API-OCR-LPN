from flask import Flask,request, render_template
import requests
import re
import pytesseract
import cv2

app = Flask(__name__)

def strbuildClean(string):
    removeChar = ['+', '=', '|']
    clean_data = string.replace('\n',' ')
    clean_data = clean_data.replace('\f',' ')
    clean_data = re.sub(' +', ' ', clean_data)
    for i in removeChar:
        clean_data = clean_data.replace(i,'')
    return clean_data

@app.route('/')
def index():
    return "Use URL /imageurl?user=____"

@app.route("/imageurl",methods = ['POST','GET'])
def image_ocr():
    try:
        url = request.args.get('url')
        file_url = url
        file_object = requests.get(file_url)
        with open('photo/Python-Tutorial.png', 'wb') as local:
            local.write(file_object.content)  
        name = "photo/Python-Tutorial.png"
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        originalImage = cv2.imread(name)
        img = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        custom_config = r'-l tha+eng --psm 6'
        text = pytesseract.image_to_string(img, config=custom_config)
        txtDict = {
            "image-Path": name,
            "url-Path" : url,
            "result": strbuildClean(text)
        }
    except:
        print("Not found image")
        txtDict = {
            "ImageName": name,
            "result": "Cannot find you image"
        }
    return txtDict

if __name__ == "__main__":
    app.run(debug="on")