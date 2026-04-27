import json
funcionario = []

# FUNÇÃO SALVAR DADOS EM JSON

def salvar_dados():
    with open("funcionario.json", "w") as arquivo:
        json.dump(funcionario, arquivo, indent=4)

# FUNÇÃO CARREGAR DADOS DO JSON

def carregar_dados():
    global funcionario
    try:
        with open("funcionario.json", "r") as arquivo:
            funcionario = json.load(arquivo)
    except FileNotFoundError:
        funcionario = []

# CADASTRAR FUNCIONARIO

def cadastrar_funcionario():
    print("=== CADASTRO FUNCIONARIOS === ")
    
    # DIGITAR NOME DO FUNCIONARIO E VERIFICAR/CORRIGIR
    while True:
        nome = input("Digite o nome do funcionario: ").strip()

        if not nome:
            print("❌ Nome não pode ser vazio!")
            continue

        if not nome.replace(" ", "").isalpha():
            print("❌ Nome deve conter apenas letras!")
            continue
        
        break       
    
    # DIGITAR CPF E VERIFICAR/CORRIGIR
    while True:
        
        cpf = input("Digite o CPF do funcionario: ").strip()

        if not cpf.isdigit():
            print("❌ CPF deve conter apenas números")
            continue
            
        if len(cpf) != 11:
            print("❌ CPF deve ter 11 dígitos!")
            continue

        if any(f['cpf'] == cpf for f in funcionario):
            print("❌ CPF já cadastrado")
            continue
        break
    
    # DIGITAR CARGO DO FUNCIONARIO
    cargo = input("Digite o cargo do funcionario: ").strip().replace(",", ".")

    # DIGITAR SALARIO DO FUNCIONARIO
    while True:
        salario = input("Digite o salário do funcionario: ").strip()

        try:
            salario_float = float(salario)
            if salario_float < 0:
                print("❌ Salário não pode ser negativo!")
                continue
            break
        except ValueError:
            print("❌ Salário deve ser um número válido!")
            continue

    funcionario.append({
    "nome": nome,
    "cpf": cpf,
    "cargo": cargo,
    "salario": salario_float
    })
    salvar_dados()

    print(f"✅ Funciario {nome} cadastrado")


# PROCURAR FUNCIONARIO

def procurar_func():
    cpf = input("Digite o cpf do funcionario: ").strip()
    verificar = False

    for lista in funcionario:
        if cpf == lista['cpf']:
            print(f"{lista['nome']} | {lista['cargo']}")
            verificar = True

    if not verificar:
        print("❌ Funcionario não encontrado!")   

    
# LISTAR TODOS OS FUNCIONARIOS

def listar_func():
    
    if not funcionario:
        print("Nenhum funcionario cadastrado")
        return
    
    print(f"\n=== LISTA DE FUNCIONARIOS ({len(funcionario)}) ===")
    for l in funcionario:
        print(f"{l['nome']} | {l['cpf']} | {l['cargo']} | R$ {l['salario']:.2f}")

# EDITAR FUNCIONARIO    

def editar_func():
    cpf = input("Digite o cpf do funcionario que quer editar: ").strip()
    encontrado = False

    for lista in funcionario:
        if cpf == lista['cpf']:
            
            encontrado = True    

            print("\n=== FUNCIONARIO ===")
            print(f"Nome : {lista['nome']}")
            print(f"CPF  : {lista['cpf']}")
            print(f"Cargo: {lista['cargo']}")
            print(f"Salário: R$ {lista['salario']:.2f}")
            # Editar novo nome
            novo_nome = input("Digite o novo nome: ")
            if novo_nome:
                if novo_nome.replace(" ", "").isalpha():
                    lista['nome'] = novo_nome 
                else:
                    print("❌ Nome inválido, mantendo o antigo.")

            # Editar cargo
            novo_cargo = input("Digite o novo cargo: ")
            if novo_cargo:
                if novo_cargo.replace(" ", "").isalpha():
                    lista['cargo'] = novo_cargo
                else:
                    print("❌ Cargo inválido, mantendo o antigo.")

            # Editar salário
            while True:
                novo_salario = input("Digite o novo salário: ").strip().replace(",", ".")
                if not novo_salario:
                    break
                try:
                    salario_float = float(novo_salario)
                    if salario_float < 0:
                        print("❌ Salário não pode ser negativo!")
                        continue
                    lista['salario'] = salario_float
                    break
                except ValueError:
                    print("❌ Salário deve ser um número válido!")
                    continue
            
            print("✅ Funcionário atualizado com sucesso!")
            salvar_dados()
            return

    if not encontrado:
        print("❌ Funcionario não encontrado!")

# EXCLUIR FUNCIONARIO       

def excluir_func():
    cpf_excluir = input("Digite o CPF do funcionario a ser excluído: ").strip()
    cpf_encontrado = False

    for l in funcionario:
        if cpf_excluir == l['cpf']:

            cpf_encontrado = True

            print("\n=== FUNCIONARIO ===")
            print(f"Nome : {l['nome']}")
            print(f"CPF  : {l['cpf']}")
            print(f"Cargo: {l['cargo']}")
            print(f"Salário: R$ {l['salario']:.2f}")

            confirmar = input("Tem certeza que deseja excluir? (s/n)").strip().lower()

            if confirmar == "s":
                funcionario.remove(l)
                print("✅ Funcionario removido com sucesso!")
                salvar_dados()
            else:
                print("❌ Exclusão cancelada!") 
            return
        
    if not cpf_encontrado:
        print("❌ Funcionário não encontrado!")

# MENU DE OPÇÕES

def menu():

    while True:
        print("=== ESCOLHA SUA OPÇÃO ===\n"
          "1 - Cadastrar Funcionáio\n"
          "2 - Procurar Funcionáio\n"
          "3 - Listar Funcionáio\n"
          "4 - Editar Funcionáio\n"
          "5 - Excluir Funcionáio\n"
          "6 - Sair"
          )
    
        op = input("Digite sua opção: ").strip()

        if op == "1":
            cadastrar_funcionario()
        elif op == "2":
            procurar_func()
        elif op == "3":
            listar_func()
        elif op == "4":
            editar_func()
        elif op == "5":
           excluir_func()
        elif op == "6":
            print("Saíndo do sistema, tenha uma ótima jornada✅...")
            break
        else:
            print("❌ Opção inválida")


carregar_dados()
menu()





           

    
    




        