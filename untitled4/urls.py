"""untitled4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
import blog
from blog.views import page_not_found,page_error, page_forbidden

handler404 = page_not_found,
handler500 = page_error
handler403 = page_forbidden

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',include('blog.urls')),
    path(r'', include('comments.urls')),



]
