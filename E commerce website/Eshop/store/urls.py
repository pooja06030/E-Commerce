from django.contrib import admin
from django.urls import path
from.views.home import index_1
#from .views import index,signup,login
from .views import home,signup,login



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.index,name='homepage'),
     path('post',home.index_1,name='post'),
    path('signup/',signup.signup,name='signup'),
    path('login',login.login, name='login'),
    path('logout',login.logout,name='logout'),
    #path('cart',cart.cart,name='logout'),
   
    #Add to card
    
   
   
]
