from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from notes.serializers import NoteSerializer
from notes.models import Note
from notes.permissions import IsOwner

class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    # Override default `list` implementation to add filter error handling
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        from_date = self.request.query_params.get('from_date')
        till_date = self.request.query_params.get('till_date')

        if from_date is not None and till_date is not None:
            try:
                queryset = queryset.filter(updated_at__range=(from_date, till_date))
            except ValidationError as exception:
                return Response(data=str(exception),
                                status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    # Only allow accessing own notes
    def get_queryset(self):
        return self.request.user.note_set.all()

    # When saving a model, use the authenticated user for setting the user_id instead of the request payload's user_id
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def stats(self, request):
        return Response({
            'personal_note_count': Note.objects.filter(user=self.request.user).count(),
            'total_note_count': Note.objects.count(),
            'total_user_count': User.objects.count()
        })
