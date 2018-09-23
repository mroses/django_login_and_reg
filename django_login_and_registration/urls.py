"""django_login_and_registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

#we have two apps - 'main' and 'products' we need to decide the root route. in this case if the website is about products, we may want to have the root route to be the products page
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('apps.main.urls', namespace='users')), #this goes to main which is actually the users app.
    url(r'^', include('apps.products.urls', namespace="products")) #this goes last because it is more general. anything will get caught by this url so it should go last with more specific routes first.
]
#this project level (not app level) urls file has more than we typically have in here because we have the 2 apps instead of one.