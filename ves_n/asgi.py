"""
ASGI config for ves_n project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import time

from django.core.asgi import get_asgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ves_n.settings')
#
# application = get_asgi_application()


import os
import django
import multiprocessing as ml

import threading as thread
# import uvicorn
from channels.routing import get_default_application
def pr():
    i = 0
    while 1:
        pass
        print(i, ' -----------------------------------------------------------------------------------')
        time.sleep(5)
        i = i+1

# pr = thread.Thread(target=pr, daemon=True)
# pr.start()

pr = ml.Process(target=pr, daemon=True)
# if not pr.is_alive():
#     print('start process========================================================================')
pr.start()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ves_n.settings")
django.setup()
application = get_default_application()
