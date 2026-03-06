from rest_framework import generics
from .serializers import ToDoSerializer
from todo.models import ToDo

class ToDoList(generics.ListAPIView):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user).order_by('-created')
