
import asyncio
from django.http import JsonResponse
from .scraper import coletar_dados

async def iniciar_scraping(request):
    dados_coletados = await coletar_dados()  # Executa a função assíncrona
    return JsonResponse({"mensagem": "Web scraping concluído!", "dados": dados_coletados})
