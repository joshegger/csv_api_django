from csvapp.models import Log
import datetime

class AccessLogs(object):

    # One-time config
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Add the page info and timestamp into DB
        try:
            Log(pageURL=request.path, timestamp=datetime.now(tz=None)).save()
        except Exception as e:
            print(e)

        return response