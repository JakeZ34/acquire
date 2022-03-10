from django.db import models, requests

# Create your models here.
'''from django.db import models, migrations
import bcrypt
import re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'
        
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'
        
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid Email Address'
        
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Already in use"
        if not email_checker.match(postdata['email']):
            errors['email'] = 'Email must be valid'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors
    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False
        user=users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())
    def register(self, postData):
        pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = pw,
        )
        return errors

class User(models.Model):
    #first_name = models.CharField(max_length=55)
    #ast_name = models.CharField(max_length=55)
    #email = models.EmailField(unique=True)
    #password = models.CharField(max_length=255)
    #objects = UserManager()

class PostManager(models.Manager):
    def post_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "Post must have a title"
        if len(postData['description']) < 1:
            errors['description'] = "Post must have a description"
        if len(postData['mess']) < 1:
            errors['mess'] = "Link must not be empty"
        return errors

class Post(models.Model):
    message = models.URLField(max_length=200)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    #image = models.ImageField()
    poster = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager() 
#'''