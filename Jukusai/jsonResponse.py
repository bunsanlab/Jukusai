from django.http import HttpResponse
import json

class JSONResponse(HttpResponse):
    def __init__(self, data, token, **kwargs):
        if 'paginate' not in data:
            content = json.dumps({'data': data}, ensure_ascii=False, indent=2)
        else:
            response = {x[0]: x[1] for x in data.items()}
            content =json.dumps(response, ensure_ascii=False, indent=2)
        super(JSONResponse, self).__init__(content = content)
        super(JSONResponse, self).__setitem__('Content-Type', 'application/json; charset=utf-8')

