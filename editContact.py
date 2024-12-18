import cleanTerminal

def execute(contacts):
  print("\n LISTA DOS CONTATOS SALVO")

  for index, contact in enumerate(contacts, start=1):
    print(f"  {index}. NOME: {contact["name"]}")

  id = input("\n INFORME O ID DO CONTATO QUE DESEJA ALTERAR: ")

  index = int(id) - 1

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
