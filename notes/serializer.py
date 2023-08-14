from rest_framework import serializers
from .models import Machines

class machineserializer(serializers.ModelSerializer):

    class Meta:
        model = Machines
        # fields= '__all__'
        fields = ['ok_count', 'ng_count','shift_1_ok_count','shift_1_ng_count','shift_2_ok_count','shift_2_ng_count','last_date_updated' ]
        
