
#cadastro dos projetos
dic = {}
qntd = int(input("Insira a qunatidade de projetos que serão adicionados: "))
for i in range(qntd):
    nome_proj = input(f"Insira o nome do {i + 1} projeto: ")
    responsavel_proj = input(f"Insira o nome do {i + 1} responsavel: ")
    qntd_horas = int(input(f"Insira a quantidade de horas do {i + 1} projeto: "))
    status_proj = input(f"Insira o status do {i + 1} projeto: ")
    dic[nome_proj] = {
        "Responsavel" : responsavel_proj,
        "Horas" : qntd_horas,
        "Status" : status_proj
    }
#menu abaixo
resp_usu = input("1 - Listar todos os projetos \n2 - Buscar projetos por responsavel \n3 - Exibir Somente projetos ativos \n4 - Calcular total de horas estimadas \n5 - Alterar status de um projeto \n6 - Sair \nEscolha uma opção: ")
while resp_usu != '6':
    if resp_usu == '1':
     print(f"Todos os projetos são: {list(dic.keys())}")
    if resp_usu == '2':
        busca = input("Insira o nome do responsavel: ")
        projetos_responsavel = []
        for nome, dicmenor in dic.items():
            if dicmenor['Responsavel'] == busca:
                projetos_responsavel.append(nome)
        if projetos_responsavel:
            print(f"Os projetos que {busca} está encarregado são esses: {','.join(projetos_responsavel)}")      
        else:
            print(f"Esse responsavel não pariticipa de nenhum projeto!")      
    if resp_usu == '3':
        projetos_ativos = []
        for nome, dicmenor in dic.items():
         if dicmenor['Status'] == 'Ativo' or dicmenor['Status'] == 'ativo':
            projetos_ativos.append(nome)
        if projetos_ativos:
         print(f"Os Projetos que estão ativos são esses: {','.join(projetos_ativos)}")
        else:
            print("Nenhum projeto ativo no momento!")
    if resp_usu == '4':
        horas_total = 0
        for dicmenor in dic.values():
         horas_total+=dicmenor['Horas']
        print(f"Todos os projetos tem {horas_total} horas!")    
    if resp_usu == '5':
        busca = input('Insira o nome do proejeto para ser alterado: ')
        if busca in dic:
            alterar_status = input("Insira o novo status do projeto: ")
            dic[busca]['Status'] = alterar_status
            print(f"O status do {busca} foi alterado para {alterar_status}")
        else:
         print("Projeto não encontrado!")
    resp_usu = input("1 - Listar todos os projetos \n2 - Buscar projetos por responsavel \n3 - Exibir Somente projetos ativos \n4 - Calcular total de horas estimadas \n5 - Alterar status de um projeto \n6 - Sair \nEscolha uma opção: ")
print("Programa encerrando...")    

