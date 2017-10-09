from rest_framework import viewsets
from app1.models import Yazar,Kitap
from app1.serializers import YazarSerializer,KitapSerializer

class YazarViewSet(viewsets.ModelViewSet):

    queryset = Yazar.objects.all()
    serializer_class = YazarSerializer

class KitapViewSet(viewsets.ModelViewSet):
   
   
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer