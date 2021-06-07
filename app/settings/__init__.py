from os import environ

from .base import *

CURRENT_ENV = environ.get('CURRENT_ENV')
if CURRENT_ENV in ('dev', 'development'):
    from .dev import *
elif CURRENT_ENV in ('prod', 'production'):
    from .prod import *
