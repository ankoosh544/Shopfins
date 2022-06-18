"""shopfins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  django.conf.urls.static import static
from shopfins import settings
from django.views.generic import TemplateView

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', TemplateView.as_view(template_name='common.html'), name='home'),
        path('about-us/',TemplateView.as_view(template_name='about-us.html'), name = 'about-us'),
        path('contact-us/', TemplateView.as_view(template_name='contact-us.html'), name='contact-us'),
        path('personal-loan/',TemplateView.as_view(template_name='personal-loan.html'), name ='personal-loan'),
        path('home-loan/', TemplateView.as_view(template_name='home-loan.html'), name='home-loan'),
        path('business-loan/', TemplateView.as_view(template_name='business-loan.html'), name='business-loan'),
        path('auto-loan/', TemplateView.as_view(template_name='auto-loan.html'), name='auto-loan'),
        path('life-insurance/', TemplateView.as_view(template_name='life-insurance.html'), name='life-insurance'),
        path('motor-insurance/', TemplateView.as_view(template_name='motor-insurance.html'), name='motor-insurance'),
        path('health-insurance/', TemplateView.as_view(template_name='health-insurance.html'), name='health-insurance'),
        path('mutual-fund/', TemplateView.as_view(template_name='mutual-fund.html'), name='mutual-fund'),
        path('stock-trading/', TemplateView.as_view(template_name='stock-trading.html'), name='stock-trading'),
        path('bonds/', TemplateView.as_view(template_name='bonds.html'), name='bonds'),
        path('personal-loan-calculator/', TemplateView.as_view(template_name='personal-loan-calculator.html'), name ='personal-loan-calculator'),
        path('home-loan-calculator/', TemplateView.as_view(template_name='home-loan-calculator.html'), name = 'home-loan-calculator'),
        path('car-loan-calculator/', TemplateView.as_view(template_name= 'car-loan-calculator.html'), name = 'car-loan-calculator'),
        path('Sign-in/', TemplateView.as_view(template_name='Sign-in.html'), name = 'Sign-in'),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
