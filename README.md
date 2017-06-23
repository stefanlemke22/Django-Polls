# Django Base

A docker-compose setup for serving static files and a
[Django](https://www.djangoproject.com/) application with
[NGINX](https://www.nginx.com/).

## Development Environment

This project utilizes [Docker](https://www.docker.com/) containers for
development environment set up.

### Docker Installation

#### macOS/Ubuntu/Windows 10
If you are using one of the
[supported platforms](https://docs.docker.com/engine/installation/#supported-platforms),
you can download and install the
[Community Edition](https://www.docker.com/community-edition#/download) of
Docker.

#### Windows 7
If you are using an older, unsupported operating system, you can download and
install the [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/).

**Note: You must set up your project within the `C:\Users`
directory for docker to map volumes corectly.**

Docker Toolbox requires you to run Docker on a virtual machine rather than
localhost. It comes with VirtualBox for this purpose. Once you have Docker
installed, you will need to run:

```
> docker-machine create default
> docker-machine env
```

Copy/paste the `env` command output in the command line to complete the
docker-machine configuration. Check https://docs.docker.com/machine/reference/env/
for more information on this topic.

### Docker Tutorials

If you are unfamiliar with Docker, you can check out these resources to learn
more.

- [Docker Docs: Get Started](https://docs.docker.com/get-started/)
- [Docker Docs: Compose and Django](https://docs.docker.com/compose/django/)
- [YouTube: Building Python apps with Docker](https://www.youtube.com/watch?v=VhabrYF1nms)

### Getting Going with Django Development

Once you have Docker installed, set the project environment variables in a
`.env` file. Be sure to generate a new unique secret key for Django.

    $ mv .env-template .env
    $ docker-compose run django python manage.py shell
    >>> from django.core.management.utils import get_random_secret_key
    >>> print(get_random_secret_key())
    >>> exit()

With the `.env` file in place you can build and run the project.

    $ docker-compose up --build -d
    $ docker-compose run django python manage.py migrate
    $ docker-compose run django python manage.py collectstatic

Everything should be running and browsable at http://localhost or your VM's ip
if your are using docker-machine (run `docker-machine ip` to see it).

From here, it's pretty much Django development as usual. If you are coming from
a development style using virtualenvs, getting used to Docker containers might
take a minute. Just know that the docker-compose volumes are mapped between your
machine and their corresponding containers and you run django commands from the
django container. For example, to start a new app, you would run
`docker-compose run django python manage.py startapp app_name`. The new
`app_name` directory will be created in the container but will also appear in
your local `django` directory where you can work on it.

### Nginx and try_files

Any files in the `nginx/try_files` directory are hosted by nginx before a
request attempt is made to the Django app. This is great for hosting .html files
and other static assets not specific to the Django app such as favicons, the .js
files for an AngularJS front-end application, or special files required by
third-party services (e.g. Google Webmaster Tools, apple-app-site-association)
