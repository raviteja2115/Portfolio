from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('proj/', views.project, name="project"),
    path('contact/', views.contact, name="contact"),
    path('proj/cen/', views.cen, name="cen"),
    path('proj/crd/', views.crd, name="crd"),
    path('proj/gvds/', views.gvds, name="gvds"),
    path('fetch_file_content/', views.fetch_file_content, name="fetch_file_content"),
    path('execute_script/', views.execute_script, name='execute_script'),
]
