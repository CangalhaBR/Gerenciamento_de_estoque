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
        - 3: Apagar produto
        - 4: Sair
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

        # verificar se a quantidade é maior que o minimo da categoria
        if any(produto["nome"] == nome for produto in produtos):
            # se um produto ja existir, adicione mais
            for produto in produtos:
                if produto["nome"] == nome:
                    produto["quantidade"] += quantidade
        elif categoria not in CATEGORIES:
            print("\n> Categoria não existe")
            continue
        elif quantidade < CATEGORIES[categoria]:
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

            # caucular o total de produtos na categoria
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
    elif action == '4':
        exit()
    else:
        print("\n> Ação não existe")
        continue