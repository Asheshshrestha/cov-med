from django.db import models
from django.forms import widgets


    

class WebsiteSettingModel(models.Model):
    VERSION_CHOOSE = (('V2','V2'),('V2 Invisible','V2 Invisible'),('V3','V3'))
    website_name = models.CharField(max_length=100,null=False,blank=False)
    show_website_name = models.BooleanField(blank=True,default=False)
    captcha_version = models.CharField(max_length=30,choices=VERSION_CHOOSE,null=True,blank=True)
    site_key = models.CharField(max_length=100,null=True,blank=True)
    secret_key = models.CharField(max_length=100,null=True,blank=True)
    enable_captcha = models.BooleanField(blank=True)
    logo_image = models.ImageField()
    favicon = models.ImageField()
    copyright = models.CharField(max_length=200,blank=True,null=True)
    


