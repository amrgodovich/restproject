from django.urls import path,include
from .views import *

urlpatterns = [
    path('fbv',FBV_List),
    path('fbv/<int:pk>',FBV_PK),

]
