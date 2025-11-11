from django.urls import path,include
from .views import nomodelnorest

urlpatterns = [
    path('',nomodelnorest),

]
