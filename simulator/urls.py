from django.urls import path
from . import views

urlpatterns = [ #urls to different parts of our site 
    path('',views.home, name = 'simulator-home'), #format goes link, function, name
    path('about/',views.about, name = 'simulator-about'),  #someone went to about page, lets send the request
     path('portfolio/',views.userPortfolio, name = 'simulator-user-portfolio'),  #someone went to portfolio page, lets send the request

]