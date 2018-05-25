# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UserManager(models.Manager):
    # in classes when you are defining function they must have (self, and data 
    def register_validator(self, data):
        errors = []
        if len(data['name']) < 2 or any(char.isdigit() for char in data['name']) :
            errors.append("Invalid First Name")
        if len(data['alias']) < 1:
            errors.append("Invalid Last Name")    
        if len(data['email']) < 0:
             errors.append("Invalid Email")   
        if not email_regex.match(data['email']):
            errors.append("Invalid Email")       
        if len(data['password']) < 8 :
            errors.append("Password is too short")   
        elif data['password'] != data['confirmation'] :
            errors.append("password and confirmation aren't the same")
        if len(data['birth_day']) < 1:
            errors.append("please enter birthday")
        if self.filter(email=data['email']).count() > 0:
            errors.append("Someone with that email is already registered")  
        return errors
    def login_validator(self, data):
        # these are the checks in the views.py def login for errors.
        errors = []           
        if len(data['email']) < 0:
             errors.append("Invalid Email")   
        elif not email_regex.match(data['email']):
            errors.append("Invalid Email")      
        elif len(data['password']) < 8 :
            errors.append("Password is too short")   
        elif self.filter(email=data['email']).count() < 1:
            errors.append("You haven't registered with that email yet")  
        # if bcrypt.checkpw(data['password'].encode(), self.filter(email=data['email'])[0].password.encode()):
            # errors.append("You haven't registered with that email yet")  
        return errors
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birth_day = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class QuoteManager(models.Manager):
    def Course_validator(self, data):
        errors = []
        if len(data['quote_author']) < 3 or any(char.isdigit() for char in data['quote_author']) :
            errors.append("Please enter valid Author name")
        if len(data['quote_message']) < 10 :
            errors.append("Quote must be at least 10 characters")      
        return errors

class Quote(models.Model):
    quote_author= models.CharField(max_length=255)
    quote_message=models.CharField(max_length=500)
    quote_creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_quotes')
    favorites = models.ManyToManyField(User,related_name='favorites')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=QuoteManager()



