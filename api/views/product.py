from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Product
from api.serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request):
        res = {
            'code': 400,
            'msg': 'success',
            'data': []
        }

        product_query = Product.objects.all()
        serializers = ProductSerializer(instance=product_query, many=True)

        res['code'] = 200
        res['data'] = serializers.data
        return Response(res)
