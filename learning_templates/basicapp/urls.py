from django.urls import path
from basicapp import views

#templates tagging
app_name = 'basicapp'

urlpatterns = [
    path('relative/', views.relative,name='relative'),
    path('other/',views.others,name='other'),
]
