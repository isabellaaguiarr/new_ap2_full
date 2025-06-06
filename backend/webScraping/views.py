
import asyncio
from django.http import JsonResponse
from .scraper import coletar_dados

async def iniciar_scraping(request):
    dados_coletados = await coletar_dados()  
    return JsonResponse({"mensagem": "Web scraping concluído!", "dados": dados_coletados})
