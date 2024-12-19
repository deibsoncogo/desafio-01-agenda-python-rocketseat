import cleanTerminal

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

    break

  print()

  return
