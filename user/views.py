# Create your views here.

from rest_framework.settings import api_settings
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from . import serializers, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from . import models
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, listng,deleting and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

    # perform_create is a function that we can add to our viewset to
    # customize the logic that's run when we create a  new object through our viewset
    # when django restframework creates new object in our viewset we want to
    # customize this to make sure that the user profile of the profileFeedItem
    # thats created is set to the currently logged in user .we do that by creating a
    # perform_create Function within our viewset
