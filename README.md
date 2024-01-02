# Sistema de Chat Distribuído usando OmniORB e Python

Este projeto consiste em um sistema de chat distribuído implementado em Python utilizando o omniORB para comunicação entre os clientes e o servidor.

## Especificações Técnicas

* Linguagem: Python
* Framework: omniORB (implementação do padrão CORBA)
* Requisitos: omniORB, Python

Funcionalidades Principais

*Servidor de chat que permite comunicação entre múltiplos clientes distribuídos.
*Registro de logs do servidor.
*Histórico de conversas para todos os clientes.

Instalação
Pré-requisitos

Certifique-se de ter o omniORB instalado no seu sistema. Você pode encontrar instruções de instalação na documentação oficial do omniORB.
Passos de Instalação

    Clone o repositório para o seu ambiente local: 


git clone https://github.com/JoseDavi10/Chat-OmniORB-e-Conda.git


Configure o servidor e execute-o:

python server.py

Execute o cliente para interagir com o servidor:

    python client.py

Utilização

    Ao executar o servidor, ele começará a ouvir conexões dos clientes.
    Os clientes devem se conectar ao servidor fornecendo o endereço IOR e a porta do servidor.
    Após a conexão bem-sucedida, os clientes podem enviar mensagens que serão distribuídas a todos os outros clientes conectados.

Estrutura do Projeto

    server.py: Arquivo Python que inicia o servidor de chat.
    client.py: Arquivo Python que inicia o cliente de chat.
    chat.idl: Arquivo que define a interface do chat usando IDL (Interface Definition Language).

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para sugestões, problemas encontrados ou enviar pull requests.

Autores

    @JoseDavi10
    @Vitor-bs
    @Joaolucas045

Metodologia Ágil Utilizada

    https://trello.com/invite/b/XAsA7CBA/ATTI2544d69cbd397a7d446579815c87f143EED13552/trabalhos-finais

Vídeo da demonstração do sistema 

    https://www.youtube.com/watch?v=82zRMO6k7GI
    
Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
