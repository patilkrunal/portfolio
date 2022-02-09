import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG", "False") == 'True'

try:
    if DEBUG:
        from .local import *
    else:
        from .production import *
except ImportError:
    pass
