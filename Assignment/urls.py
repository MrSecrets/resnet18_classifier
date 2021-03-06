
"""trial URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static

from resnet import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('model/', views.call_model.as_view()),
    path('image2classify/',views.call_model().get),

    path('',views.index, name='index'),
    path('',views.index_view,name="home"),
    path('add_image', views.addImage_view , name="add_image") ,
    path('get_images', views.getImages_view , name="get_images"),
    path('', include('pwa.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
