from rest_framework import serializers
from .models import Guest

class GuestProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('url','email','first_name','last_name','phone_number','occupation','address','country','work_place','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        password = validated_data.pop('password')
        guest = Guest(**validated_data)
        guest.username = validated_data.get('email')
        guest.set_password(password)
        guest.save()
        return guest
        