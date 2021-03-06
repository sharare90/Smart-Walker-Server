"""SmartWalkerServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1.jpg. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1.jpg. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1.jpg. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name=''),
    path('add_line', views.add_line, name='add_line'),
    path('create_file', views.create_file, name='create_file'),
    path('add_image', views.add_image, name='add_image'),
    path('create_image_directory', views.create_image_directory, name='create_image_directory')
]
