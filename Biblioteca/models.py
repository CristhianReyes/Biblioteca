from django.db import models

class Editor (model.Model):
    nombre = models.CharField(max_lenght=30)
    domicilio = models.CharField(max_lenght=50)
    ciudad = models.CharField(max_lenght=60)
    estado = models.CharField(max_lenght=30)
    pais = models.CharField(max_lenght=50)
    website = models.URLField()

    def __unicode__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_lenght=30)
    apellido = models.CharField(max_lenght=40)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        cadena = "%s %s" %(self.nombre, self.apellido)
        return cadena

class Libro(models.Model):
    titulo = models.CharField(max_lenght=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to = 'portadas/')
    sinopsis = models.TextField(blank=True)

    def __unicode__(self):
        return self.titulo
