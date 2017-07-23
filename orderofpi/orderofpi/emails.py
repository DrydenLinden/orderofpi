from django.core.mail import send_mail, BadHeaderError
#from django.http import HttpResponse, HttpResponseRedirect

#formatted html emails
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


#class that mails things for us
class Mailer():
    def send_email(subject, message, to_email):
        from_email = 'charges@uvicorderofpi.ca'    

        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, [to_email])
            except BadHeaderError:
                return False 
            return True 

        else:
            #missing parameters
            #failure from other error checking
            pass

    def send_html_email(plaintext_file, htmly_file, subject, to_name, to_email):
        # specific to instance
        plaintext = get_template(plaintext_file)
        htmly     = get_template(htmly_file)

        d = { 'receive_name': to_name }

        from_email = 'charges@uvicorderofpi.ca'
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send() 