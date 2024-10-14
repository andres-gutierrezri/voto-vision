"""
Django settings for project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# Importar os para manejar las variables de entorno
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from dotenv import load_dotenv
from VOTO_VISION.local_settings import IS_DEPLOYED, DATABASE_DICT
from VOTO_VISION.logging_settings import *
from VOTO_VISION.cloud_settings import *

# Carga las variables de entorno del archivo .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Construir rutas dentro del proyecto de esta manera: BASE_DIR / 'subdir'.
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
# Seguridad: no ejecute con depuración activada en producción!
# Se recomienda que DEBUG sea False en producción
# Se recomienda que DEBUG sea True en desarrollo
DEBUG = not IS_DEPLOYED

# Configuración de la dirección IP y el puerto donde se alojará la aplicación
HOSTING_IP_PORT = os.getenv("HOSTING_IP_PORT", '0.0.0.0:8080')

# Configuración del dominio donde se alojará la aplicación
HOSTING_DOMAIN = os.getenv("HOSTING_DOMAIN", "")

# Configuración de la URL de alojamiento de la aplicación
HOSTING_URL= os.getenv("HOSTING_URL", "")

# Configuración de los hosts permitidos
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', HOSTING_IP_PORT, HOSTING_DOMAIN]

# Configuración de los hosts de confianza para la protección contra falsificación de solicitudes entre sitios (CSRF)
CSRF_TRUSTED_ORIGINS = ['http://*', HOSTING_URL]  

# Application definition
# Definición de aplicaciones

INSTALLED_APPS = [
    'django.contrib.admin', # Administrador de Django
    'django.contrib.auth', # Autenticación
    'django.contrib.contenttypes', # Tipos de contenido
    'django.contrib.sessions', # Sesiones
    'django.contrib.messages', # Mensajes
    'django.contrib.staticfiles', # Archivos estáticos
    'django.contrib.humanize', # Humanizar números
    'whitenoise.runserver_nostatic', # Whitenoise para archivos estáticos
    'storages', # Almacenamiento en la nube
    'Personero', # Primera Aplicación del Proyecto
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Seguridad
    'django.contrib.sessions.middleware.SessionMiddleware', # Sesiones
    'django.middleware.common.CommonMiddleware', # Común (Middleware)
    'django.middleware.csrf.CsrfViewMiddleware', # Protección contra falsificación de solicitudes entre sitios (CSRF)
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Autenticación
    'django.contrib.messages.middleware.MessageMiddleware', # Mensajes
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Protección contra ataques de clics en el marco
    'whitenoise.middleware.WhiteNoiseMiddleware', # Whitenoise para archivos estáticos
]


# URL Configuration
# Configuración de URL
# https://docs.djangoproject.com/en/4.1/topics/http/urls/
ROOT_URLCONF = 'VOTO_VISION.urls'

# Template Configuration
# Configuración de plantillas
# https://docs.djangoproject.com/en/4.1/topics/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # Directorios de plantillas
        'APP_DIRS': True, # Aplicaciones de plantillas
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug', # Depuración
                'django.template.context_processors.request', # Solicitudes
                'django.contrib.auth.context_processors.auth', # Autenticación
                'django.contrib.messages.context_processors.messages', # Mensajes
            ],
        },
    },
]

# WSGI Configuration
# Configuración de WSGI
WSGI_APPLICATION = 'VOTO_VISION.wsgi.application'


# Database
# Configuración de la base de datos
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': DATABASE_DICT # Base de datos por defecto
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # Validador de similitud de atributos de usuario
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # Validador de longitud mínima de contraseña
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # Validador de contraseña común
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Validador de contraseña numérica
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-co' # Código de idioma

TIME_ZONE = 'America/Bogota' # Zona horaria
# TIME_ZONE = 'UTC'

USE_I18N = True # Usar internacionalización

USE_L10N = True # Usar localización

USE_TZ = True # Usar zona horaria


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# Archivos estáticos (CSS, JavaScript, imágenes)
# Configura la ruta de los archivos estáticos
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/staticfiles/' if IS_DEPLOYED else '/static/'

LOGIN_URL = '/signin'

"""
# Configuración para almacenar archivos estáticos en S3
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
"""

# Configuración para almacenar archivos multimedia en el sistema de archivos (S3)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if not IS_DEPLOYED:
    MEDIA_URL = '/media/'
else:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
    
# Se define el nombre de la carpeta de archivos públicos
PUBLIC_MEDIA = 'publico'
