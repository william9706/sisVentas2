from django.urls import path, include
from sisVentas.articulo.views import vista_index

urlpatterns = [
    path("", view=vista_index, name="index")
]
