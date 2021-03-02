'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''
import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cambauba.settings')

application = Cling(get_wsgi_application())
