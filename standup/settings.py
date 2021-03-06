# Application settings.
# To override the values, create a local_settings.py and enter the
# new values there.

DEBUG = False

# The key used to authenticate API calls.
API_KEY = 'qwertyuiopasdfghjklzxcvbnm1234567890'

SITE_URL = 'http://localhost:5000'
SESSION_SECRET = 'asdfghjklqwertyuiopzxcvbnm1234567890'

try:
    from local_settings import *
except ImportError:
    pass
