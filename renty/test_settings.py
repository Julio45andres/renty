from .settings import *

# Sqlite settings

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }

# Codeship settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'renty_test',
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'HOST': 'localhost',
        'PORT': '5436',
    }
}

# Local settings

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'renty_test',
#         'USER': 'julio45',
#         'PASSWORD': 'renty',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
