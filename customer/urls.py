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
    path('logout/',views.logout,name='logout'),
    path('payment/',views.payment,name='payment'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('remove_from_cart/<int:product_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('add_to_wishlist/<int:products_id>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('remove_from_wishlist/<int:products_id>/',views.remove_from_wishlist,name='remove_from_wishlist')



]