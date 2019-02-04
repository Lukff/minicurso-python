import json

def registra_aluno(nome, ano_entrada, ano_nascimento, **misc):
    """Cria a entrada do registro de um aluno."""
    registro = {'nome': nome,
                'ano_entrada': ano_entrada,
                'ano_nascimento': ano_nascimento}

    for key in misc:
        registro[key] = misc[key]

    return registro

def escreve_registro(registro, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(registro, f)


registros = {
    'alunos': []
}

def adicionar_registro(nome, ano_entrada, ano_nascimento, registros, **misc):
    registros['alunos'].append(registra_aluno(nome,
                                              ano_entrada, ano_nascimento,
                                              **misc))




