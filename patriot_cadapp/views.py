

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.shortcuts import render, redirect, render
from django.contrib import messages
from .models import User
from .models import Vehicle
from django.http import JsonResponse
from django.db.models import Q
from time import gmtime, strftime
from .models import Fire
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, "home.html")

def dashboard(request):

    if 'loggedUser' not in request.session:
            messages.error(request, "Log in to view page please.")
            return redirect("/login")
    loggedUser = User.objects.get(id=request.session['loggedUser'])

    context={
        'loggedUser':loggedUser,
        'officers':User.objects.all(),
        'dispatch' :Call.objects.all(),
        'fire' : Fire.objects.all()
    }
    return render(request, "dashboard.html",context, )

def desktop(request):
    return render(request, "desktop.html")

def register(request):
    return render(request, "register.html")

def citation(request, perpId):
    
    
    

    context = {
        "allperps":Suspect.objects.get(id=perpId),
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render (request, "citation.html", context)

def registeraction(request):
        
    resultFromValidator = User.objects.registerValidator(request.POST)
    
    #if there are any error messages, the length of resultFromValidator will be greater than 0
    if len(resultFromValidator) > 0:
        #for each error message, we are sending the message to messages framework that allows us to send messages to the HTML for one refresh
        for key, value in resultFromValidator.items():

            messages.error(request, value)

        return redirect("/register")

    newUser = User.objects.create(badge= request.POST['badge'], last_name= request.POST['last_name'], email=request.POST['email'],password= request.POST['password'])
    
    print(newUser)
    print(newUser.id)
    request.session['loggedUser'] = newUser.id

    return redirect("/dashboard")

def viewlog(request, callId):
    context={
        'oneCall': Call.objects.get(id=callId)
    }
    return render(request, "callInfo.html", context)

def loginaction(request):
    
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        #for each error message, we are sending the message to messages framework that allows us to send messages to the HTML for one refresh
        for key, value in errors.items():

            messages.error(request, value)
        return redirect("/login")

    userMatch = User.objects.filter(badge=request.POST['badge'])
    request.session['loggedUser'] = userMatch[0].id
    return redirect("/dashboard")

def logout(request):
        request.session.clear()
        return redirect("/")

def addcall(request):
    context={
        'officers':User.objects.all(),
        'dispatch' :Call.objects.all(),
        'fire' : Fire.objects.all()
    }
    return render(request, "addcall.html", context)

def addcallfire(request):
    context={
        'officers':User.objects.all(),
        'dispatch' :Call.objects.all(),
        'fire' : Fire.objects.all()
    }
    return render(request, "firestartcall.html", context)

def submitcall(request):  
    newCall = Call.objects.create(location = request.POST['location'], description = request.POST['description'] ,  code = request.POST['code'])
    return redirect("/dispatchdashboard")

def submitcallfire(request):  
    newCall = Call.objects.create(location = request.POST['location'], description = request.POST['description'] ,  code = request.POST['code'])
    return redirect("/firedashboard")

def clearcallfire(request, callId):
    c = Call.objects.get(id=callId)
    c.delete()
    return redirect("/firedashboard")

def clearcall(request, callId):
    c = Call.objects.get(id=callId)
    c.delete()
    return redirect("/dispatchdashboard")

def vcheck(request):
    if 'term' in request.GET:
        qs = Vehicle.objects.filter(plate__istartswith=request.GET.get('term'))
        plates = list()
        for vehicle in qs:
            plates.append(vehicle.plate)
        return JsonResponse(plates, safe=False)
    if request.method=='POST':
        plate = request.POST["plate"]

        if plate:
            match = Vehicle.objects.filter(Q(plate__icontains=plate))

            if match:
                return render(request,"platecheck.html",{"sr":match})

            else:
                messages.error(request,"No registration found. Please reference Citation System for citation information")
        else:
            return HttpResponsRedirect('/vcheck')
            
    return render( request, "platecheck.html")

def status(request, officerId):
    context= {
        "showStatus": User.objects.get(id=officerId)
    }
    return render(request,"editStatus.html", context)

def changestatus(request, officerId):
    c = User.objects.get(id=officerId)
    c.status = request.POST["status"]
    c.save()
    return redirect ("/dashboard")

def criminalcitation(request):
    return render(request,"criminalcitation.html")

def dispatchlogin(request):
    return render (request, "dispatchlogin.html")

def logindispatch(request):
    
    errors = Dispatcher.objects.dispatchValidator(request.POST)
    if len(errors) > 0:
        #for each error message, we are sending the message to messages framework that allows us to send messages to the HTML for one refresh
        for key, value in errors.items():

            messages.error(request, value)
        return redirect("/dispatchlogin")

    userMatch = Dispatcher.objects.filter(user_name=request.POST['username'])
    request.session['loggedUser'] = userMatch[0].id
    return redirect("/dispatchdashboard")

def dispatchdashboard(request):
    if 'loggedUser' not in request.session:
            messages.error(request, "Log in to view page please.")
            return redirect("/login")
    loggedUser = Dispatcher.objects.get(id=request.session['loggedUser'])

    context={
        'loggedUser':loggedUser,
        'officers':User.objects.all(),
        'dispatch' :Call.objects.all(),
        'fire' : Fire.objects.all()
    }
    return render(request, "dispatchdashboard.html",context)

def firedashboard(request):
    context={
        'dispatch':Call.objects.all(),
        'fire': Fire.objects.all()
    }
    return render(request, "firedashboard.html", context)

def dashboardvcheck(request):
    if 'term' in request.GET:
        qs = Vehicle.objects.filter(plate__istartswith=request.GET.get('term'))
        plates = list()
        for vehicle in qs:
            plates.append(vehicle.plate)
        return JsonResponse(plates, safe=False)
    if request.method=='POST':
        plate = request.POST["plate"]

        if plate:
            match = Vehicle.objects.filter(Q(plate__icontains=plate))

            if match:
                return render(request,"dashboardvcheck.html",{"sr":match})

            else:
                messages.error(request,"No registration found. Please reference Citation System for citation information")
        else:
            return HttpResponsRedirect('/dashboardvcheck')
    return render(request, "dashboardvcheck.html")

def tencodesdispatch(request):
    return render(request, "10codesdispatch.html")

def tencodesleo(request):
    return render(request, "10codesleo.html")

def editcall(request, callId):
    context={
        "calls":Call.objects.get(id=callId)
    }

    
    return render(request, "callinfo.html", context)

def firestatus(request):
    return render(request,"editstatusfire.html")


def editstatusdispatch(request, officerId):
    c = User.objects.get(id=officerId)
    c.status = request.POST["status"]
    c.save()
    return redirect ("/dispatchdashboard")

def changestatusfire(request, officerId):
    c = User.objects.get(id=officerId)
    c.status = request.POST["status"]
    c.save()
    return redirect ("/firedashboard")


def statusdispatch(request, officerId):
    context= {
        "showStatus": User.objects.get(id=officerId)
    }
    return render(request,"dispatchchangestatus.html", context)

def idcheck(request):
    if 'term' in request.GET:
        qs = Suspect.objects.filter(name__istartswith=request.GET.get('term'))
        names = list()
        for suspect in qs:
            names.append(suspect.name)
        return JsonResponse(names, safe=False)
    if request.method=='POST':
        name = request.POST["name"]

        if name:
            match = Suspect.objects.filter(Q(name__icontains=name))

            if match:
                return render(request,"idcheck.html",{"ss":match})

            else:
                messages.error(request,"No identification found. Please reference Citation System for citation information")
        else:
            return HttpResponsRedirect('/idcheck')
    return render(request, "idcheck.html")

def submitcitation(request):
    Citation.objects.create(charge=request.POST['charge'], location=request.POST['location'], details=request.POST['details'] ,perp=Suspect.objects.get(id=request.POST['name']))
    return redirect("/idcheck")


def ai_dispatcher(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')

        # Replace with your Oracle Assistant endpoint
        oracle_assistant_endpoint = "https://your-oracle-assistant-endpoint"

        # The payload to be sent to Oracle Assistant
        payload = {
            "text": user_message,
            "session": "officer_session"  # Adjust this as per your session management
        }

        # Send the message to Oracle Assistant
        response = requests.post(oracle_assistant_endpoint, json=payload)

        # Parse the response from Oracle Assistant
        ai_response = response.json().get('response')

        return JsonResponse({'message': ai_response})

    return render(request, 'chat.html')


@csrf_exempt
def dialogflow_webhook(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        intent_name = req.get('queryResult').get('intent').get('displayName')

        if intent_name == "Plate Check":
            plate_number = req.get('queryResult').get('parameters').get('plate_number')

            # Depending on how Dialogflow parses it, you might need to handle cases where only a number is returned.
            if isinstance(plate_number, list):
                plate_number = "".join(plate_number)  # Convert list to string

            try:
                vehicle = Vehicle.objects.get(plate=plate_number.upper())
                response_text = f"Vehicle {vehicle.make} {vehicle.model}, {vehicle.year}, owned by {vehicle.owner.name}."
            except Vehicle.DoesNotExist:
                response_text = f"No vehicle found with plate number {plate_number}."

            return JsonResponse({
                "fulfillmentText": response_text
            })

    return JsonResponse({"fulfillmentText": "Error processing the request"}, status=400)
