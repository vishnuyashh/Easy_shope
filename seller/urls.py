from django.urls import path
from.import views 
app_name='seller'
urlpatterns=[
    path('s_index/',views.s_index,name='s_index'),
    path('addpdt/',views.addpdt,name='addpdt'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('product_update/',views.product_update,name='product_update'),
    path('s_login/',views.s_login,name='s_login'),
    path('s_register/',views.s_register,name='s_register'),
    path('s_masterpage/',views.s_masterpage,name='s_masterpage'),
    path('remove/<int:category_id>',views.remove,name='remove'),
    path('update/<int:pid>',views.product_update,name='product_update'),
    path('s_logout/',views.s_logout,name='s_logout')
]