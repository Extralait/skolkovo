from rest_framework import serializers

from api.models import User, EmailMessage
from api.services.predict import predict


class UserSerializer(serializers.ModelSerializer):
    # ProcessingFile

    class Meta:
        model = User
        exclude = ['password','is_staff','is_superuser','is_active']
        read_only = ['email']


class EmailMessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailMessage
        fields = '__all__'
        read_only_fields = ['status','accuracy','user']

    def _user(self):
        """
        Получение текущего пользователя
        """
        return self.context['request'].user

    def create(self, validated_data):
        """
        Создать файл
        """
        email_message = (EmailMessage.objects.create(
            user=self._user(),
            **validated_data
        ))

        status, accuracy = predict(
            email_message.from_email,
            email_message.to_email,
            email_message.date,
            email_message.content_type,
            email_message.x_uid,
            email_message.body,
        )
        email_message.status = 'malevolent' if status else 'safe'
        email_message.accuracy = accuracy
        email_message.save()
        return email_message


class EmailMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailMessage
        fields = '__all__'

