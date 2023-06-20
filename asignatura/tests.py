from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Asignatura

class AsignaturaCreate(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='administradores', password= 'administradores')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token "+self.token.key)
        self.client.force_login(self.user)

    def test_create_asignatura(self):
        data = {"nombre": "Lengua", "curso":3}
        res = self.client.post('/asignatura/createAsignatura', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_asignatura(self):
        asignatura = Asignatura.objects.create(nombre="Musica", curso = 2)
        data2 = {"nombre": "E.F", "curso":3}
        res = self.client.put('/asignatura/updateAsignatura/'+str(asignatura.id), data2)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_asignatura(self):
        asignatura = Asignatura.objects.create(nombre="Musica", curso = 2)
        res = self.client.delete('/asignatura/deleteAsignatura/'+str(asignatura.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_asignatura(self):
        asignatura = Asignatura.objects.create(nombre="Musica", curso = 2)
        res = self.client.get('/asignatura/getAsignaturas/'+str(asignatura.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual('Musica', res.json()["nombre"])
    
    def test_get_all_asignatura(self):
        Asignatura.objects.create(nombre="Musica", curso = 2)
        Asignatura.objects.create(nombre="E.F", curso = 3)
        res = self.client.get('/asignatura/createAsignatura')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual([{"nombre":'Musica', "curso":2}, {"nombre":'E.F', "curso":3}],
                            res.json())
