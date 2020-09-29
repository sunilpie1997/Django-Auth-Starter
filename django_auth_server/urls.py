
from django.contrib import admin
from django.urls import path,include
from .views import homePage

urlpatterns = [
    path('',homePage,name="homepage"),
    
    path('admin/', admin.site.urls),

    #this view is for changing passwords,viewing details,profile directly on this server
    path('accounts/',include("account.urls")),

    #this is for oauth 2.0 using github. you can add google,facebook,etc.Check readme
    path('oauth/', include('social_django.urls', namespace='social')),
    

]
