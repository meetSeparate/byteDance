from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def post(self, request):
        res = {

        }

        print(request.data)

        return Response(res)