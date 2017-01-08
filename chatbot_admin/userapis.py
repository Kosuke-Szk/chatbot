from rest_framework import viewsets, routers
from chatbot_admin.models import User
from chatbot_admin.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'useruser', UserViewSet)