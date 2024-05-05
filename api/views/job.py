from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import JobSerializer
from api.models import Job
from api.config.pagination import Pagination


class JobView(APIView):
    def post(self, request):
        res = {
            'code': 400,
            'msg': ' success',
            'data': [],
            'total': 5
        }
        page = request.data.get('page')
        limit = request.data.get('limit')
        job_category_id_list = request.data.get('job_category_id_list')
        location_code_list = request.data.get('location_code_list')
        job_objects = Job.objects
        total = job_objects.count()
        if not job_category_id_list and not location_code_list:
            job_query = job_objects
        elif not job_category_id_list:
            job_query = job_objects.filter(city__code__in=location_code_list)
        elif not location_code_list:
            job_query = job_objects.filter(category__nid__in=job_category_id_list)
        else:
            job_query = job_objects.filter(category__nid__in=job_category_id_list, city__code__in=location_code_list)

        pager = Pagination(
            limit=int(limit),
            all_count=int(total),
            current_page=int(page)
        )

        job_list = job_query.all()[pager.start: pager.end]
        serializer = JobSerializer(instance=job_list, many=True)

        res['total'] = total
        res['data'] = serializer.data
        res['code'] = 200

        return Response(res)



