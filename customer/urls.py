from django.urls import path
from.import views
app_name='customer'
urlpatterns=[
    path('index',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('masterpage/',views.masterpage,name='masterpage'),
    path('men/',views.men,name='men'),
    path('women/',views.women,name='women'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about')
]