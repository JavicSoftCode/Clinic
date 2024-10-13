import os
from pathlib import Path

from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para proporcionar criptografía y mantener la seguridad del proyecto
SECRET_KEY = os.getenv('SECRET_KEY', '')

# Modo de depuración para el desarrollo. En producción debe ser False
DEBUG = os.getenv('DEBUG', '') == 'True'

# Lista de hosts permitidos para prevenir ataques de falsificación de solicitudes entre sitios (CSRF)
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Configuración del campo automático por defecto para las claves primarias
DEFAULT_AUTO_FIELD = os.getenv('DEFAULT_AUTO_FIELD', 'django.db.models.BigAutoField')

# Aplicaciones instaladas
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  # My Apps
  'BackEnd.Apps.Auth.apps.AuthConfig',
  'BackEnd.Apps.Core.apps.CoreConfig',
  'BackEnd.Apps.Doctors.apps.DoctorsConfig',
  'BackEnd.Apps.Recipes.apps.RecipesConfig',

  # App Terceros
  # 'widget_tweaks',
]

# Middleware de seguridad
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',

  # My Middleware
  'BackEnd.Apps.Auth.Middleware.middleware.NoCacheMiddleware',

  # Middleware de terceros
  'crum.CurrentRequestUserMiddleware',
]

# Configuración de URLs
ROOT_URLCONF = 'Clinic.urls'

# Configuración de plantillas
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    # 'DIRS': [os.path.join(BASE_DIR, os.getenv('DIRS_TEMPLATES'))],
    'DIRS': [os.path.join(BASE_DIR, 'FrontEnd/templates')],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]

# Aplicación WSGI para servir el proyecto; este es el punto de entrada para servidores web compatibles con WSGI
WSGI_APPLICATION = 'Clinic.wsgi.application'

# Configuración de la base de datos, conector de la DB <<< pip install psycopg2-binary >>> POSTGRESQL
DATABASES = {
  'default': {
    'ENGINE': os.getenv('DB_ENGINE', ''),
    'NAME': os.getenv('DB_NAME_DATABASE', ''),
    'USER': os.getenv('DB_USERNAME_DATABASE', ''),
    'PASSWORD': os.getenv('DB_PASSWORD_DATABASE', ''),
    'HOST': os.getenv('DB_HOST_DATABASE', ''),
    'PORT': os.getenv('DB_PORT_DATABASE', '5432'),
  }
}

# Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    'OPTIONS': {'min_length': 8, }  # Asegura que la contraseña tenga mayor a 8 caracteres
  },
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
  },
]

# Formatos de entrada de fecha
DATE_INPUT_FORMATS = [
  '%Y-%m-%d',  # Formato Año-Mes-Día
  '%Y/%m/%d',  # Formato Día/Mes/Año
  '%d/%m/%Y',  # Formato Día/Mes/Año
  '%d-%m-%Y',  # Formato Día-Mes-Año
]

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = os.getenv('STATIC_URL', '')
STATICFILES_DIRS = [os.path.join(BASE_DIR, os.getenv('STATICFILES_DIRS', ''))]

# Configuración de archivos multimedia
MEDIA_URL = os.getenv('MEDIA_URL', '')
MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv('MEDIA_ROOT', ''))

# Modelo de usuario personalizado
AUTH_USER_MODEL = os.getenv('AUTH_USER_MODEL', '')

# Configuración de URLs de autenticación
LOGIN_URL = os.getenv('LOGIN_URL', '')  # URL para el inicio de sesión
LOGOUT_URL = os.getenv('LOGOUT_URL', '')  # URL para el cierre de sesión
LOGIN_REDIRECT_URL = os.getenv('LOGIN_REDIRECT_URL', '')  # Redirigir después del inicio de sesión
SIGNUP_REDIRECT_URL = os.getenv('SIGNUP_REDIRECT_URL', '')  # Redirigir después del registro

# Configuración de seguridad
SECURE_BROWSER_XSS_FILTER = os.getenv('SECURE_BROWSER_XSS_FILTER', '') == 'True'  # Habilitar filtro XSS en el navegador
SECURE_CONTENT_TYPE_NOSNIFF = os.getenv('SECURE_CONTENT_TYPE_NOSNIFF',
                                        '') == 'True'  # Prevenir sniffing de tipo de contenido
SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT',
                                'False').lower() == 'true'  # Redirigir todas las conexiones a HTTPS
SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE',
                                  '') == 'True'  # Hacer que las cookies de sesión sean seguras (solo HTTPS)
SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'False').lower() == 'true'
# CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE', '') == 'True'  # Proteger la cookie CSRF para que sea solo HTTPS
SECURE_HSTS_SECONDS = int(os.getenv('SECURE_HSTS_SECONDS', 7200))  # Configurar el tiempo en segundos para HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.getenv('SECURE_HSTS_INCLUDE_SUBDOMAINS',
                                           '') == 'True'  # Habilitar HSTS para subdominios
SECURE_HSTS_PRELOAD = os.getenv('SECURE_HSTS_PRELOAD',
                                '') == 'True'  # Permitir el pre-carga de HSTS en navegadores compatibles

# Configuración de la sesión en Django
SESSION_ENGINE = os.getenv('SESSION_ENGINE', '')  # Usar base de datos para sesiones
SESSION_COOKIE_AGE = int(os.getenv('SESSION_COOKIE_AGE', 7200))  # Tiempo de vida de la cookie de sesión (2 horas)
SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME', '')  # Nombre de la cookie de sesión
SESSION_COOKIE_HTTPONLY = os.getenv('SESSION_COOKIE_HTTPONLY',
                                    '') == 'True'  # Evitar acceso a la cookie desde JavaScript
SESSION_SAVE_EVERY_REQUEST = os.getenv('SESSION_SAVE_EVERY_REQUEST',
                                       '') == 'True'  # Guardar la sesión en cada solicitud
SESSION_EXPIRE_AT_BROWSER_CLOSE = os.getenv('SESSION_EXPIRE_AT_BROWSER_CLOSE',
                                            '') == 'True'  # Expirar la sesión al cerrar el navegador

BROWSER_REFRESH_SECONDS = 1
