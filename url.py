import requests#is a libary in python but i need to know what is in it  This helps send requests to the http of the website and make it simple and human friendly
from bs4 import BeautifulSoup
import smtplib#what is this libary  sends emails to any computer with the smtp function
from http import server
import time#what function does this libary do  this is used so the email refreshes after every hlur and can be used in various ways like counting strings
URL = 'https://www.amazon.co.uk/dp/B0875K11W6/ref=uk_a_phonex_2'#assigning website to variable so you dont need to typle the whole website name out

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'} # what is point of user agent and the header 

def check_price():

    page = requests.get(URL, headers=headers) #what is the point of headers=header+request.get gets the info from website

    soup = BeautifulSoup(page.content, 'html.parser')#content is things on the page but what is parser

    title = soup.find(id="productTitle").get_text() # why assign to id and txt.get
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[1:5])# what does the 1:5mean how long the price is 
    

    if(converted_price < 400): 
       send_mail() 

    print(converted_price)
    print(title.strip())#point of strip this moves all the uneccasary white spaces from the code
    
    if(converted_price > 400):
        send_mail()


def send_mail():
    server  = smtplib.SMTP('smtp.gmail.com',587)#what is 587  this is a protical for mail transmission
    server.ehlo()#ehlo? identifies smtp server
    server.starttls()#? it is one way to create an insecure connection and then updating the transport layer security
    server.ehlo()

    server.login('milz27052004@gmail.com','hprthjumcydnjvwf')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.co.uk/dp/B0875K11W6/ref=uk_a_phonex_2' 
    
    msg = f"Subject: {subject}\n\n{body} "# what does this mean this is the product and how the page is set out
    # what is that f for?      

    server.sendmail(
        'milz27052004@gmail.com',
         'milanlol27@gmail.com',
         msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(60 * 60)#what is the point of time .sleep so you can refersh the price and it will send you an email


