import os
import sys

activate_this = os.path.expanduser('/home/c/cz18090/venv/bin/activate_this.py')
exec(open(activate_this).read(), {'__file__': activate_this})

sys.path.insert(1, os.path.expanduser('/home/c/cz18090/grace/public_html'))

__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grace.settings')

application = get_wsgi_application()
