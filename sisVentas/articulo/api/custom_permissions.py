from django.conf import settings
from rest_framework.permissions import BasePermission


class ClienteRequestPermission(BasePermission):
    """
    permiso para validar que el request viene de la app cliente
    """

    def get_server_client_token(self):
        """
        pequeño método para permitir sobreescribir el server_client_token
        en caso de ser necesario
        """
        return settings.LA_CONSOLA_VUE_APP_TOKEN

    def has_permission(self, request, view):
        server_client_token = self.get_server_client_token()
        client_token = request.headers.get("Client-Token", "")
        return server_client_token and server_client_token == client_token
