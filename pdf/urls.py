

from django.contrib import admin
from django.urls import path
from . import views


app_name = "pdf"

urlpatterns = [
	path('', views.pdf_marge, name="pdf_marge"),

]

