from django.db import models
from django.utils import timezone

# Create your models here.

class usuario(models.Model):
    username = models.CharField(max_length=100,verbose_name='Nombre de usuario')
    password = models.CharField(max_length=100,verbose_name='Contraseña') 
    correo = models.CharField(max_length=100, default="example@example.com")
    rol = models.CharField(max_length=100, default="user")
    Fecha_Registro = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.username} ({self.rol}) - {self.correo} - {self.Fecha_Registro}"

  
class Foro(models.Model):
    foro = models.CharField(max_length=100,verbose_name='Foro')
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion')
    Tema = models.CharField(max_length=100, verbose_name='Tema')
    fechaCreacion = models.DateField()

    

    def __str__(self):
        return f"{self.foro} - {self.titulo} - {self.Tema} - {self.fechaCreacion} - {self.Descripcion}"
    
class Foro_Participacion(models.Model):
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE)
    username = models.ForeignKey(usuario, on_delete=models.CASCADE)
    FechaParticipacion = models.DateField()

    def __str__(self):
        return f"{self.foro} - {self.username} - {self.FechaParticipacion}"


 
class Informe_Proyecto(models.Model):
    Id_reporte = models.ForeignKey(Foro, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion')
    FechaSubida = models.DateField()

    def __str__(self):
        return f"{self.Id_reporte} - {self.titulo} - {self.Descripcion} - {self.FechaSubida}"


    