import json
from datetime import datetime


class JSONDateTimeSerializer:  # I used this to put a datetime in Session, to keep track of visitors on a range of dates
    @staticmethod
    def _default(ob):
        if isinstance(ob, datetime):
            return {'__datetime__': ob.isoformat()}
        raise TypeError(type(ob))

    @staticmethod
    def _object_hook(d):
        if '__datetime__' in d:
            return datetime.fromisoformat(d['__datetime__'])
        return d

    def dumps(self, obj):
        return json.dumps(obj, separators=(',', ':'), default=self._default)

    def loads(self, data):
        return json.loads(data, object_hook=self._object_hook)

