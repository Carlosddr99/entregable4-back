from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Profesor, Asignatura

class ProfesorCreate(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='administradores', password= 'administradores')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token "+self.token.key)
        self.client.force_login(self.user)

    def test_create_profesor(self):
        data = {"nombre": "Maria", "edad":60}
        res = self.client.post('/profesor/createProfesor', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_profesor(self):
        asignatura = Asignatura.objects.create(nombre="Musica", curso = 2)
        profesor = Profesor.objects.create(nombre = "Maria", edad = 60, asignatura = asignatura)
        data2 = {"nombre": "Lucia", "edad":25, "curso": 2}
        res = self.client.put('/profesor/updateProfesor/'+str(profesor.id), data2)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_profesor(self):
        asignatura = Asignatura.objects.create(nombre="Musica", curso = 2)
        profesor = Profesor.objects.create(nombre = "Maria", edad = 60, asignatura = asignatura)
        res = self.client.delete('/profesor/deleteProfesor/'+str(profesor.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_profesor(self):
        asignatura = Asignatura.objects.create(nombre="Musica", curso = 2)
        profesor = Profesor.objects.create(nombre = "Maria", edad = 60, asignatura = asignatura)
        res = self.client.get('/profesor/getProfesores/'+str(profesor.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual('Maria', res.json()["nombre"])
    
    def test_get_all_profesor(self):
        Profesor.objects.create(nombre = "Maria", edad = 60)
        Profesor.objects.create(nombre = "Paco", edad = 50)
        res = self.client.get('/profesor/createProfesor')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual([{"nombre":'Maria', "edad":60, "asignatura":None}, {"nombre":'Paco', "edad":50, "asignatura":None}],
                            res.json())