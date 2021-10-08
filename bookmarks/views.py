from .models import Bookmark
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BookmarkSerializer

# Create your views here.

class BookmarkViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Bookmark.objects.all()
    # The serializer class for serializing output
    serializer_class = BookmarkSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
