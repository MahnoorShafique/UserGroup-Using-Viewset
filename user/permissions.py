from rest_framework import permissions


# permission file checks that only single  user can update his profile  not all users can update a profile.
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""
        # if user just want to view the profile let him view
        # safe method is non destructive ,means it alllows you to retrieve data but wont let you change modift
        # update or delete any object indatabase it is like http get.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update thier own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update thier own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
