from __future__ import unicode_literals
from .models import Temperature,Humidity,Moisture,Waterlevel 
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def index(request):
	temp_data=Temperature.objects.all()[len(Temperature.objects.all())-1]
	temp_data=str(temp_data)
	hum_data=Humidity.objects.all()[len(Humidity.objects.all())-1]
	hum_data=str(hum_data)
	moi_data=Moisture.objects.all()[len(Moisture.objects.all())-1]
	moi_data=str(moi_data)
	water_data=Waterlevel.objects.all()[len(Waterlevel.objects.all())-1]
	water_data=str(water_data)
	context={'sensor1':temp_data,'sensor2':hum_data,'sensor3':moi_data,'sensor4':water_data}
	return render(request,'temperature/index.html',context)
def getdata(request):
	if request.method=='GET' :
		temp_value=request.GET['temperature']
		t_obj=Temperature()
		t_obj.tem_value=temp_value
		t_obj.save()
		hum_value=request.GET['humidity']
		h_obj=Humidity()
		h_obj.hum_value=hum_value
		h_obj.save()
		#moi_value=request.GET['moisture']
		#m_obj=Moisture()
		#m_obj.moi_value=moi_value
		#m_obj.save()
		water_value=request.GET['waterlevel']
		w_obj=Waterlevel()
		w_obj.water_value=water_value
		w_obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")

