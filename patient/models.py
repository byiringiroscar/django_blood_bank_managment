from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Patient/',null=True,blank=True)

    age=models.PositiveIntegerField()
    bloodgroup=models.CharField(max_length=10)
    disease=models.CharField(max_length=100)
    doctorname=models.CharField(max_length=50)

    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
    

class Hospitapl_service(models.Model):
    hospital_name = models.CharField(max_length=100)
    hospital_location = models.CharField(max_length=100)
    hospital_start_time = models.TimeField()
    hostptal_end_time = models.TimeField()
    post_date = models.DateTimeField(auto_created=True)
    
    
    def __str__(self):
        return f"{self.hospital_name}"
    class Meta:
        verbose_name_plural = " Hospital service"
        ordering = ['-post_date']