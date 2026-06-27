def cadastrar_cliente(clientes):
    while True:
        print("=== CADASTRANDO CLIENTE ===")

        nome = input("\nDigite o nome do cliente: ").strip().title()
        
        if nome in clientes:
            print(f"❌ O cliente '{nome}' já está cadastrado.\n")
        else: 
            clientes.append(nome)
            print(f"✅ Cliente {nome} registrado com sucesso!")
            break

def listar_cliente(clientes):
    print("=== CLIENTES CADASTRADOS ===")

    if not clientes:
        print("\n❌Nenhum cliente cadastrado.")
        return

    for indice, cliente in enumerate(clientes, start=1):
        print(f"{indice}. {cliente}")


def buscar_cliente(clientes):
    print("\n=== PESQUISE SEU CLIENTE ===")

    nome_busca = input("\nDigite o nome:  ").strip().title()

    if nome_busca in clientes:
        print(f"✅ Cliente '{nome_busca}' encontrado.")

    else:
        print(f"❌ Cliente '{nome_busca}' não encontrado.")

def excluir_cliente(clientes):
    print("=== EXCLUIR CADASTRO ===")

    nome_exc = input("\nDigite o nome: ").strip().title()

    while True:
        if nome_exc not in clientes:
            print("❌ Cliente não encontrado.")
            return
        
        conf_remov = input(f'Tem certeza que deseja excluir "{nome_exc}"? (S/N): ').strip().title()

        if conf_remov == "S":
            clientes.remove(nome_exc)
            print(f"✅ Cliente {nome_exc} removido.")
            break

        elif conf_remov == "N":
            print(f"Exclusão do cliente cancelada!")
            break

        else:
            print("Opção inválida."
                  "\nDigite apenas S ou N.")