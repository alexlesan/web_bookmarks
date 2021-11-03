from django.urls import path
from .views import BookmarksView

urlpatterns = [
    path('', BookmarksView.as_view(), name="bookmarks")
]