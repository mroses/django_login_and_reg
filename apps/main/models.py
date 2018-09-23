from __future__ import unicode_literals
from django.db import models
#from ..products.models import *
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

    #will send whatever we get here back to views - either will send error or will send a user back to the views. but all validation will be here. must send errors back in order to flash messages in html.
class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []
        if len(form_data['first_name']) < 3:
            errors.append('First name must be at least 3 characters')
        if len(form_data['last_name']) < 3:
            errors.append('last_name must be at least 3 characters')
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append('Must be valid email address')
        if len(form_data['password']) < 8:
            errors.append('password must be at least 8 characters')
        if form_data['password'] != form_data['conf_pw']:
            errors.append('Password and confirm password must match')

    #OPTION 1 for validating unique email
        user_email = self.filter(email=form_data['email'])
    #this could also be user_email = User.objects.filter...We are using self because in our model, objects is overwritten by the User Manager. Since we're in the Manager here, we can just use self (either works but self is shorter)
        if len(user_email) > 0:
            errors.append('Email already in use')

    #OPTION 2 for validating unique email
    #expecting to get an error below under try because most of the time people will not be trying to register with an email that's already in use. might be better to use another filter because try and except 

        try:
            user = self.get(email=form_data['email'])
            #if this line doesn't throw an error, we know the email doesn't exist
            errors.append('email already in use')
            return (False, errors)
        except:
            if len(errors) > 0:
                return (False, errors)
            else: 
                pw_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
                user = self.create(first_name=form_data['first_name'], last_name=form_data['last_name'], email=form_data['email'], pw_hash=pw_hash)
                return (True, user)
            # (True, user) #user is defined under the try above.

    def validatelogin(self, form_data):
        errors = []

        try:
            user = self.get(email = form_data['email'])
            if bcrypt.checkpw(form['password'].encode(), user.pw_hash.encode()):
                return (True, user)
            else:
                errors.append('incorrect email or password')
                return (False, errors)
        except:
            errors.append('incorrect email or password')
            return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    #function below allows us to see the output and name rather than just an object. Helpful in debugging
    def __str__(self):
        #output = "User: {} {}".format(self.first_name, self.last_name)
        return self.first_name

 