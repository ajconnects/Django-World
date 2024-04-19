from rest_framework import generics
from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer

# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.prefetch_related("tags").all() #read about prefetch_related is use for (many to many relations in the model as inner join on two table)
    serializer_class = PostSerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class Post_R_U_D_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.prefetch_related("tags").all()
    serializer_class = PostSerializer
    lookup_field = "pk"

class Tag_R_U_D_View(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "pk"