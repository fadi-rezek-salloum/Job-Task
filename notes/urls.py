from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.ListNotesApiView.as_view(), name='notes-list'),
    path('create/', views.CreateNoteApiView.as_view(), name='notes-create'),
    path('delete/<pk>/', views.DeleteNoteApiView.as_view(), name='notes-delete'),
    path('details/<pk>/', views.RetrieveNotesApiView.as_view(), name='notes-details'),
]
