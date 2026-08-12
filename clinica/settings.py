from pathlib import Path

# =========================================
# BASE DIR
# =========================================

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================
# SECURITY
# =========================================

SECRET_KEY = 'django-insecure-am-systems'

DEBUG = True

ALLOWED_HOSTS = []

# =========================================
# APPS
# =========================================

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # HUMANIZE
    'django.contrib.humanize',

    # APPS DO SISTEMA
    'accounts.apps.AccountsConfig',
    'agenda',
    'ckeditor',

]

# =========================================
# MIDDLEWARE
# =========================================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

# =========================================
# URLS
# =========================================

ROOT_URLCONF = 'clinica.urls'

# =========================================
# TEMPLATES
# =========================================

TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]

# =========================================
# WSGI
# =========================================

WSGI_APPLICATION = 'clinica.wsgi.application'

# =========================================
# DATABASE
# =========================================

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }

}

# =========================================
# PASSWORD VALIDATION
# =========================================

AUTH_PASSWORD_VALIDATORS = []

# =========================================
# INTERNACIONALIZAÇÃO
# =========================================

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Formatação brasileira

USE_THOUSAND_SEPARATOR = True

THOUSAND_SEPARATOR = '.'

DECIMAL_SEPARATOR = ','

NUMBER_GROUPING = 3

# =========================================
# STATIC FILES
# =========================================

STATIC_URL = '/static/'

STATICFILES_DIRS = [

    BASE_DIR / 'static',

]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# =========================================
# DEFAULT AUTO FIELD
# =========================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'