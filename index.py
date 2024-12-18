import cleanTerminal, createContact, findContacts, editContact, deleteContact

contacts = []

cleanTerminal.execute()

while True:
  print(" BEM VINDO A AGENDA DE CONTATOS")
  print("  1. ADICIONAR UM CONTATO")
  print("  2. LISTAR OS CONTATOS")
  print("  3. EDITAR UM CONTATO")
  print("  4. EXCLUIR UM CONTATO")
  print("  5. FAVORITOS")
  print("  6. SAIR")

  option = int(input("\n  ESCOLHA UMA OPÇÃO: "))

  if option == 1:
    createContact.execute(contacts)
  elif option == 2:
    findContacts.execute(contacts)
  elif option == 3:
    editContact.execute(contacts)
  elif option == 4:
    deleteContact.execute(contacts)
  elif option == 6:
    print("\n  APLICAÇÃO ENCERRADA")
    break
