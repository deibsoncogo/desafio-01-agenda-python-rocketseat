import cleanTerminal, findContacts

def execute(contacts):
  findContacts.execute(contacts)

  try:
    id = input(" INFORME O ID DO CONTATO QUE DESEJA ALTERAR: ")

  except Exception:
    cleanTerminal.execute()
    print(" DIGITE UM NÚMERO PARA ACESSAR O MENU\n")

  else:
    index = int(id) - 1

    if contacts[index]["isFavorite"]:
      contacts[index]["isFavorite"] = False
    else:
      contacts[index]["isFavorite"] = True

    cleanTerminal.execute()

    print(" CONTATO ATUALIZADO COM SUCESSO\n")
