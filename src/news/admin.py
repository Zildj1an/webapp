from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Regis

class AdminRegis(admin.ModelAdmin):
	list_display = ["email", "name", "timestamp"]
	form  =RegModelForm
	#list_display_links = ["name"]
	list_filter = ["timestamp"]
	list_editable = ["name"]
	search_fields = ["email","name"]
	#class Meta:
	#	model = Regis


admin.site.register(Regis, AdminRegis)