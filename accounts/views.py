from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from accounts.models import CustomUser
from accounts.serializer import UserTopMoneySerializer


class ItemSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class UserTopMoney(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserTopMoneySerializer
    pagination_class = ItemSetPagination
    queryset = CustomUser.objects.filter().order_by('-money')
