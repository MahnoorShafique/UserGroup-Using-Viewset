from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile  # this tells this  meta class is pointing to this model
        fields = ('id', 'email', 'name', 'password')  # what fields in model we want to use in serializer
        extra_kwargs = {'password': {'write_only': True}}  # password is made write only so you won't be able to see
        # it through serializer
        # you will only be able to write it from the serializer
        # we donot want to store text password user entered in the database we encrypt it to hash for security purposes

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
        # we set this (extra_kwargs) automatically baseds on user that
        # is currently loggin.we don't want users  tobe
        # able to create user profiles or profile feed
        # items for other users in the system .We only
        # want to create a profile feed item for currently loggedin user
