from Funcoes.Funcoes_Dicionario import *

usuarios={}
usuarios={"Chaves":["Chaves Silva","17/06/1975","Recep_01"],"Quico":["Enrico Flores","03/06/1976","Raiox_02"]}
usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]


opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    if opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()

#Maneiras 1
   # chave = input("Digite o login: ").upper()
   # nome = input("Digite o nome: ").upper()
   # data = input("Digite a última data de acesso: ")
   # estacao = input("Qual a última estação acessada: ").upper()
   # usuarios[chave] = [nome, data, estacao]

    # Maneiras 2
    #chave = input("Digite o login: ").upper()
    #usuarios[chave] = [input("Digite o nome: ").upper(),
     #                  input("Digite a última data de acesso: "),
     #                  input("Qual a última estação acessada: ").upper()]

    # Maneiras 3
    #usuarios[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
    #                                              input("Digite a última data de acesso: "),
    #                                              input("Qual a última estação acessada: ").upper()]
print(usuarios.keys())
print(usuarios.popitem())




