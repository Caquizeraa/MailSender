import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

your_email = #EMAIL AQUI ENTRE ASPAS ""
your_password = #SENHA AQUI ENTRE ASPAS ""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(your_email,your_password)

email_list = pd.read_excel('Enderecos.xlsx')

names = email_list['Nome']
emails = email_list['Email']
dividas = email_list['Divida']

for i in range(len(emails)):
    name = names[i]
    email = emails[i]
    divida = dividas[i]

    msg = MIMEMultipart()
    msg['Subject'] = f'Você deve ' + str(divida) + ' reais!'
    msg['From'] = your_email
    msg['To'] = email
    body = f'Olá ' + name +'!<br>Você deve aproximadamente '+str(divida)+ ' reais!<br> Nos chame caso queira abater esta dívida!<br><br>Gratos!'
    msg.attach(MIMEText(body, 'html'))

    # sending the email
    server.sendmail(your_email, email, str(msg))

server.quit()