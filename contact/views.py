from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactForm
from .forms import  messageForm
from HackOkapp.sms import *

# add to your views
def contact(request):
    form_class = ContactForm
    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)
        contact = messageForm(data=request.POST)

        if form.is_valid():

            Name = request.POST.get( 'Name', '')
            Phone = request.POST.get('Phone', '')
            Email = request.POST.get( 'Email', '')
            Message = request.POST.get('Message', '')

            
            Name = form.cleaned_data['Name']
            Phone = form.cleaned_data['Phone']
            Email = form.cleaned_data['Email'] 
            Message = form.cleaned_data['Message']
            text = "Dear Admin,\nSomeone used the LocateUs contact form.\n\nHere is what was submited:\nName: %s\nPhone no.: %s\nEmail: %s\nMessage: %s\n\nYou received this message, because you are the admin." %(Name,Phone,Email,Message)
            send_sms(text,"+254704308083")
            instance = contact.save(commit=False)
            instance.save()
            
            return redirect('/contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
