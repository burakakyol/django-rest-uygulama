from app1.models import Kitap,Yazar
from rest_framework import serializers

class YazarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Yazar
        fields=('isim','soyisim','kitaplar')


class KitapSerializer(serializers.ModelSerializer):
    class Meta:
        model=Kitap
        fields=('baslik',)