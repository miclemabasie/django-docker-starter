import logging
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .exceptions import NotYourProfileException, ProfileNotFoundException
from apps.users.models import Profile, User
from .renderers import ProfileJSONRenderer
from .serializers import (
    ProfileSerializer,
    UpdateProfileSerializer,
    UnifiedProfileSerializer,
)

logger = logging.getLogger(__name__)


class GetProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user_profile = self.request.user.profile
        serializer = ProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]
    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFoundException("Profile does not exist")

        user_name = request.user.username
        if user_name != username:
            raise ProfileNotFoundException("Not your profile to update")

        serializer = self.serializer_class(
            instance=request.user.profile, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "PATCH"])
@permission_classes([permissions.IsAuthenticated])
def profile_update(request):
    """
    Handle profile updates for authenticated users
    GET: Return current user's profile data
    PUT/PATCH: Update user and profile information
    """
    user = request.user

    if request.method in ["PUT", "PATCH"]:
        serializer = UnifiedProfileSerializer(
            user, data=request.data, partial=request.method == "PATCH"
        )

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Explicit update handling for better visibility
        validated_data = serializer.validated_data
        print("this is the validated data", validated_data)

        # Update User model fields
        user.first_name = validated_data.get("first_name", user.first_name)
        user.last_name = validated_data.get("last_name", user.last_name)
        user.save()

        # Update Profile model fields
        profile = user.profile
        profile.phone_number = validated_data.get("phone_number", profile.phone_number)
        profile.bio = validated_data["profile"].get("bio", profile.bio)
        profile.gender = validated_data["profile"].get("gender", profile.gender)
        profile.country = validated_data["profile"].get("country", profile.country)
        profile.city = validated_data["profile"].get("city", profile.city)
        profile.address = validated_data["profile"].get("address", profile.address)

        # Handle profile photo upload
        if "profile_photo" in validated_data["profile"]:
            print(
                "this is the profile photo", validated_data["profile"]["profile_photo"]
            )
            profile.profile_photo = validated_data["profile"]["profile_photo"]

        profile.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle GET request
    serializer = UnifiedProfileSerializer(user)
    return Response(serializer.data)
