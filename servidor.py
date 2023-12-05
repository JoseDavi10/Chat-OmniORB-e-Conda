from omniORB import CORBA
import Chate__POA

class ChatServant(Chate__POA.Chat):
    def __init__(self):
        self.users = []
        self.messages = []

    def sendMessage(self, username, message):
        formatted_message = f"{username}: {message}"
        print(formatted_message)
        self.messages.append(formatted_message)

    def receiveMessage(self):
        if self.messages:
            log = '\n'.join(self.messages)
            return log
        else:
            return "Nenhuma mensagem"

    def joinChat(self, username):
        self.users.append(username)
        print(f"{username} Entrou no Chat.")
        self.messages.append(f"{username} Entrou no Chat.")

    def leaveChat(self, username):
        self.users.remove(username)
        print(f"{username} Saiu do Chat.")
        self.messages.append(f"{username} Saiu do Chat.")

    def listUsers(self):
        return ', '.join(self.users)


orb = CORBA.ORB_init([], CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

chatServant = ChatServant()
chatObject = chatServant._this()

print("Servidor está rodando...")
print("IOR -> ", orb.object_to_string(chatObject))

orb.run()
