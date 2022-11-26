from django import forms
from camps.models import Hospital_service


class HospitalServiceForm(forms.ModelForm):
    class Meta:
        model = Hospital_service
        fields = ['hospital_name', 'hospital_location', 'hospital_start_time', 'hospital_end_time', 'hospital_phone']