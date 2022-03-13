from datetime import datetime
from adminInterface.json_datetime_serializer import JSONDateTimeSerializer


class CreateSession:

    def session(self, request):
        if not request.session.has_key('creation_date'):
            date = JSONDateTimeSerializer.dumps(JSONDateTimeSerializer, datetime.now())
            request.session['creation_date'] = date

