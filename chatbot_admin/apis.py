from rest_framework import viewsets, routers
from chatbot_admin.models import Account
from chatbot_admin.serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)