from django.urls import path
from tugether import views

urlpatterns = [
    path('user', views.user_list),
    path('user/<int:pk>', views.user_detail),
    path('event', views.event_list),
    path('event/<int:pk>', views.event_detail),
]