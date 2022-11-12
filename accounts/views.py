from rest_framework.generics import CreateAPIView, GenericAPIView

from .serializers import AccountSerializer


class RegisterApiView(CreateAPIView):
    serializer_class = AccountSerializer
