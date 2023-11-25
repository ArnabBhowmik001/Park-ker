import cv2
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.   
def Catch_camera(request):
   
     cam = cv2.VideoCapture(1,cv2.CAP_DSHOW)
     fps = cam.get(cv2.CAP_PROP_FPS)

    # Calculate the frame number for the specified snapshot time
     frame_number = int(10 * fps)

    # Set the video capture object to the specified frame number
     cam.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
     ret, frame1 = cam.read()
     cam.release()
     cam.destoryAllWindows()

def Sign_up(request):
     if request.method == "POST":
       email = request.POST.get("email")
       username = request.POST.get("email")
       password = request.POST.get("password")
       user = Customer.objects.get(email=email)
       if user is not None:
         messages.error(request, "User already exists")
         return redirect('signup')        
       Customer = Customer.objects.create_user(username, email, password)
       Customer.save()
       
       messages.success(request, "Account created successfully")
       
       return redirect('signin')


def log_in(request):
      if request.method == "GET":
       email = request.POST.get("email")
       password = request.POST.get("password")
       
       user = authenticate(username=email, password=password)
      
       if user is not None:
         login(request, user)
         print("Login successful")
         messages.success(request, "Login successful")
         request.session['email'] = email
         request
         return render(request,"musicals/index.html",{"email":email})
       
       else:
        print("Invalid credentials")
       
        messages.error(request, "Invalid credentials")
        return redirect('signin')
          
        return render(request, "musicals/signin.html")

# def booking(request):
    #  return HttpResponse("Booking SuccessFul")

def end_journey(request):
     if request.method== "POST":
         id=request.POST.cus_id
     return HttpResponse("Ended")

def parkings(request):
     return HttpResponse("Total Parkings")

def create_park(request):
     return HttpResponse("parking Created ")

def confirm_Book(request):
     return HttpResponse("Booking Confirmed")
def payment(request):
     return HttpResponse("payemnt Done ")
def Owners_parkings(request):
     return HttpResponse("owners parkings")

def parking_create(request):
     return HttpResponse("parking created")
