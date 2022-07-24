from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    '''manager for user profile'''
    def create_user(self,email,name,password=None):
        ''' create new user pofile'''
        if not email:
            raise ValueError('User must have email address ')
        
        email = self.normalize_email(email)
        user = self.model(email=email,name= name)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff   = True
        user.save(using=self._db)
        return user 
        






# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.CharField(max_length=20, unique = True)
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
     
    objects = UserProfileManager()
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['name']
    
    def  get_full_name(self):
        '''retrive full name of User'''
        return self.name
    
    def  get_short_name(self):
        '''retrive short name of User'''
        return self.name
    def __str__(self):
        '''return string repersant to our users'''
        return self.email