import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

### Function to send the email ###
def send_an_email():   
    toaddr = 'youremail@gmail.com' 
    me = 'yourname' 
    subject = "Home Security Notification "
    #wifi_message_file = 
    text = open("importProbemon/wifi_data_for_email.txt","r")  #importProbemon/wifi_data_for_email.txt

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = toaddr
    msg.preamble = "test " 
    msg.attach(MIMEText(text.read()))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("FSWebcampictures/latestPicture.jpg", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="FSWebcampictures/latestPicture.jpg"')
    msg.attach(part)

    try:
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.ehlo()
       s.starttls()
       s.ehlo()
       s.login(user = 'youremail@gmail.com', password = 'yourpassword')
       #s.send_message(msg)
       s.sendmail(me, toaddr, msg.as_string())
       s.quit()
    #except:
    #   print ("Error: unable to send email")
    except SMTPException as error:
          print ("Error")

send_an_email()
