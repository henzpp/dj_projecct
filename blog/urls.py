from django.urls import path
from . import views

urlpatterns = [
    #path('<int:pk>/', views.PostDetail.as_view()),
    #path('', views.PostList.as_view()),
    path('community/', views.community),
    path('forums/', views.forums),
    path('gallery/', views.gallery),
    path('plantrvl/', views.plantrvl),
    
]
