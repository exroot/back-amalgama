import json
from rest_framework.renderers import JSONRenderer

class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, media_type=None, renderer_context=None):
        response = ''
        if renderer_context['response'].status_code >= 400:
            response = json.dumps({'errors': data})
        else:
            request_context = renderer_context['request']
            if request_context.GET.get('show_meta', None) is not None:
                response = json.dumps(data['results'])
            else:
                
                response = json.dumps({'data': data, 'status': renderer_context['response'].status_code, 'message': 'ok' })
        return response