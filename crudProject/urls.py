from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from crudApp import views

router = routers.DefaultRouter()
router.register('student', views.StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crudApp.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
