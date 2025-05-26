from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from administracao.apis import router as administracaoRouter


api = NinjaAPI(
    title="Api da Ludmila",
    version="1.0.0",
    description="Apis para serem usadas no frontend de escolas"
)
api.add_router("/administracao/",administracaoRouter )



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]