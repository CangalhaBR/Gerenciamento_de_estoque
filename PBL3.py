# definição da senha
USUARIO = "admin"
SENHA = "@dmiN"

logged = False

# numero de tentativas
tries = 3

# pagina de login
while tries > 0:
    usuarioInput = input("Digite o Usuario: ")
    senhaInput = input("Digite a Senha: ")
    # se a senha for valida
    if usuarioInput == USUARIO and senhaInput == SENHA:
        logged = True
        print("Bem vindo ao sistema de cadastro de produtos")
        break
    # se a senha for invalida
    else:
        tries -= 1
        if(tries > 0):
            print("\nUsuario ou Senha invalidos \nVocê tem {} tentativas\n".format(tries))
        else:
            print("\nUsuario ou Senha invalidos \nVocê não tem mais tentativas\n")

CATEGORIES = {
    # "nome": min,
    "Roupas": 10,
    "Acessorios": 30,
    "Equipamentos": 5, 
}

produtos = []

while logged:
    print(
        """
    
        Escolha sua ação: 
        - 1: Cadastrar novo produto
        - 2: Listar produtos
        - 3: Editar Produtos
        - 4: Apagar produto
        - 5: Sair
        """
    )

    action = input("Digite sua ação: ")
    if action == '1':
        # Perguntar sobre o produto
        print("> Adicionar um produto:")

        # pegar as informações do produto
        # categoria
        print("Escolha a categoria: ")
        for category_name, min in CATEGORIES.items():
            print("{} (min: {})".format(category_name, min))
        categoria = input("Digite o nome da categoria: ")
        # nome
        nome = input("Nome do produto: ")
        # quantidade
        quantidade = int(input("Quantidade: "))

        
        if any(produto["nome"] == nome for produto in produtos):
            # se um produto ja existir, adicione mais
            for produto in produtos:
                if produto["nome"] == nome:
                    produto["quantidade"] += quantidade
        elif categoria not in CATEGORIES:
            print("\n> Categoria não existe")
            continue
        elif quantidade < CATEGORIES[categoria]: # verificar se a quantidade é maior que o minimo da categoria
            print("\n> Quantidade menor que o minimo")
            continue
        else:
            # adicionar na lista de produtos
            produtos.append({
                "categoria": categoria,
                "nome": nome,
                "quantidade": quantidade
            })
    elif action == '2':
        
        # calcular o total de produtos 
        total = 0
        for produto in produtos:
            total += produto["quantidade"]

        # para cada categoria, mostre os produtos com : nome, quantidade
        for category_name, min in CATEGORIES.items():
            print("\n{}: {} produtos mínimos".format(category_name, min))

            #  o total de produtos na categoria
            totalDaCategoria = 0
            for produto in produtos:
                if produto["categoria"] == category_name:
                    totalDaCategoria += produto["quantidade"]
            
            for produto in produtos:
                if produto["categoria"] == category_name:
                    print("- {}: {} ({:.2f}% da categoria) ({:.2f}% do estoque)".format(
                        produto["nome"], 
                        produto["quantidade"], 
                        produto["quantidade"] / totalDaCategoria * 100, 
                        produto["quantidade"] / total * 100
                    ))
                    
            # print total :
            print("> Total da categoria: {}".format(totalDaCategoria))

        pass
    elif action == '3':
        # perguntar o nome do produto 
        produtoInput = input("Nome do produto que deseja editar: ")

        # Ver se o produto existe
        exist = False  
        for produto in produtos:
            if produto["nome"] == produtoInput:
                exist = True
        if exist == False:
            print("\n> Produto não existe")
            continue
            
        
        # Perguntar o que deseja editar (1: categoria, 2: nome, 3: quantidade) e modificar o produto
        print("""
        O que deseja editar?
        - 1: Categoria
        - 2: Nome
        - 3: Quantidade
        """)
        action = input("Digite sua ação: ")
        

        for produto in produtos:
            if produto["nome"] == produtoInput:

                if action == '1':
                    for category_name in CATEGORIES.keys():
                        print("- {}".format(category_name))
                    categoria = input("Digite o nome da categoria: ")
                    
                    if categoria in CATEGORIES.keys():
                        produto["categoria"] = categoria 
                        print("Categoria modificada")
                    else:
                        print("\n> Categoria não exite")

                
                elif action == '2':
                    nome = input("Novo nome do produto: ")
                    produto["nome"] = nome
                    print("\n> Nome modificado")

                elif action == '3':
                    totalDaCategoria = 0
                    for produtoCheck in produtos:
                        if produtoCheck["categoria"] == produto["categoria"]:
                            totalDaCategoria += produtoCheck["quantidade"]
                    
                    quantidade = int(input("Quantidade (min: {}) (na categoria: {}): ".format(CATEGORIES[produto["categoria"]], totalDaCategoria)))

                    if totalDaCategoria - produto["quantidade"] + quantidade < CATEGORIES[produto["categoria"]]:
                        print("\n> Quantidade menor que o minimo")
                    else:
                        produto["quantidade"] = quantidade
                        print("\n> Quantidade alterada")

                break


    elif action == '4':
        # perguntar o nome do produto
        produtoInput = input("Digite o nome do produto: ")

        # remover produto da lista
        removed = False
        for produto in produtos:
            if produto["nome"] == produtoInput:
                produtos.remove(produto)
                print("\n> Produto removido")
                removed = True

        if not removed:
            print("\n> Produto não existe")
        pass
    elif action == '5':
        exit()
    else:
        print("\n> Ação não existe")
        continue