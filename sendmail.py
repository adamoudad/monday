# If using gmail, enable 2-step verification beforehand
# https://support.google.com/accounts/answer/185839

import smtplib
from getpass import getpass

def login(server):
  password = getpass("Sender email password:")
  server.login(sender, password)

def send_email(body, subject, sender, receiver, host, port):
  server = smtplib.SMTP(host, port)
  server.ehlo()
  server.starttls()
  server.ehlo()

  while True:
    try:
      login(server)
    except smtplib.SMTPAuthenticationError as e:
      print("Authentication error. Are your credentials right?")
      continue
    break

  while True:
    try:
      message = f"Subject: {subject}\n\n{body}"
      server.sendmail(
        sender,
        receiver,
        message
      )
    except smtplib.SMTP as e:
      print("Connection refused. In Gmail, you might need to authorize access to \"less secure apps\" (https://support.google.com/accounts/answer/6010255)")
      continue
    break

if __name__ == "__main__":
  sender = input("Sender email: ")
  receiver = input("Receiver email: ")
  subject = input('Subject: ') or "Hello !"
  body = input("Body: ") or "Sample text."
  host = input("Host (default is Gmail): ") or "smtp.gmail.com"
  port = input("Port: ") if host != "smtp.gmail.com" else 587

  send_email(body, subject, sender, receiver, host, port)
  print("Email has been sent !")
