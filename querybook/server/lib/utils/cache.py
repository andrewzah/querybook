import hashlib
from urllib.parse import quote


TEMPLATE_FRAGMENT_KEY_TEMPLATE = "template.cache.%s.%s"

# this is from django/django/core/cache/utils.py


def make_template_fragment_key(fragment_name, vary_on=None):
    if vary_on is None:
        vary_on = ()
    key = ":".join(quote(str(var)) for var in vary_on)
    args = hashlib.sha256(key.encode())
    return TEMPLATE_FRAGMENT_KEY_TEMPLATE % (fragment_name, args.hexdigest())
