from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = "home"),
    path('check', views.asiwaju, name='check'),
    path('greet',views.greeting, name='come'),
    # path('greetings/<str:name>/<int:age>' , views.greeting , name='greet')
    path('greetings/<str:name>/<str:age>' , views.greeting , name='greet'),
    path('products',views.skincare, name='products'),
    path("blog/<str:id>" ,views.reading,name="read"),
    path("create" ,views.createblog,name="yourblog"),
    path("delete/<str:id>",views.delete,name='clear'),
    path("edit/,<str:id>",views.edit,name='edit'),
    
]