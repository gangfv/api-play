from django.urls import path, include

from accounts.views import UserTopMoney

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('top/', UserTopMoney.as_view())
]
