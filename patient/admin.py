from django.contrib import admin
from .models import Patient, MedicalRecord

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'date_of_birth', 'contact_number')
    search_fields = ('patient_id', 'first_name', 'last_name')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'diagnosis', 'visit_date')
    list_filter = ('visit_date',)
    search_fields = ('patient__patient_id', 'diagnosis')
