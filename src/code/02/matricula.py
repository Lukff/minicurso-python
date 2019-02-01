def registra_aluno(nome, ano_entrada, ano_nascimento, **misc):
    """Cria a entrada do registro de um aluno."""
    registro = {'nome': nome,
                'ano_entrada': ano_entrada,
                'ano_nascimento': ano_nascimento}

    for key in misc:
        registro[key] = misc[key]

    return registro

