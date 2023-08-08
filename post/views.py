from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

## import models
from core.models import Post
from post import serializers


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer

    # represents objects that are available for this viewset.
    # queryset objects that are manageable by this view.
    queryset = Post.objects.all()

    # In order to use endpoint provided by this viewset, we will need ]
    # authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return self.queryset.filter(user=self.request.user).order_by("-id")

    def get_serializer_class(self):
        """Returns the serializer class to be used for the request"""

        if self.action == "list":
            return serializers.PostSerializer
        return self.serializer_class

    def perform_create(self, serializer):


        serializer.save(user=self.request.user)
