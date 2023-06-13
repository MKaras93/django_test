from django.urls import path

from clients.views import ClientCreateAPIView, ClientListAPIView, ClientGenerateCSV

urlpatterns = (
    path("clients/", ClientListAPIView.as_view()),
    path("clients/create", ClientCreateAPIView.as_view()),
    path("clients/csv", ClientGenerateCSV.as_view()),
)
