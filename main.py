CATEGORIES = {
    # "nome": [min, max]
    "Roupas": [10, 100],
    "Acessorios": [30, 100],
    "Equipamentos": [5, 200],
}

produtos = []

print("Bem vindo ao sistema de cadastro de produtos")
while True:
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
        for category_name, minmax in CATEGORIES.items():
            print("{} (min: {}/max: {})".format(category_name, minmax[0], minmax[1]))
        categoria = input("Digite o nome da categoria: ")
        # nome
        nome = input("Nome do produto: ")
        # quantidade
        quantidade = int(input("Quantidade: "))

        # verificar se a quantidade é maior que o minimo da categoria
        if any(p["nome"] == nome for p in produtos):
            # se um produto ja existir, adicione mais
            for p in produtos:
                if p["nome"] == nome:
                    p["quantidade"] += quantidade
        elif categoria not in CATEGORIES:
            print("\n> Categoria não existe")
            continue
        elif quantidade < CATEGORIES[categoria][0]:
            print("\n> Quantidade menor que o minimo")
            continue
        elif quantidade > CATEGORIES[categoria][1]:
            print("\n> Quantidade maior que o maximo")
            continue
        else:
            # adicionar na lista de produtos
            produtos.append({
                "categoria": categoria,
                "nome": nome,
                "quantidade": quantidade
            })
    elif action == '2':
        # para cada categoria, mostre os produtos com : nome, quantidade
        for category_name, minmax in CATEGORIES.items():
            print("\n{}: {}/{}".format(category_name, minmax[0], minmax[1]))
            total = 0
            for produto in produtos:
                if produto["categoria"] == category_name:
                    print("- {}: {}".format(produto["nome"], produto["quantidade"]))
                    total += produto["quantidade"]
            print("> Porcentagem do estoque: {}%".format(total / minmax[1] * 100))

        pass
    elif action == '3':
        # perguntar o nome do produto
        produto = input("Digite o nome do produto: ")

        # remover produto da lista
        removed = False
        for p in produtos:
            if p["nome"] == produto:
                produtos.remove(p)
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