from django.http import JsonResponse
from webScraping.models import TbImoveis
import asyncio
from webScraping.scraper import coletar_dados

async def iniciar_scraping(request):
    """Executa o scraping em segundo plano e permite que Streamlit consulte os resultados depois."""
    
    asyncio.create_task(asyncio.to_thread(coletar_dados))  # Executa em segundo plano
    return JsonResponse({"mensagem": "Web scraping sendo executado em segundo plano!"})


def obter_dados(request):
    """Consulta os dados salvos no banco e retorna para Streamlit."""
    
    imoveis = TbImoveis.objects.all().values()  # Obtém os dados salvos
    return JsonResponse({"dados": list(imoveis)})