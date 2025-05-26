from django.shortcuts import get_object_or_404
from administracao.models import TbAlunos, TbCarros, TbEnderecos
from administracao.schemas import TbAlunosSchemaIn


def atualizar_alunos_por_id(id: int, data: TbAlunosSchemaIn):
    aluno = get_object_or_404(TbAlunos, id=id)
    aluno.nome_aluno = data.nome_aluno
    aluno.email = data.email
    if data.cep:
        endereco = TbEnderecos.objects.get(pk=data.cep)
        aluno.cep = endereco
    else:
        aluno.cep = None
    if data.carro:
        carro = TbCarros.objects.get(pk=data.carro)
        aluno.carro = carro
    else:
        aluno.carro = None
    aluno.save()
    return aluno