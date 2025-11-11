from django.urls import path,include
from .views import *

urlpatterns = [
    path('fbv',FBV_List),
    path('fbv/<int:pk>',FBV_PK),
    path('cbv',CBV_List.as_view()),

]
