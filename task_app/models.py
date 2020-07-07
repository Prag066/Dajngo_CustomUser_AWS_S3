from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None,*args,**kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            first_name = kwargs.get('first_name',None),
            last_name = kwargs.get('last_name',None),
            profile_image = kwargs.get('profile_image',None),
            position = kwargs.get('position',None),
            location = kwargs.get('location',None),
            mobile = kwargs.get('mobile',None),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None):
        user = self.create_user(
            email,
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    profile_image = models.ImageField(upload_to='',blank=True,null=True)
    position = models.CharField(max_length=255,blank=True,null=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    def save(self,*args,**kwargs):
        super(MyUser,self).save(*args,**kwargs)
