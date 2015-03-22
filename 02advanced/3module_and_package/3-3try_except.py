try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


print '--do Task--'
try:
    import json
except ImportError:
    import simplejson as json
print json.dumps({'python':2.7})
