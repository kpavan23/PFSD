from django.urls import path
from . import views
urlpatterns=[
    path("TravelManagementhome",views.TravelManagementhome,name="TravelManagementhome"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),

]
