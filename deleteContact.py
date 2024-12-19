import cleanTerminal

def execute(contacts):
  print("\n LISTA DOS CONTATOS SALVO")

  for index, contact in enumerate(contacts, start=1):
    print(f"  {index}. NOME: {contact["name"]}")

  try:
    id = int(input("\n INFORME O ID DO CONTATO QUE DESEJA EXCLUIR: "))

    index = id - 1
  except Exception:
    cleanTerminal.execute()
    print(" DIGITE UM NÚMERO PARA ESCOLHER UM CONTATO\n")

  else:
    isDeleted = input(f"\n  PRESSIONE 1 PARA CANCELAR A EXCLUSÃO DE {contacts[index]["name"]}: ")

    if isDeleted == "1":
      cleanTerminal.execute()
      print(" EXCLUSÃO DO CONTATO CANCELADO\n")
      return

    contacts.remove(contacts[index])

    cleanTerminal.execute()

    print(" CONTATO EXCLUÍDO COM SUCESSO\n")

  return
