from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, GenericAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework import mixins, viewsets

data = {
    "id": 1,
    "title": "hi"
}

"""
# @api_view(["GET", "POST", "DELETE"])
# @permission_classes([IsAuthenticated])
# def postlist(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
"""

'''
class PostList(APIView):
    """getting a list of post and creating new posts"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''


class PostList(ListCreateAPIView):
    """getting a list of post and creating new posts"""

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


'''
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    # queryset = self.get_queryset()
    # serializer = self.serializer_class(queryset, many=True)
    # return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     return self.create(self, request, *args, **kwargs)
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
'''


@api_view(["GET", "PUT", "DELETE"])
def postDetail(request, id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=404)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail": "Item deleted successfully"}, status=204)



"""
class PostDetail(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        post = Post.objects.filter(pk=id, status=True)

        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(selfself, request, id):
        post = Post.objects.filter(pk=id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
"""


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    # lookup_field = "id" if we dont want to change the url to pk from id we can do this


'''
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

    # def get(self, request, id):
    #     post = Post.objects.filter(pk=id, status=True)
    #
    #     serializer = self.serializer_class(post)
    #     return Response(serializer.data)
'''


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


'''
    # @action(methods=["get"], detail=False)
    # def get_ok(self, request):
    #     return Response({'detail': 'ok'})

    # def list(self, request):
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     post_object = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.serializer_class(post_object)
    #     return Response(serializer.data)
    #
    # def create(self, request):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
    #     pass
'''


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
