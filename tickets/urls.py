from django.urls import path,include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', GuestViewSet)

urlpatterns = [
    path('fbv',FBV_List),
    path('fbv/<int:pk>',FBV_PK),
    path('cbv',CBV_List.as_view()),
    path('viewset/', include(router.urls)),
]
