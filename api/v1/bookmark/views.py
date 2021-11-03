from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from .models import Bookmark
from .permissions import IsPublic
from .serializers import BookmarkSerializer


class BookmarksView(mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated | IsPublic]
    queryset = Bookmark.objects.all()

    def get_queryset(self):
        """ filter bookmarks results to get for authenticated users and guests """
        if self.request.user.is_authenticated:
            return self.queryset.filter(user=self.request.user.id)
        else:
            return self.queryset.filter(is_public=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
