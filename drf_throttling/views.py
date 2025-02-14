from rest_framework import viewsets
from jwt_auth.models import Student
from jwt_auth.serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import SanjanaRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, SanjanaRateThrottle]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'roll', 'city']
    search_fields = ['name', 'roll', 'city']
    search_fields = ['^name', '^roll', '^city']
    ordering_fields = ['name', 'roll', 'city']