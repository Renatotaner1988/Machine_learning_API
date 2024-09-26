## Instruções para Executar a Aplicação
# Pré-requisitos
- Python 3.x instalado na máquina.
- Um terminal ou prompt de comando disponível para executar as instruções.

# Passos para rodar a aplicação
1. Clonar o Repositório Primeiro, clone o repositório da aplicação para sua máquina local: ``` git clone https://github.com/seu-repositorio/aqui ```

2. Navegar até a Pasta da API Acesse a pasta do projeto onde está localizada a API: ``` cd caminho/para/pasta/API ```

3. Criar um Ambiente Virtual Crie um ambiente virtual para garantir que as dependências do projeto sejam instaladas isoladamente: ``` python -m venv venv ```

4. Ativar o Ambiente Virtual Após criar o ambiente virtual, ative-o:  No Windows: ``` venv\Scripts\activate ``` No macOS/Linux: ``` source venv/bin/activate ```

5. Instalar Dependências Com o ambiente virtual ativado, instale as dependências necessárias que estão listadas no arquivo requirements.txt: ``` pip install -r requirements.txt ```

6. Rodar a Aplicação Agora que todas as dependências estão instaladas, execute a aplicação com o comando: ``` flask run --host 0.0.0.0 --port 5000 --reload ```
- Esse comando irá iniciar a aplicação Flask no endereço http://0.0.0.0:5000, permitindo que ela seja acessada de outros dispositivos na mesma rede local.

7. Acessar a Aplicação Abra um navegador da web e acesse a aplicação através do seguinte endereço: ``` http://localhost:5000 ```
