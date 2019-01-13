from django.contrib import admin
from django.urls import path
from . import views as shift_views
from django.contrib.auth import views as auth_views

# app_name = 'shifts'

urlpatterns = [
    path('', shift_views.index, name="index"),
    path('initial_page/', shift_views.initial_page, name="initial_page"),
    path('submit/', shift_views.create_shift, name='submit'),
    path('select/', shift_views.filter_shifts_by_date, name='select'),
    path('edit/<int:pk>/', shift_views.update_shift, name='edit'),
    path('detail/<int:pk>/', shift_views.shift_detail, name='detail'),
    path('remove/<int:pk>/', shift_views.remove_shift, name='remove'),
    path('select/<str:date_from>/<str:date_to>/', shift_views.select_payment_period, name='select'),
]