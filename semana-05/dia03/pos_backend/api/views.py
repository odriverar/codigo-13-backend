from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(APIView):
      
      def get(self, request):
            context ={
                  'ok': True,
                  'message':'¡El servidor está activo!'
            }
            return Response(context)