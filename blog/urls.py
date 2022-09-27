from django.urls import path
from . import views

urlpatterns = [
    #path('<int:pk>/', views.PostDetail.as_view()),
    #path('', views.PostList.as_view()),
    path('community/', views.community),
    path('forums/', views.forums, name='forums'),
    path('gallery/', views.gallery),
    path('places/', views.places),
    path('forums_result/', views.forums_result, name='forums_result'),
    path('forums_result2/', views.forums_result2, name='forums_result2'),
    path('forums_result3/', views.forums_result3, name='forums_result3'),
    path('forums_result4/', views.forums_result4, name='forums_result4'),
]
