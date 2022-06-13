
from django.urls import path, include
from django.conf.urls import include
from . import views
#from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)# no need of base name with model viewset
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),

]
