from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, min_length=6)

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        # la password no la vamos a poder ver
        extra_kwargs = {'password': {'write_only': False}}


    def create(self, validate_data):
        return get_user_model().objects.create_user(**validate_data)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError('El usuario no existe', code='authorization')

        data['user'] = user
        return data