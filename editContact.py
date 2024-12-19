import cleanTerminal

def execute(contacts):
  print("\n LISTA DOS CONTATOS SALVO")

  for index, contact in enumerate(contacts, start=1):
    print(f"  {index}. NOME: {contact["name"]}")

  try:
    id = int(input("\n INFORME O ID DO CONTATO QUE DESEJA ALTERAR: "))

    index = id - 1

  except Exception:
    cleanTerminal.execute()
    print(" DIGITE UM NÚMERO PARA ACESSAR O MENU\n")

  else:
    name = input("\n  NOME: ")

    if name:
      contacts[index]["name"] = name.upper()

    phone = input("  TELEFONE: ")

    if phone:
      contacts[index]["phone"] = phone

    email = input("  EMAIL: ")

    if email:
      contacts[index]["email"] = email.upper()

    cleanTerminal.execute()

    print(" CONTATO ATUALIZADO COM SUCESSO\n")

  return
