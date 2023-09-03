# gophish-mail-alert
```
 (
  \  _,--._,-.__,         )
  / (,  ,       ,`-._    /
 (  ,^--^-. ;--^--/ (    \
  :'      `/       \ )   /
  (  o    (   o    |(  \'
   \  ,----\       /(,-.)
  ,'`-\___  `.___,'  ,. )
,'                   __/
`-.______________   |,---,
      `-^;-^--^-'\  |   '----,
        ( '------'  .',-.___/
         ;._____,--' / \
gofish  (           /   \
        (`-        /     \
         \       ,'       \
        / )  _,-'          \
       / (,-'       \       \
```
## Monitoreo de Campañas GoPhish
Este script está diseñado para monitorear campañas de GoPhish, una herramienta popular para realizar pruebas de educación y sensibilización sobre phishing. Cuando detecta que alguien ha enviado datos (como resultado de caer en un intento de phishing), envía un correo electrónico con esos detalles.

## Requisitos
Bibliotecas Python:
- gophish
- urllib3
- smtplib
- email
- datetime
Un servidor SMTP en localhost para enviar correos.
Clave de API de GoPhish.

## Uso
- Configura las direcciones de correo electrónico me (remitente) y you (destinatario).
- Ingresa tu clave de API de GoPhish en la variable api_key.
- Define el ID de la campaña de GoPhish que deseas monitorear en campaign_id.
- me = "EMAIL SENDER"
- you = "EMAIL QUE RECIBE"
- api_key = 'API KEY DE GOPHISH'
- campaign_id = 59
- Ejecuta el script. Esto monitoreará continuamente la campaña especificada y enviará correos electrónicos cuando detecte datos enviados.
## Funciones
send_email(me, you, data): Envía un correo electrónico con los datos recopilados de la campaña GoPhish.
## Advertencia
La ingeniería social y el phishing pueden ser ilegales o no éticos en muchos contextos. Utiliza este script solo en entornos controlados y con el consentimiento completo de todas las partes involucradas.


## 
## ------------------------------------------------------------------------------------------------------------
## 
## English


## GoPhish Campaign Monitoring
This script is designed to monitor GoPhish campaigns, a popular tool for conducting phishing education and awareness testing. When it detects that someone has submitted data (as a result of falling for a phishing attempt), it sends an email with those details.

## Requirements
Python Libraries:

gophish
urllib3
smtplib
email
datetime
A SMTP server on localhost to send emails.
GoPhish API Key.
## Usage
Configure the email addresses me (sender) and you (recipient).
Enter your GoPhish API key in the api_key variable.
Define the GoPhish campaign ID you wish to monitor in campaign_id.
me = "EMAIL SENDER"
you = "EMAIL RECIPIENT"
api_key = 'GOPHISH API KEY'
campaign_id = 59
Run the script. This will continuously monitor the specified campaign and send emails when it detects submitted data.
## Functions
send_email(me, you, data): Sends an email with the data collected from the GoPhish campaign.

## Warning
Social engineering and phishing can be illegal or unethical in many contexts. Use this script only in controlled environments and with the full consent of all parties involved.
