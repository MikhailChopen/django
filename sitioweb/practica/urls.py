from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^estudiantes/$', views.estudiantes, name='estudiantes'),
    url(r'^asignaciones/$', views.asignaciones, name='asignaciones'),
    url(r'^Editar_estudiantes/$', views.editarestu, name='editarestu'),
    url(r'^Editar_asignacion/$', views.editarasig, name='editarasig'),
]