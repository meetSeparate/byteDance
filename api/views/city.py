from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import City
from api.serializers import CitySerializer


class CityView(APIView):
    def get(self, request):
        res = {
            'code': 400,
            'msg': 'success',
            'data': []
        }

        city_list = City.objects.all()
        serializer = CitySerializer(instance=city_list, many=True)

        res['data'] = serializer.data
        res['code'] = 200
        return Response(res)