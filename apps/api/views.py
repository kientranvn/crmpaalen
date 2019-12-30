from django.http import JsonResponse

from django.shortcuts import render


# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post


class TestView(APIView):
    def get(self, request, *agrs, **kwargs):
        qs = Post.objects.all()
        #serializers = PostSerializer(qs, many=True)
        post = qs.first()
        serializers = PostSerializer(post)
        return Response(serializers.data )

    def post(self, request, *args, **kwargs):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)





#def test_view(request):
#    data = {
#        'name': 'Kien',
#        'age': 25
#    }    
#    return JsonResponse(data)
