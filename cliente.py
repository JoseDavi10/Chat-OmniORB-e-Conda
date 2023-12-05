from omniORB import CORBA
import Chate
import sys

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
ior = input("Digite o IOR: ")
obj = orb.string_to_object(ior)
chat = obj._narrow(Chate.Chat)

if chat is None:
    raise Exception("IOR inexistente")

username = input("Nome de usuário: ")
chat.joinChat(username)

while True:

    received_message = chat.receiveMessage()
    print("Chat:\n",received_message)
    print("\n1. Enviar Mensagem")
    print("2. Usuários online")
    print("3. Sair")
    
    choice = input("escolha a opção (1|2|3): ")

    if choice == '1':
        message = input("Digite a Mensagem: ")
        chat.sendMessage(username, message)

    elif choice == '2':
        users = chat.listUsers()
        print("Usuários Online:", users)
        input("Pressione Enter Para Sair")

    elif choice == '3':
        chat.leaveChat(username)
        break

    
orb.destroy()
