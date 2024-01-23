from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import JobSerializer
from api.models import Job


class JobDetailView(APIView):
    def get(self, request, nid):
        res = {
            'code': 400,
            'msg': 'success',
            'data': {}
        }

        job_obj = Job.objects.filter(nid=nid).first()

        serializer = JobSerializer(instance=job_obj, many=False)

        res['data'] = serializer.data
        res['code'] = 200

        return Response(res)
