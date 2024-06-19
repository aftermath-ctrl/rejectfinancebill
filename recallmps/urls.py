
from django.urls import path
from .views import MPListView
from . import views

urlpatterns = [
	path('', MPListView.as_view(), name='mp_list'),
	path('upload-pdf/', views.upload_pdf, name='upload_pdf'),
]