from djoser.permissions import CurrentUserOrAdmin
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .serializers import *
from rest_framework.pagination import PageNumberPagination


# class StandardResultsSetPagination(PageNumberPagination):
#     """
#     Стандартная пагинация
#     """
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 5


class EmailMessageViewSet(viewsets.ModelViewSet):
    filter_fields = [f.name for f in EmailMessage._meta.fields if not f.__dict__.get('upload_to')]
    ordering_fields = filter_fields

    def get_permissions(self):
        """
        Возвращает права доступа
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated,)
        elif self.action == 'create':
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsAdminUser,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """
        Возвращает класс сериализатора
        """
        if self.action in ['list', 'retrieve']:
            serializer_class = EmailMessageSerializer
        else:
            serializer_class = EmailMessageCreateSerializer

        return serializer_class

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = EmailMessage.objects.all()
        else:
            queryset = EmailMessage.objects.filter(user=user).all()
            # queryset = EmailMessage.objects.all()
        return queryset




