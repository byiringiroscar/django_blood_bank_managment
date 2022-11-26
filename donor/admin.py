from django.contrib import admin
from donor.models import Donor, BloodDonate

# Register your models here.


admin.site.register(Donor)

admin.site.register(BloodDonate)
