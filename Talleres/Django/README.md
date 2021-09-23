<div align="center">
    <h1>RESUMEN DE COMANDOS</h1>
</div>

## Comandos generales - configuración

* Creación del proyecto django: `django-admin startproject <nomProyecto>`

* Ejecutar el servidor local: `python manage.py runserver`

* Crear aplicación: `python manage.py startapp <nomApp>`

* Añadir aplicación en `settings.py`:

```
INSTALLED_APPS = [
    ...,
    '<nomApp>'
]
```

* Ejecutar migraciones: `python manage.py makemigrations` y `python manage.py migrate`

* Desarrollo de pruebas de lógica CRUD y del proyecto django en general: `python manage.py shell`

* Configuración de la librería `rest_framework` en `settings.py`:

```
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

```

## Modelos del proyecto - CRUD

* `models.Model` permite la creación de las tablas SQL a través de clases de Python. Se emplea durante relaciones de herencia.

* `models.CharField(max_length= <int>)` se emplea para la creación de atributos de tipo texto. Permite especificar la cantidad de caracteres.

* `models.IntegerField()` se utiliza para el almacenamiento de valores numéricos. Sólo números enteros.

* `models.FloatField()` permite almacenar números decimales.

* `models.ImageField()` se emplea para guardar imágenes y fotografías.

* `models.FileField()` se utiliza para guardar cualquier tipo de archivo (video, audio, pdf, word, etc).

* `models.ForeignKey(<nomClaseModelo>, on_delete=models.CASCADE)` sirve para crear conexión entre tablas SQL y entre objetos CRUD.

* `models.ManyToManyField(<nomClaseModelo>)` se emplea para registrar conexiones entre múltiples tablas SQL y objetos CRUD de Python.

## Administración CRUD manual

Para el registro de modelos en la sección de _django-admin_ (localhost:8000/admin), debes hacer lo siguiente en `admin.py`:

```PYTHON
from django.contrib import admin

from <nomApp>.models import *

admin.site.register(<nomClaseModelo>)
...

```

Para crear usuarios de tipo administrador, debes ejecutar: `python manage.py createsuperuser`

## Serializadores

* `from rest_framework import serializers` importa los serializadores al proyecto.
* `serializers.Serializer` permite crear un serializador básico. Se emplea en relaciones de _herencia_.
* `serializers.ModelSerializer` crea serializadores con base en los modelos del proyecto. Se emplea en relaciones de _herencia_.
* `serializers.CharField()` se emplea para atributos de tipo texto a serializar.
* `serializers.IntegerField()` permite serializar atributos de tipo entero.
* `serializers.FloatField()` serializa atributos de números decimales.

Ejemplo _ModelSerializer_:

```PYTHON
from rest_framework import serializers

from Productos.models import *

class TipoSerial(serializers.ModelSerializer):
    class Meta:
        model = TipoElectrodomestico
        fields = '__all__'
        #fields = ["nombre", "foto"]
```

Ejemplo _Serializer_:

```PYTHON
from rest_framework import serializers

from Productos.models import *

class TipoSerial(serializers.Serializer):
    nombre = serializers.CharField(max_length=200)
    foto = serializers.ImageField()
```

## Resumen CRUD y serializadores - `shell`

```PYTHON
from <nomApp>.models import *

#OBTENCIÓN DE DATOS
todosObjsCRUD = <nomClaseCRUD>.objects.all()                        #Todos los objetos

objsCRUD = <nomClaseCRUD>.objects.filter(<nomAtributo> = <valor>)   #Todos los objetos que cumplan las condiciones

objCRUD = <nomClaseCRUD>.objects.get(<nomAtributo> = <valor>)       #Obtiene el objeto que cumpla la condición (sólo puede ser uno)

#CREACIÓN DE DATOS SQL 

nuevoObj = <nomClase>.objects.create(<nomAtributo1> = <valor>, ...)

#CONEXIONES 'ForeignKey'

<objsCRUDHijos> = <objCRUDpadre>.<nomClassHija>_set.all()

#Ejemplo ForeignKey

computadores = Tecnologia.pc_set.all()

#PROBAR SERIALIZADOR
from <nomApp>.serializers import *

objCRUD = <nomClaseCRUD>.objects.get(<nomAtributo> = <valor>)

objSerial = <nomClaseSerial>(objCRUD)

objSerial.data

```

## Errores comunes

* `ImportError: No module named PIL`. Solución: instalar la librería mediante `python -m pip install Pillow`.
* `no such table: ...` no hay registro de tabla SQL. Solución: correr las migraciones `python manage.py makemigrations` y `python manage.py migrate`
