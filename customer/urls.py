from django.urls import path
from.import views
app_name='customer'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('masterpage/',views.masterpage,name='masterpage'),
    path('men/',views.men,name='men'),
    path('women/',views.women,name='women'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('cart/',views.cart,name='cart'),
    path('logout/',views.logout,name='logout'),
    path('payment/',views.payment,name='payment')
]