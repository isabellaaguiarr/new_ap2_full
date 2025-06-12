from django.db import models

class TbImoveis(models.Model):
    localizacao = models.CharField(max_length=255, blank=True, null=True)
    metragem = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quartos = models.IntegerField(blank=True, null=True)
    decricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_dados_imobiliarios'
