from django.contrib import admin
from django.urls import path, include
from carsapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cars/',views.CarViewSet.as_view()),
    path('popular/',views.PopularCarViewSet.as_view()),
    path('rate/',views.CarRateViewSet.as_view()),
]
