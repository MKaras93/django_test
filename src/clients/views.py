import csv
from datetime import datetime

from django.http import HttpResponse
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientCreateAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientGenerateCSV(APIView):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        current_date = datetime.utcnow()
        response["Content-Disposition"] = f"attachement; filename=clients-{current_date}.csv"

        writer = csv.writer(response)

        for client in Client.objects.all():
            writer.writerow([str(client.id), client.name])

        return response
