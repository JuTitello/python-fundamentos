from funcoes import(
    cadastrar_cliente,
    listar_cliente,
    buscar_cliente,
    excluir_cliente
)

clientes = []

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Excluir cliente")
    print("5 - Sair")

    opcao = input("Digite o Nº da opção: ")

    if opcao == "1":
        cadastrar_cliente(clientes)

    elif opcao == "2":
        listar_cliente(clientes)

    elif opcao == "3":
        buscar_cliente(clientes)

    elif opcao == "4":
        excluir_cliente(clientes)

    elif opcao == "5":
        print("Encerrando...")
        break

    else:
        print("❌ Opção inválida!") 