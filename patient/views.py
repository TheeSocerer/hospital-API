from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Patient, MedicalRecord
from .serializers import PatientSerializer, MedicalRecordSerializer
from rest_framework.authtoken.views import obtain_auth_token 

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'patient_id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient_id', 'first_name', 'last_name', 'email']

    def get_object(self):
        return get_object_or_404(Patient, patient_id=self.kwargs['patient_id'])

    @action(detail=True, methods=['post'])
    def add_medical_record(self, request, patient_id=None):
        patient = self.get_object()
        serializer = MedicalRecordSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(patient=patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def medical_history(self, request, patient_id=None):
        patient = self.get_object()
        medical_records = patient.medical_records.all()
        serializer = MedicalRecordSerializer(medical_records, many=True)
        return Response(serializer.data)