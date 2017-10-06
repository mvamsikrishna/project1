# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Temperature,Humidity,Moisture,Waterlevel
admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Moisture)
admin.site.register(Waterlevel)
