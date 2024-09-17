from django.urls import path
from . import views

urlpatterns = [
    path('', views.option_pricing_view, name='option_pricing'),  # URL for option pricing form and calculation
]
