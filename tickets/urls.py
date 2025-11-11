from django.urls import path,include
from .views import nomodelnorest,index

urlpatterns = [
    # path('',nomodelnorest),
    path('',index),

]
