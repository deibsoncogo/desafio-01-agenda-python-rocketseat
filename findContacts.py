import cleanTerminal

def execute(contacts):
  cleanTerminal.execute()

  print(" CONTATOS LISTADO COM SUCESSO")

  for index, contact in enumerate(contacts, start=1):
    name = contact["name"]
    phone = contact["phone"]
    email = contact["email"]

    print(f"  {index}. NOME: {name} TELEFONE: {phone} E-MAIL: {email}")

  print()

  return
