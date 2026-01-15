from banco.banco_plantas import BancoPlantas
from usuarios.empregado import Empregado
from plantas.briofita import Briofita
from plantas.pteridofita import Pteridofita
from plantas.gimnosperma import Gimnosperma
from plantas.angiosperma import Angiosperma


# ================= INSTÂNCIAS PRINCIPAIS =================

banco = BancoPlantas()
empregado = Empregado("Administrador")


# ================= PLANTAS INICIAIS =================

plantas_iniciais = [
    Angiosperma("Vitória-régia", "00001", "Angiosperma", "Grande",
                "Planta aquática símbolo da Amazônia",
                "Norte", None, None, "Verde"),
    Angiosperma("Açaizeiro", "00002", "Angiosperma", "Médio",
                "Base da alimentação amazônica",
                "Norte", "Açaí", "Roxo", "Verde"),
    Angiosperma("Castanheira", "00003", "Angiosperma", "Grande",
                "Pode viver mais de 500 anos",
                "Norte", "Castanha-do-pará", "Marrom", "Verde"),
    Angiosperma("Seringueira", "00004", "Angiosperma", "Grande",
                "Fonte do látex natural",
                "Norte", None, None, "Verde"),
    Angiosperma("Cupuaçuzeiro", "00005", "Angiosperma", "Médio",
                "Muito usado em doces",
                "Norte", "Cupuaçu", "Marrom", "Verde-escuro"),
    Pteridofita("Samambaia-açu", "00006", "Pteridófita", "Grande",
                None, "Norte", None, None, "Verde"),
    Briofita("Musgo amazônico", "00007", "Briófita", "Pequeno",
             None, "Norte", None, None, "Verde"),

    Angiosperma("Ipê-amarelo", "00008", "Angiosperma", "Grande",
                "Árvore símbolo do Brasil",
                "Centro-Oeste", None, None, "Verde"),
    Angiosperma("Pequi", "00009", "Angiosperma", "Médio",
                "Fruto típico do Cerrado",
                "Centro-Oeste", "Pequi", "Amarelo", "Verde"),
    Angiosperma("Buriti", "00010", "Angiosperma", "Grande",
                "Conhecida como árvore da vida",
                "Centro-Oeste", "Buriti", "Marrom", "Verde"),
    Angiosperma("Cagaita", "00011", "Angiosperma", "Médio",
                None, "Centro-Oeste", "Cagaita", "Amarelo", "Verde"),
    Angiosperma("Baru", "00012", "Angiosperma", "Grande",
                "Castanha nutritiva",
                "Centro-Oeste", "Baru", "Marrom", "Verde"),
    Pteridofita("Samambaia-do-cerrado", "00013", "Pteridófita", "Médio",
                None, "Centro-Oeste", None, None, "Verde"),
    Briofita("Musgo do cerrado", "00014", "Briófita", "Pequeno",
             None, "Centro-Oeste", None, None, "Verde-claro"),

    Angiosperma("Mandacaru", "00015", "Angiosperma", "Grande",
                "Cacto símbolo do sertão",
                "Nordeste", None, None, "Verde"),
    Angiosperma("Umbuzeiro", "00016", "Angiosperma", "Médio",
                "Produz frutos mesmo na seca",
                "Nordeste", "Umbu", "Verde", "Verde"),
    Angiosperma("Juazeiro", "00017", "Angiosperma", "Grande",
                "Mantém folhas na seca",
                "Nordeste", None, None, "Verde"),
    Angiosperma("Xique-xique", "00018", "Angiosperma", "Médio",
                None, "Nordeste", None, None, "Verde"),
    Angiosperma("Aroeira", "00019", "Angiosperma", "Grande",
                "Uso medicinal",
                "Nordeste", None, None, "Verde"),
    Pteridofita("Avenca", "00020", "Pteridófita", "Pequeno",
                None, "Nordeste", None, None, "Verde"),
    Briofita("Musgo da caatinga", "00021", "Briófita", "Pequeno",
             None, "Nordeste", None, None, "Verde-acinzentado"),

    Gimnosperma("Araucária", "00022", "Gimnosperma", "Grande",
                "Árvore símbolo do Sul",
                "Sul", None, None, "Verde"),
    Angiosperma("Erva-mate", "00023", "Angiosperma", "Médio",
                "Base do chimarrão",
                "Sul", None, None, "Verde"),
    Angiosperma("Imbuia", "00024", "Angiosperma", "Grande",
                "Madeira nobre",
                "Sul", None, None, "Verde"),
    Angiosperma("Bracatinga", "00025", "Angiosperma", "Médio",
                "Espécie pioneira",
                "Sul", None, None, "Verde"),
    Angiosperma("Canela", "00026", "Angiosperma", "Grande",
                "Casca aromática",
                "Sul", None, None, "Verde"),
    Gimnosperma("Pinheiro-brasileiro", "00027", "Gimnosperma", "Grande",
                None, "Sul", None, None, "Verde"),
    Briofita("Musgo sulino", "00028", "Briófita", "Pequeno",
             None, "Sul", None, None, "Verde-escuro"),

    Angiosperma("Pau-brasil", "00029", "Angiosperma", "Grande",
                "Árvore histórica",
                "Sudeste", None, None, "Verde"),
    Angiosperma("Manacá-da-serra", "00030", "Angiosperma", "Médio",
                "Flores mudam de cor",
                "Sudeste", None, None, "Verde"),
    Angiosperma("Jequitibá-rosa", "00031", "Angiosperma", "Gigante",
                "Uma das maiores árvores do Brasil",
                "Sudeste", None, None, "Verde"),
    Angiosperma("Quaresmeira", "00032", "Angiosperma", "Médio",
                "Flores roxas",
                "Sudeste", None, None, "Verde"),
    Angiosperma("Jatobá", "00033", "Angiosperma", "Grande",
                "Fruto comestível",
                "Sudeste", "Jatobá", "Marrom", "Verde"),
    Pteridofita("Samambaia-da-mata", "00034", "Pteridófita", "Médio",
                None, "Sudeste", None, None, "Verde"),
    Briofita("Musgo atlântico", "00035", "Briófita", "Pequeno",
             None, "Sudeste", None, None, "Verde"),
]

for planta in plantas_iniciais:
    banco.adicionar(planta)


# ================= FUNÇÕES AUXILIARES =================

def escolher_tipo():
    while True:
        print("1 - Briófita")
        print("2 - Pteridófita")
        print("3 - Gimnosperma")
        print("4 - Angiosperma")
        op = input("Escolha o tipo: ")

        tipos = {
            "1": "Briófita",
            "2": "Pteridófita",
            "3": "Gimnosperma",
            "4": "Angiosperma"
        }

        if op in tipos:
            return tipos[op]

        print("Opção inválida.")


def escolher_regiao():
    while True:
        print("1 - Norte")
        print("2 - Nordeste")
        print("3 - Centro-Oeste")
        print("4 - Sudeste")
        print("5 - Sul")
        op = input("Escolha a região: ")

        regioes = {
            "1": "Norte",
            "2": "Nordeste",
            "3": "Centro-Oeste",
            "4": "Sudeste",
            "5": "Sul"
        }

        if op in regioes:
            return regioes[op]

        print("Opção inválida.")

def questionario_tipo_planta():
    print("\n--- QUESTIONÁRIO BOTÂNICO ---")

    vasos = input("A planta possui vasos condutores? (s/n): ").lower()
    sementes = input("A planta produz sementes? (s/n): ").lower()
    frutos = input("A planta produz frutos? (s/n): ").lower()

    if vasos == "n":
        print("\n Resultado: **Briófita**")
    elif sementes == "n":
        print("\n Resultado: **Pteridófita**")
    elif frutos == "n":
        print("\n Resultado: **Gimnosperma**")
    else:
        print("\n Resultado: **Angiosperma**")



# ================= MENU EMPREGADO =================

def menu_empregado():
    # ---------- CRIAR SENHA ----------
    if not empregado.tem_senha():
        while True:
            senha = input("Crie uma senha (6 números): ")

            if not senha.isdigit() or len(senha) != 6:
                print("A senha deve conter exatamente 6 números.")
                continue

            confirmacao = input("Confirme a senha: ")

            if senha != confirmacao:
                print("As senhas não coincidem.")
                continue

            empregado.definir_senha(senha)
            print("Senha criada com sucesso!")
            break

    # ---------- LOGIN ----------
    while True:
        senha = input("Digite sua senha: ")

        if not senha.isdigit():
            print("A senha deve conter apenas números.")
            continue

        if senha != empregado._senha:
            print("Senha incorreta.")
            continue

        break

    # ---------- MENU ----------
    while True:
        print("\n--- MENU EMPREGADO ---")
        print("1 - Adicionar planta")
        print("2 - Atualizar planta")
        print("3 - Remover planta")
        print("4 - Listar plantas")
        print("5 - Alterar senha")
        print("6 - Voltar")

        op = input("Escolha: ")

        # ===== ADICIONAR PLANTA =====
        if op == "1":
            while True:
                nome = input("Nome da planta: ")
                if nome.replace(" ", "").isalpha():
                    break
                print("O nome não pode conter números.")

            while True:
                id_planta = input("ID (5 números): ")
                if id_planta.isdigit() and len(id_planta) == 5:
                    break
                print("ID inválido.")

            tipo = escolher_tipo()
            porte = input("Porte: ")
            regiao = escolher_regiao()

            curiosidade = None
            if input("Deseja inserir curiosidade? (s/n): ").lower() == "s":
                curiosidade = input("Curiosidade: ")

            nome_fruto = cor_fruto = None
            if tipo == "Angiosperma" and input("Possui fruto? (s/n): ").lower() == "s":
                nome_fruto = input("Nome do fruto: ")
                cor_fruto = input("Cor do fruto: ")

            while True:
                cor_folhas = input("Cor das folhas: ")
                if cor_folhas.replace(" ", "").isalpha():
                    break
                print("Cor inválida.")

            classe = {
                "Briófita": Briofita,
                "Pteridófita": Pteridofita,
                "Gimnosperma": Gimnosperma,
                "Angiosperma": Angiosperma
            }[tipo]

            planta = classe(
                nome, id_planta, tipo, porte,
                curiosidade, regiao,
                nome_fruto, cor_fruto, cor_folhas
            )

            banco.adicionar(planta)
            print("Planta adicionada com sucesso!")

        # ===== ATUALIZAR PLANTA =====
        elif op == "2":
            chave = input("Digite o nome ou ID da planta: ")
            planta = banco.buscar(chave)

            if not planta:
                print("Planta não encontrada.")
                continue

            nova_curiosidade = input("Nova curiosidade: ")
            planta.curiosidade = nova_curiosidade
            print("Planta atualizada.")

        # ===== REMOVER PLANTA =====
        elif op == "3":
            chave = input("Digite o nome ou ID da planta: ")
            if banco.remover(chave):
                print("Planta removida.")
            else:
                print("Planta não encontrada.")

        # ===== LISTAR =====
        elif op == "4":
            valor = input("Digite o nome ou ID da planta (ou ENTER para listar todas): ")

            if valor.strip() == "":
                for p in banco.plantas:
                    print(p)
                    print("-" * 40)
            else:
                p = banco.buscar(valor)

                if p is None:
                    print("Planta não encontrada.")
                else:
                    print(p)

        # ===== ALTERAR SENHA =====
        elif op == "5":
            senha_atual = input("Digite a senha atual: ")

            if senha_atual != empregado._senha:
                print("Senha incorreta.")
                continue

            while True:
                nova = input("Nova senha (6 números): ")

                if not nova.isdigit() or len(nova) != 6:
                    print("Senha inválida.")
                    continue

                confirmacao = input("Confirme a nova senha: ")

                if nova != confirmacao:
                    print("As senhas não coincidem.")
                    continue

                empregado.definir_senha(nova)
                print("Senha alterada com sucesso!")
                
                break
        elif op == "6":
            break

def menu_visitante():
    while True:
        print("\n--- MENU VISITANTE ---")
        print("1 - Listar todas as plantas")
        print("2 - Filtrar plantas")
        print("3 - Questionário: identificar tipo da planta")
        print("4 - Voltar")

        op = input("Escolha: ")

        # ===== LISTAR TODAS =====
        if op == "1":
            for p in banco.plantas:
                print(p)
                print("-" * 40)

        # ===== FILTRAR =====
        elif op == "2":
            print("\n--- FILTROS ---")
            print("1 - Por tipo")
            print("2 - Por região")
            print("3 - Por porte")

            f = input("Escolha: ")

            if f == "1":
                tipo = escolher_tipo()
                encontrados = [p for p in banco.plantas if p.tipo == tipo]

            elif f == "2":
                regiao = escolher_regiao()
                encontrados = [p for p in banco.plantas if p.regiao == regiao]

            elif f == "3":
                porte = input("Digite o porte (Pequeno, Médio, Grande, Gigante): ")
                encontrados = [p for p in banco.plantas if p.porte.lower() == porte.lower()]

            else:
                print("Opção inválida.")
                continue

            if not encontrados:
                print("Nenhuma planta encontrada.")
            else:
                for p in encontrados:
                    print(p)
                    print("-" * 40)

        # ===== QUESTIONÁRIO =====
        elif op == "3":
            questionario_tipo_planta()

        # ===== VOLTAR =====
        elif op == "4":
            break

        else:
            print("Opção inválida.")


# ================= MAIN =================

while True:
    print("\n--- SISTEMA DE PLANTAS DA ONG ---")
    print("1 - Empregado")
    print("2 - Visitante")
    print("3 - Sair")

    escolha = input("Qual área deseja acessar: ")

    if escolha == "1":
        menu_empregado()
    elif escolha == "2":
        menu_visitante()
    elif escolha == "3":
        print("Encerrando sistema...")
        break
