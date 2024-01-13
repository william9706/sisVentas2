# Sisventas!

Alquila mejor. Preocupate menos. Dora le brinda tranquilidad a los propietarios, y facilita la vida del arrendatario.

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![pipeline status](https://gitlab.com/hola-dora/dora/badges/master/pipeline.svg)](https://gitlab.com/hola-dora/dora/-/commits/master)
[![coverage report](https://gitlab.com/hola-dora/dora/badges/master/coverage.svg)](https://gitlab.com/hola-dora/dora/-/commits/master)
[![Latest Release](https://gitlab.com/hola-dora/dora/-/badges/release.svg)](https://gitlab.com/hola-dora/dora/-/releases)

El proyecto fue construido usando la base de código del [cookiecutter](https://github.com/cookiecutter/cookiecutter) para [Django](https://github.com/cookiecutter/cookiecutter-django), y algunas de las referencias estan mejor descritas directamente en algunas de las secciones de la [documentación](http://cookiecutter-django.readthedocs.io/en/latest/)

## Settings

Usa las variables y constantes de configuración, detalladas en la documentación: [configuraciones](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Docker

El proyecto esta fuentemente cimentado en el uso de Docker, y docker compose, tan para los entornos de desarrollo, como producción. Para mas detalles, verificar los comandos en [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### OpenSearch

[OpenSearch](https://opensearch.org/) es un search engine open source. Es usado en Dora para indexar los elementos de la base de datos y acelerar la búsqueda. En producción, se utiliza el servicio [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/). Sin embargo, para las instancias local y staging se utiliza a través de [docker](https://opensearch.org/downloads.html).

Para integrar Django con OpenSearch se usa [Django Opensearch DSL](https://django-opensearch-dsl.readthedocs.io/en/latest/)

### Management commands

Para crear los índices:

`python manage.py opensearch index create`

Para actualizar los índices con las instancias ya existentes

`python manage.py opensearch document index`

[Lista completa](https://django-opensearch-dsl.readthedocs.io/en/latest/management/)

#### Consideración para Staging

En staging, el usuario por defecto es actualizado sobreescribiendo el archivo `internal_users.yml`

Para más información, revisar estos enlaces:

- [internal_users.yml](https://opensearch.org/docs/latest/security/configuration/yaml/#internal_usersyml)
- [Applying changes to configuration files](https://opensearch.org/docs/latest/security/configuration/security-admin/)

#### Consideración para MacOS

Para correr openSearch en docker, se requiere actualizar este valor en la máquina virtual `vm.max_map_count=262144`. Según la [documentación oficial](https://www.elastic.co/guide/en/elasticsearch/reference/5.1/docker.html#docker-cli-run-prod-mode), se debe correr:

```
    screen ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/tty
    sysctl -w vm.max_map_count=262144
```

Sin embargo, las versiones más recientes de docker no tienen el archivo requerido para correr el comando anterior. En este caso, revisar [esta respuesta](https://stackoverflow.com/a/77431685)

#### Consideración para Windows

Para actualizar este valor, se debe utilizar wsl para conectarse a la máquina virtual de docker. [Este artículo](https://dev.to/shunmare/configuring-vmmaxmapcount-for-elasticsearch-in-docker-using-wsl-3fhc) puede ser de utilidad

## Comandos basicos de trabajo

### Configurando usarios

- Para crear una cuenta de **usuario normal**, solo es necesario realizar el flujo de registro de usuario, ya implementado en el proyecto. El flujo en un entorno de desarollo imprime los registros al gestor de correo SMTP en la consola, donde puede ver el enlace para validar el correo suministrador.

- Para crear una cuenta de **superusuario**, solo es correr el comando:

      $ docker compose -f local.yml run --rm django python manage.py createsuperuser

### Migraciones

    $ docker compose -f local.yml run --rm django python manage.py makemigrations
    $ docker compose -f local.yml run --rm django python manage.py migrate

### Validación de tipado

Running type checks with mypy:

    $ docker compose -f local.yml run --rm django mypy holadora

### Análisis de código estatico

El proyecto incluye Flake8, Bandit, y PyLint, para los dos primeros, solo es correr el proceso directamente en el archivo del proyecto. Para el caso de PyLint, si se hace necesaria la configuración de las variables del proyecto, por lo que se corre directamente en Docker.

    $ docker compose -f local.yml run --rm django pylint holadora

### Cobertura de pruebas

Para correr las pruebas, es importante usar la cobertura de los mismos, lo que ademas permite visualizar en resultado en un reporte HTML:

    $ docker compose -f local.yml run --rm django coverage run -m pytest
    $ docker compose -f local.yml run --rm django coverage html
    $ open htmlcov/index.html

#### Correr los test usando pytest

    $ docker compose -f local.yml run --rm django pytest

### Celery

La aplicación usa Celery.

```bash
cd dora
celery -A config.celery_app worker -l info
```

Es importante tener presente que para que funcionen las opciones de Celery, es importante la ubicación donde se corren los comandos; es ideal correr los comandos de Celery desde la misma ubicación donde está el archivo _manage.py_ del proyecto.

### Email Server

Para desarrollo se cuenta con un contenedor de Docker del cliente SMTP local [MailHog](https://github.com/mailhog/MailHog), y se lanza automaticamente en el momento en que se inicia el servicio de _docker compose_. Para ver la interfaz web, solo se necesita ir a `http://127.0.0.1:8025`.

## Despliegue a producción

Para mayor información sobre el despliegue del proyecto en entornos de producción, revisar la documentación [usando Docker](https://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html)

### Heroku

Es posible desplegar la aplicación en Heroku [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

### Management command

Es posible crear comandos propios en las aplicaciones de Holadora [manage.py <command> [options]](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/).

Running management command:

- Para conocer la lista de comandos que hay actualmente en el **holadora**, solo es correr el comando:

      $ docker compose -f local.yml run --rm django python manage.py help

- Para ejecutar alguno de los comandos de **holadora**, solo es correr el comando:
  command = Cualquier comando que aparezca en el help.
  options = Argumentos o variables que se hayan definido dentro del comando.

      $ docker compose -f local.yml run --rm django python manage.py <command> [options]
