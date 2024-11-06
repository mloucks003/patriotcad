from django.db import models
from datetime import date
import re



class UserManager(models.Manager):

    def registerValidator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        logUser = User.objects.filter(email=postData['email'])
        # name required
        if len(postData['badge']) == 0:
            errors['badgereq'] = "Must Enter Badge Number"
        # username required
        if len(postData['last_name']) == 0:
            errors['usernamereq'] = "Must Enter a Last Name"
        if len(postData['email']) == 0:
            errors['emailreq'] = "Must Enter Email"
        #email in correct format
        elif not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['emailpattern'] = "Invalid email address!"

        # password required with at least 8 characters
        if len(postData['password']) < 8:
            errors['passreq'] = "Password needs to be eight characters long"     
        #password and confirmed password must match
        if postData['cpass'] != postData['cpass']:
            errors['cpass'] = "Passwords must match"

        return errors


        

    def loginValidator(self, postData):
        errors = {}
        
        
        #email in correct format
        logUser = User.objects.filter(badge=postData['badge'])
        # print(logUser)
        if len(logUser) == 0:
            errors['valid email'] = "Badge number is required. If not registered, please contact administration to register"
        #if email is taken already
        
        else:
            if logUser[0].password != postData['password']:
                errors['passmatch'] = ["Incorrect password!"]
                print("Valid email")
                print("password incorrect")
        
        return errors

    def dispatchValidator(self, postData):
        errors = {}
        
        
        #email in correct format
        logDispatch = Dispatcher.objects.filter(user_name=postData['username'])
        # print(logUser)
        if len(logDispatch) == 0:
            errors['valid username'] = "Username is required. If not registered, please contact administration to register"
        #if email is taken already
        
        else:
            if logDispatch[0].password != postData['password']:
                errors['passmatch'] = ["Incorrect password!"]
                print("Valid email")
                print("password incorrect")
        
        return errors

    def dispatchRegister(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        logDispatch = Dispatcher.objects.filter(email=postData['email'])
        # name required
        if len(postData['username']) == 0:
            errors['usernameReq'] = "Must Enter Username"
        # username required
        if len(postData['last_name']) == 0:
            errors['lnameereq'] = "Must Enter a Last Name"
        if len(postData['email']) == 0:
            errors['emailreq'] = "Must Enter Email"
        #email in correct format
        elif not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['emailpattern'] = "Invalid email address!"

        # password required with at least 8 characters
        if len(postData['password']) < 8:
            errors['passreq'] = "Password needs to be eight characters long"     
        #password and confirmed password must match
        if postData['cpass'] != postData['cpass']:
            errors['cpass'] = "Passwords must match"

        return errors


# -----------------------------------One To Many---------------------------------------
class User(models.Model):
    last_name=models.CharField(max_length=255, default="")
    aop=models.CharField(max_length= 255,default="" )
    status=models.CharField(max_length=255, default="")
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    badge = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =UserManager()
    def __str__ (self):
            return self.badge


class Suspect(models.Model):
    name = models.CharField(max_length=255)
    password= models.name = models.CharField(max_length=255, null=True)
    alias = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    dob= models.DateTimeField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__ (self):
        return self.name

class Arrest(models.Model):
    reason= models.CharField(max_length=255, null=True)
    circumstances = models.CharField(max_length=255,  null=True)
    perp = models.ForeignKey(Suspect,  related_name ="arrests", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Citation(models.Model):
    charge= models.CharField(max_length=255, null=True)
    location= models.CharField(max_length=255, null=True)
    details= models.CharField(max_length=255, null=True)
    perp = models.ForeignKey(Suspect,  related_name ="citations", on_delete = models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Warrant(models.Model):
    reason= models.CharField(max_length=255, null=True)
    location= models.CharField(max_length=255, null=True)
    warranty = models.ForeignKey(Suspect,  related_name ="warrants", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Vehicle(models.Model):
    make = models.CharField(max_length=255)
    model= models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    year = models.IntegerField()
    plate = models.CharField(max_length=255)
    registration = models.CharField(max_length=255, null=True)
    insurance= models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(Suspect,  related_name ="vehicles", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__ (self):
        return self.plate


# ------------------------------- One To Many----------- Also Many to Many Factor----------------------

class Call(models.Model):
    location = models.CharField(max_length=255)
    description = models.TextField()
    code = models.IntegerField()
    assigned_officer = models.ManyToManyField(User, related_name="calls")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Dispatcher(models.Model):
    user_name= models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255 ,null=True)
    email = models.name = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Fire (models.Model):
    last_name=models.CharField(max_length=255, default="")
    status=models.CharField(max_length=255, default="")
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    badge = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =UserManager()
    def __str__ (self):
            return self.last_name

    # calls models