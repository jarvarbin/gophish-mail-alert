# gophish-mail-alert


![DALL·E 2023-08-25 10 38 25 - un gato hacker, como Mr Robot, diparando señales wifi a traves de un ordenador,  realistico, en 3d y futurista](https://github.com/jarvarbin/gophish-mail-alert/assets/93614373/db0371f2-1ea0-4baf-9b54-3f12ecc11695)


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
