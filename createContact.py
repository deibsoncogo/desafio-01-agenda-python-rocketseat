import cleanTerminal

def execute(contacts):
  print("\n INFORME OS DADOS DO CONTATO:")

  try:
    name = input("  NOME: ")
    phone = int(input("  TELEFONE: "))
    email = input("  EMAIL: ")

    favorite = input("\n  PRESSIONE 1 PARA FAVORITAR ELE: ")
    isFavorite = True if favorite == "1" else False
  except Exception:
    cleanTerminal.execute()
    print(" VALOR DIGITADO INVÁLIDO, TENTE NOVAMENTE\n")

  else:
    contact = {
      "name": name.upper(),
      "phone": phone,
      "email": email.upper(),
      "isFavorite": isFavorite
    }

    contacts.append(contact)

    cleanTerminal.execute()

    print(" CONTATO ADICIONADO COM SUCESSO\n")

  return
