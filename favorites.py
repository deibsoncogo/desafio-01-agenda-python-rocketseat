import cleanTerminal, toggleFavorite

def execute(contacts):
  cleanTerminal.execute()

  while True:
    print(" ESTES SÃO SEUS CONTATOS FAVORITOS:")

    for index, contact in enumerate(contacts, start=1):
      if contact["isFavorite"]:
        name = contact["name"]
        phone = contact["phone"]
        email = contact["email"]

        print(f"  {index}. NOME: {name} TELEFONE: {phone} E-MAIL: {email}")

    print("\n ESCOLHA O QUE DESEJA REALIZAR:")
    print("  1. ATRIBUIR OU REMOVER O FAVORITISMO")
    print("  2. PARA VOLTAR AO MENU ANTERIOR")

    try:
      option = int(input("\n  ESCOLHA UMA OPÇÃO: "))

    except Exception:
      cleanTerminal.execute()
      print(" DIGITE UM NÚMERO PARA ACESSAR O MENU\n")

    else:
      if option == 1:
        toggleFavorite.execute(contacts)
      elif option == 2:
        cleanTerminal.execute()
        break

  return
