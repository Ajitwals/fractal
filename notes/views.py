from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import machineserializer

def home(request, *args, **kwargs):
    # plant= Plant_1.objects.all()
    # machines = Machines.objects.all()
    # print(plant,machines)
    if request.user.is_authenticated:
        username = request.user.username
        print(username)
    
    return render(request, 'home.html')

@api_view(['PATCH','GET'])
def patch_machine_data(request):


    if request.method == 'GET':

        machine_names = Machines.objects.all()
        serializer = machineserializer(machine_names,many=True)
        return Response({
                    'status':True,
                    'message':'data fetched successfully',
                    'data':serializer.data
                                })
    


    if request.method == 'PATCH':

        try:
            data = request.data
            
            if not data.get('machine_name'):
                return Response({
                    'response':False,
                    'message':'Please enter a valid machine name',
                    'data':{}
                })
            obj= Machines.objects.get(machine_name=data.get('machine_name'))

            serializer = machineserializer(obj,data=data, partial = True)
            if serializer.is_valid():
                serializer.save() 

                return Response({
                    'status':True,
                    'message':'count updated successfully',
                    'data':serializer.data
                                })

            return Response({
                    'status':False,
                    'message':'Error updating count',
                    'data':serializer.errors,})
        except Exception as e:
            return  Response({
                'status':False,
                'message':request.data,
            })