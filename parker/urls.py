
from django.urls import path
from . import views

urlpatterns =[
    path('signup/',views.Sign_up),
    path('login/',views.log_in),
    path('slots/',views.Catch_camera),
    path('end/',views.end_journey),
    path('parkings/',views.parkings),
    path('createpark/',views.create_park),
    path('confirmbook/',views.confirm_Book),
    path('myparkings/',views.Owners_parkings),
    path('payment/',views.payment),
    path('parking/create',views.parking_create)
]
