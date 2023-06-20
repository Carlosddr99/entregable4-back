from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ProfesorViewSet, "profesores")

urlpatterns = [
    path('getProfesores/<int:pk>', views.ProfesorRetrieveAPIView.as_view()),
    path('createProfesor', views.ProfesorCreateAPIView.as_view()),
    path('updateProfesor/<int:pk>', views.ProfesorUpdateAPIView.as_view()),
    path('deleteProfesor/<int:pk>', views.ProfesorDestroyAPIView.as_view()),
    path('obtenerAsignaturaProfesor', views.obtenerAsignaturaProfesor),
    path('profesores/', include(router.urls))

]