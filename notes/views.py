from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView

from .models import Note
from .serializers import NotesSerializer


class ListNotesApiView(ListAPIView):
    queryset = Note.objects.all().order_by('-created')
    serializer_class = NotesSerializer
    

class CreateNoteApiView(CreateAPIView):
    serializer_class = NotesSerializer


class DeleteNoteApiView(DestroyAPIView):
    queryset = Note.objects.all()


class RetrieveNotesApiView(RetrieveAPIView):        
    queryset = Note.objects.all()
    serializer_class = NotesSerializer