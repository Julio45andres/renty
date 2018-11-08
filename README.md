# Aplicación Renty DoD - Desarrollo de aplicaciones empresariales 2018

Hacer pull antes de trabajar:

```bash
$ git fetch origin develop
$ git pull origin develop
```

Entrar al entorno virtual:

```bash
$ pipenv shell
```

Para correr el proyecto:

```bash
$ docker-compose run --rm web
```

Para trabajar en la rama develop:

```bash
$ git checkout develop
```

Para crear un nuevo feature, estando en la rama develop:

```bash
$ git checkout -b feature/<nombre>
```

Despues de hacer hacer los cambios confirmalos con:

```bash
$ docker-compose run --rm web python manage.py makemigrations
```

Finalmente aplicamos las migraciones al contenedor:

```bash
$ docker-compose run --rm web python manage.py migrate
```

Todo comando que se vaya a correr sobre el contenedor debe ser de la siguiente forma:

```bash
$ docker-compose run --rm web <Inserte su comando aca>
```
