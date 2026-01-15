# PROJETO-FINAL--POO
Este projeto consiste em um sistema de catálogo de plantas desenvolvido em Python, com foco em Programação Orientada a Objetos (POO).
O sistema foi criado para uma ONG fictícia que realiza o registro, organização e consulta de plantas brasileiras, classificadas por tipo, região e porte.

O sistema possui dois perfis de usuários:

Empregado: possui acesso administrativo (com autenticação por senha).

Visitante: possui acesso apenas para consulta e exploração das plantas, sem necessidade de senha.

O projeto aplica de forma prática os principais conceitos de POO: Abstração, Encapsulamento, Polimorfismo, Herança e Modularização

🧠 Estrutura do Sistema
📁 Principais Módulos

plantas/

Planta (classe base)

Briofita

Pteridofita

Gimnosperma

Angiosperma

usuarios/

Usuario (classe base)

Empregado

Visitante

banco/

BancoPlantas → responsável por armazenar, buscar, listar e remover plantas

main.py

Ponto de entrada do sistema

Contém os menus e a interação com o usuário

▶️ Instruções para Execução
Execute o main.py e abrirá 3 opções, a primeira abrirá a área de funcionalidades do empregado, que consistem em gerenciar o banco de dados com as plantas
ou mudar a senha, mas, antes disso, é necessário que o empregado defina, confirme e utilize sua senha. Na opção 2, abrirá  as funcionalidades do Visitante, que consistem em ver todas as plantas catalogadas, filtrar por porte, tipo ou região e por fim, ser diirecionado para um pequeno questionário para verificar se uma planta vista pelo mesmo é briófita, pteridófita, gimno ou angiosperma.


🧪 Evidências dos Resultados e Testes
✅ Teste 1 — Listagem de Plantas

Ação: Listar todas as plantas cadastradas
Resultado esperado:
As plantas são exibidas com informações completas (nome, tipo, região, porte etc.)
Resultado obtido: ✅ Correto

✅ Teste 2 — Busca por Nome ou ID

Ação: Buscar uma planta pelo nome ou ID
Resultado esperado:
Exibição correta da planta correspondente
Resultado obtido: ✅ Correto
