from django.http import HttpResponse
from django.shortcuts import render
from wallofgardens.settings import EMAIL_HOST_USER
from contact.forms import contactForm
from django.core.mail import send_mail
from .models import Contact
# Create your views here.
def ContactUs(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        
        # print(form.cleaned_data)
        name = form.cleaned_data['name']
        userEmail = form.cleaned_data['userEmail']
        sub = form.cleaned_data['sub']
        message = form.cleaned_data['message']
        p=Contact(Username=name,UserEmail=userEmail,Subject=sub,Message=message)
        p.save()
        data_list = '\nName :    ' + name + '\nSubject  :   ' + \
            sub + '\nMessage   :    ' + message + '\nEmail  :    ' + userEmail
        # print(data_list)
        resend_Data = 'Hey ,' + \
            name+' Thanks for connecting 🥰 Your message means alot to me.If you have any queries,suggestions and anything ,feel free to  Contact me.You can contact me on my E-mail :- ' + \
            EMAIL_HOST_USER + ' as well as on contact number :- 9873538514\nRegards :\nVarun Kumar \n '
        # print(resend_Data)

        send_mail("Contact Details", data_list,
                  userEmail, [EMAIL_HOST_USER], fail_silently=False)
        send_mail("Thank You For Connecting.", resend_Data,
                  EMAIL_HOST_USER, [userEmail], fail_silently=False)
        print("mail sent successfully")
    
    
    return render(request, "home.html")

