
from django.urls import path
from . import views

urlpatterns = [
    path('getAsignaturas/<int:pk>', views.AsignaturaRetrieveAPIView.as_view()),
    path('createAsignatura', views.AsignaturaCreateAPIView.as_view()),
    path('updateAsignatura/<int:pk>', views.AsignaturaUpdateAPIView.as_view()),
    path('deleteAsignatura/<int:pk>', views.AsignaturaDestroyAPIView.as_view()),

]