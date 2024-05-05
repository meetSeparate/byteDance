from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import ResumeFile
from api.config.resume_parse import parser


class ParseView(APIView):
    def post(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': {}
        }
        uid = 2405040
        pwd = 'AC0qWdY2wusJ'
        url = 'https://www.resumesdk.com/api/parse'
        file = request.FILES.get('file')
        userid = request.headers.get('userid')
        resume = ResumeFile.objects.create(file=file, user_id=userid)
        path = str(resume.file.url)[1:]
        result = parser(url, path, uid, pwd)
        res['data'] = result
        return Response(res)
