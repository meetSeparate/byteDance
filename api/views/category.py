from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Category
from api.serializers import CategorySerializer


class CategoryView(APIView):
    def get(self, request):
        res = {
            'code': 400,
            'msg': 'success',
            'data': []
        }

        category_list = Category.objects.all()

        serializer = CategorySerializer(instance=category_list, many=True)

        res['data'] = serializer.data
        res['code'] = 200
        return Response(res)
