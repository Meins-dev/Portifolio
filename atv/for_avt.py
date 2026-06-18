import os
restaurantes = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_restaurante():
    limpar_tela()
    print("--- CADASTRO DE RESTAURANTE ---")
    
    nome = input("Nome do restaurante: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("Estado (UF): ").strip().upper()
    funcionarios = int(input("Quantidade de funcionários: "))
    clientes = int(input("Quantidade de clientes atendidos no mês: "))
    faturamento = float(input("Faturamento mensal (R$): "))
    entregues = int(input("Quantidade de pedidos entregues: "))
    cancelados = int(input("Quantidade de pedidos cancelados: "))
    
    while True:
        nota = float(input("Nota média dos clientes (0 a 10): "))
        if 0 <= nota <= 10:
            break
        print("Nota inválida! Digite um valor entre 0 e 10.")
        
    pratos = int(input("Quantidade de pratos no cardápio: "))
    
    restaurante = {
        "nome": nome, "cidade": cidade, "estado": estado,
        "funcionarios": funcionarios, "clientes": clientes,
        "faturamento": faturamento, "pedidos_entregues": entregues,
        "pedidos_cancelados": cancelados, "nota_media": nota,
        "pratos_cardapio": pratos
    }
    
    restaurantes.append(restaurante)
    print(f"\nRestaurante '{nome}' cadastrado com sucesso!")
    input("\nPressione Enter para voltar ao menu...")


def exibir_relatorio_completo():
    limpar_tela()
    if not restaurantes:
        print("Nenhum restaurante cadastrado no sistema.")
        input("\nPressione Enter para voltar...")
        return

    print("--- RELATÓRIO COMPLETO E ANÁLISES ---\n")
    
    
    total_faturamento = sum(r['faturamento'] for r in restaurantes)
    media_faturamento_geral = total_faturamento / len(restaurantes)
    total_notas = sum(r['nota_media'] for r in restaurantes)
    media_notas_geral = total_notas / len(restaurantes)
    
    total_entregues = sum(r['pedidos_entregues'] for r in restaurantes)
    total_cancelados = sum(r['pedidos_cancelados'] for r in restaurantes)
    total_pedidos = total_entregues + total_cancelados
    perc_cancelados_geral = (total_cancelados / total_pedidos * 100) if total_pedidos > 0 else 0
    
    restaurantes_mais_20_func = [r for r in restaurantes if r['funcionarios'] > 20]
    if restaurantes_mais_20_func:
        media_clientes_mais_20_func = sum(r['clientes'] for r in restaurantes_mais_20_func) / len(restaurantes_mais_20_func)
    else:
        media_clientes_mais_20_func = 0

    rest_maior_fat = max(restaurantes, key=lambda x: x['faturamento'])
    rest_menor_canc = min(restaurantes, key=lambda x: x['pedidos_cancelados'])
    rest_mais_clientes = max(restaurantes, key=lambda x: x['clientes'])


    print("CÁLCULOS E ANÁLISES GERAIS:")
    print(f"  • Restaurante com maior faturamento: {rest_maior_fat['nome']} (R$ {rest_maior_fat['faturamento']:.2f})")
    print(f"  • Restaurante com menor nº de cancelamentos: {rest_menor_canc['nome']} ({rest_menor_canc['pedidos_cancelados']} cancelados)")
    print(f"  • Média de clientes (restaurantes > 20 funcionários): {media_clientes_mais_20_func:.2f}")
    print(f"  • Percentual de pedidos cancelados em relação ao total: {perc_cancelados_geral:.2f}%")
    print(f"  • Média das notas dos clientes entre todos: {media_notas_geral:.2f}")
    print(f"  • Média de faturamento geral: R$ {media_faturamento_geral:.2f}")
    print("-" * 50)


    print("LISTAGENS E RELATÓRIOS ESPECÍFICOS:")
    
    print("\n  • Mais de 100 pratos no cardápio:")
    for r in restaurantes:
        if r['pratos_cardapio'] > 100: print(f"    - {r['nome']} ({r['pratos_cardapio']} pratos)")
        
    print("\n  • Nota média acima de 9:")
    for r in restaurantes:
        if r['nota_media'] > 9: print(f"    - {r['nome']} (Nota: {r['nota_media']})")
        
    print(f"\n  • Maior quantidade de clientes atendidos:\n    - {rest_mais_clientes['nome']} ({rest_mais_clientes['clientes']} clientes)")
    
    print("\n  • Faturamento ultrapassa R$ 100.000,00:")
    for r in restaurantes:
        if r['faturamento'] > 100000: print(f"    - {r['nome']} (R$ {r['faturamento']:.2f})")
        
    input("\nPressione Enter para voltar ao menu...")


def buscar_restaurante():
    limpar_tela()
    print("--- BUSCAR RESTAURANTE ---")
    nome_busca = input("Digite o nome do restaurante que deseja buscar: ").strip().lower()
    
    encontrado = False
    for r in restaurantes:
        if nome_busca in r['nome'].lower():
            encontrado = True
            print(f"\nResultado encontrado:")
            print(f"   Nome: {r['nome']} | Cidade: {r['cidade']}-{r['estado']}")
            print(f"   Faturamento: R$ {r['faturamento']:.2f} | Nota: {r['nota_media']}")
            print(f"   Funcionários: {r['funcionarios']} | Pratos: {r['pratos_cardapio']}")
            print("-" * 40)
            
    if not encontrado:
        print("\n Nenhum restaurante encontrado com esse nome.")
    input("\nPressione Enter para voltar...")


def mostrar_estatisticas_adicionais():
    limpar_tela()
    if not restaurantes:
        print("Nenhum restaurante cadastrado no sistema.")
        input("\nPressione Enter para voltar...")
        return

    print("--- ESTATÍSTICAS ADICIONAIS ---\n")
    
    media_faturamento_geral = sum(r['faturamento'] for r in restaurantes) / len(restaurantes)

    acima_da_media = sum(1 for r in restaurantes if r['faturamento'] > media_faturamento_geral)

    faturamento_por_estado = {}
    for r in restaurantes:
        faturamento_por_estado[r['estado']] = faturamento_por_estado.get(r['estado'], 0) + r['faturamento']
    estado_maior_fat = max(faturamento_por_estado, key=faturamento_por_estado.get)
    

    clientes_por_cidade = {}
    for r in restaurantes:
        clientes_por_cidade[r['cidade']] = clientes_por_cidade.get(r['cidade'], 0) + r['clientes']
    cidade_mais_clientes = max(clientes_por_cidade, key=clientes_por_cidade.get)
    

    nota_sup_8 = sum(1 for r in restaurantes if r['nota_media'] > 8)
    porcentagem_nota_8 = (nota_sup_8 / len(restaurantes)) * 100
    

    total_cancelados_geral = sum(r['pedidos_cancelados'] for r in restaurantes)

    print(f"• Qtd. de restaurantes com faturamento acima da média: {acima_da_media}")
    print(f"• Estado com maior faturamento total: {estado_maior_fat} (R$ {faturamento_por_estado[estado_maior_fat]:.2f})")
    print(f"• Cidade que possui mais clientes atendidos: {cidade_mais_clientes} ({clientes_por_cidade[cidade_mais_clientes]} clientes)")
    print(f"• Porcentagem de restaurantes com nota > 8: {porcentagem_nota_8:.1f}%")
    print(f"• Total geral de pedidos cancelados: {total_cancelados_geral}")

    input("\nPressione Enter para voltar ao menu...")


def atualizar_restaurante():
    limpar_tela()
    print("--- ATUALIZAR DADOS ---")
    nome_busca = input("Digite o nome exato do restaurante para atualizar: ").strip().lower()
    
    for r in restaurantes:
        if r['nome'].lower() == nome_busca:
            print(f"\nRestaurante encontrado! Insira os novos dados:")
            r['faturamento'] = float(input(f"Novo Faturamento (Antigo: {r['faturamento']}): "))
            r['clientes'] = int(input(f"Nova Qtd. Clientes (Antigo: {r['clientes']}): "))
            r['nota_media'] = float(input(f"Nova Nota Média (Antigo: {r['nota_media']}): "))
            r['funcionarios'] = int(input(f"Nova Qtd. Funcionários (Antigo: {r['funcionarios']}): "))
            print("\nDados atualizados com sucesso!")
            input("\nPressione Enter para voltar...")
            return
            
    print("\nRestaurante não encontrado.")
    input("\nPressione Enter para voltar...")


def remover_restaurante():
    limpar_tela()
    print("--- REMOVER RESTAURANTE ---")
    nome_busca = input("Digite o nome exato do restaurante para remover: ").strip().lower()
    
    for r in restaurantes:
        if r['nome'].lower() == nome_busca:
            restaurantes.remove(r)
            print(f"\nRestaurante '{r['nome']}' removido do sistema.")
            input("\nPressione Enter para voltar...")
            return
            
    print("\nRestaurante não encontrado.")
    input("\nPressione Enter para voltar...")


def menu_principal():
    while True:
        limpar_tela()
        print("=======================================")
        print("  SISTEMA DE GESTÃO DE RESTAURANTES    ")
        print("=======================================")
        print("1 - Cadastrar restaurantes")
        print("2 - Exibir relatório completo")
        print("3 - Buscar restaurante pelo nome")
        print("4 - Mostrar estatísticas gerais")
        print("5 - Atualizar dados de restaurante")
        print("6 - Remover restaurante")
        print("7 - Encerrar sistema")
        print("=======================================")
        
        opcao = input("Escolha uma opção (1-7): ").strip()
        
        if opcao == '1':
            cadastrar_restaurante()
        elif opcao == '2':
            exibir_relatorio_completo()
        elif opcao == '3':
            buscar_restaurante()
        elif opcao == '4':
            mostrar_estatisticas_adicionais()
        elif opcao == '5':
            atualizar_restaurante()
        elif opcao == '6':
            remover_restaurante()
        elif opcao == '7':
            print("\nEncerrando o sistema... Até mais!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()