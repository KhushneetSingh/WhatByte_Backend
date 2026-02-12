from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    RegisterSerializer,
    PatientSerializer,
    DoctorSerializer,
    MappingSerializer
)
from rest_framework.decorators import action
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    
class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer

    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def get_doctors_for_patient(self, request, patient_id=None):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)