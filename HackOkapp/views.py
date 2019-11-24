from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from .sms import *
from .models import Lost,Found
from .forms import FoundForm,LostForm
import sys
import argparse
import cv2
import numpy as np
import os
import face_recognition
import glob
from PIL import Image
from matplotlib import cm
from matplotlib import pyplot as plt
import imutils
import re

def PoliceView(request):
    if request.method == "POST":
        form = LostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(request.FILES['child_pic'])
            print(Lost.objects.last().name)
            image1 = face_recognition.load_image_file('media/'+str(Lost.objects.last().child_pic))
            list_of_face_encodings1 = face_recognition.face_encodings(image1)[0]
            images = Lost.objects.all()
            for img in glob.glob("media/data/*"):
                print(img)
               
                image2 = face_recognition.load_image_file(img.replace("\\","/"))
                list_of_face_encodings2 = face_recognition.face_encodings(image2)[0]
                results = face_recognition.compare_faces([list_of_face_encodings1], list_of_face_encodings2)
                print(results[0])
                if results[0] == True:
                    print(img.replace("\\","/"))
                   
                    image = Lost.objects.last()
                    Lost.objects.filter(child_pic=str(Lost.objects.last().child_pic)).update(found=True)
                    print(Lost.objects.filter(child_pic=str(img.replace("\\","/"))))
                    
                    child_name = image.name
                    child_contact = image.contact
                    child_image = image.child_pic
                    
                    text = "Dear Customer, "+ child_name +" posted on LocateUs has been found"
                    response = send_sms(text,"+254704308083")
                 
                    location = Found.objects.last().location
                    return render(request, 'result.html',{'text':'Person Found','found':'Person Found','location':location,'image':child_image,'name':child_name,'contact':child_contact})
            return render(request, 'result.html',{'text':'Person Not Found','found':'Person Found'})
        else:
            print("Form not valid")
    else:
        form = LostForm()
    return render(request, 'missing.html', {'form': form})

def facechop(img,location,currentFrame):  
    facedata = "media/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(facedata)

    faces = cascade.detectMultiScale(img)

    for f in faces:
        x, y, w, h = [ v for v in f ]
        sub_face = img[y:y+h, x:x+w]
        file_name = "data/frame" + "_" + location + "_" + str(currentFrame) + ".jpg"
        cv2.imwrite("media/"+file_name, sub_face)
        return file_name

def HelperView(request):
    if request.method == "POST":
        print(request.FILES['videofile'])
        form = FoundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cap = cv2.imread('media/'+str(Found.objects.last().videofile),1)

            try:
                if not os.path.exists('media/data'):
                    os.makedirs('media/data')
            except OSError:
                print ('Error: Creating directory of data')
                
            for i in range(1):
                x = facechop(cap,request.POST['location'],i)
                print ('Creating...' + str(i))
                print(x)
            cv2.destroyAllWindows()
            Found.objects.filter(videofile=str(Found.objects.last().videofile)).update(videofile=str(x))
            return redirect('home')
        else:
            print("Form not valid")
    else:
        form = FoundForm()
    return render(request, 'found.html', {'form': form})

def ResultView(request):
    return render(request,"result.html")

def listView(request):
    current_user = request.user
    missings =Lost.objects.all()
    return render(request,'child-list.html',{'missings': missings,'current_user':current_user})

def detailView(request, year, month, day, lost ):
    missing = get_object_or_404(Lost, name=lost, published__year=year, published__month=month, published__day=day)
    return render(request, 'child-detail.html', {'missing': missing})

def editView(request, year, month, day, lost ,id=None):
    if request.method == "POST":
        form = LostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            missing = get_object_or_404(Lost, name=lost, published__year=year, published__month=month, published__day=day)
        else:
            print("form not valid")
        return redirect('/child')
    else:
        form = LostForm()
        
    return render(request,'child-detail.html',{'missing',missing})

def deleteView(request, year, month, day, lost ,id=None):
    missing = get_object_or_404(Lost, name=lost, published__year=year, published__month=month, published__day=day)
    missing.delete()
    return redirect('/child')
