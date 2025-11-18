from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', GuestViewSet)

urlpatterns = [
    path('fbv',FBV_List),
    path('fbv/<int:pk>',FBV_PK),
    path('cbv',CBV_List.as_view()),
    path('viewset/', include(router.urls)),
    # path('gen_post/',PostView.as_view())
    path('gen_post_pk/<int:pk>',PostView.as_view())
]
