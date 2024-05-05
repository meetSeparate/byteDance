from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Delivery, Job


class DeliveryView(APIView):
    def post(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': {}
        }
        user_id = request.data.get('userId')
        job_id = request.data.get('jobId')
        delivery = Delivery.objects.filter(user_id=user_id, job_id=job_id).first()
        if delivery:
            res['msg'] = '您已投递该岗位，请勿重复投递～'
            res['code'] = 400
            return Response(res)
        Delivery.objects.create(user_id=user_id, job_id=job_id)
        return Response(res)

    def get(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': []
        }
        user_id = request.GET.get('userId')
        delivery_list = Delivery.objects.filter(user_id=user_id).all()
        for delivery in delivery_list:
            job = Job.objects.filter(nid=delivery.job_id).first()
            res['data'].append({
                'id': delivery.id,
                'job_id': job.nid,
                'title': job.title,
                'city': job.city.name,
                'category': job.category.name,
                'recruit_type': job.recruit_type.type,
                'status': delivery.status,
                'create_date': str(delivery.create_date)[:16]
            })
        return Response(res)