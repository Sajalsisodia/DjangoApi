
from django.urls import path,include
from profile_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet , basename='hello-viewset')


urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))  #it include all the urls of viewsets class function we not need to create saprate 
    
    
]