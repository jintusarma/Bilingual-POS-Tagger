from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage, get_connection
from django.conf import settings

def send_mail_token(email, token):
    try:
        subject = "Your account needs to be verified"
        message = f'Click on the link to verify http://127.0.0.1:8000/verify/{token}/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )


    except Exception as e:
        return False
    
    return True

def send_emails(email, token):
    try:
        with get_connection(  
           host=settings.EMAIL_HOST, 
        port=settings.EMAIL_PORT,  
        username=settings.EMAIL_HOST_USER, 
        password=settings.EMAIL_HOST_PASSWORD, 
        use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = "Your account needs to be erified"  
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [email, ]  
           message = f'Click on the link to verify http://127.0.0.1:8000/verify/{token}/'  
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
    except Exception as e:
        return False
    
    return True