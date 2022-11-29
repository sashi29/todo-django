from django.urls import path  
from .import views
urlpatterns=[ 
    path('',views.home,name='home'), 
    path('addtask',views.addtask,name='addtask'), 
    path('changestatus/<str:id>',views.changestatus,name="changestatus"),
    path('delete/<str:id>',views.delete,name='delete'),
]