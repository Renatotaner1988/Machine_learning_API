## Apresentação MVP - Sistema de Machine Learning com API Integrada

# Visão Geral
Este MVP tem como objetivo demonstrar uma aplicação Fullstack que integra modelos de Machine Learning com uma interface de usuário funcional. O sistema utiliza técnicas de aprendizado de máquina para treinar modelos com dados, expondo a funcionalidade via uma API. O frontend interage com essa API, proporcionando uma experiência de usuário dinâmica e interativa.

# Arquitetura da Aplicação
- Backend (Python)

 - Bibliotecas Principais:
 - Pandas: Para carregamento e manipulação de dados.
 - Scikit-learn: Para criação e treinamento dos modelos de Machine Learning.
 - Flask ou FastAPI: Para a criação e gerenciamento da API.
 - Joblib/Pickle: Para salvar e carregar os modelos treinados.

# Funções:
- Treinamento e validação do modelo.
- Exposição do modelo treinado por meio de endpoints da API.
- Processamento e resposta às solicitações do frontend (predições baseadas em dados enviados pelo usuário).
- Frontend (HTML/CSS/JavaScript)
- HTML/CSS: Criação da interface de usuário para submissão de dados e exibição dos resultados.
- JavaScript (Fetch API/Axios): Comunicação com o backend por meio de chamadas HTTP.

# Funcionalidades:
- Interface amigável para o envio de dados ao modelo treinado.
- Visualização de predições em tempo real após a comunicação com a API.
- Feedback imediato com base nos resultados processados pelo modelo.


# Carregamento e Preparação dos Dados:

- O sistema utiliza a biblioteca Pandas para realizar a leitura e manipulação dos dados de entrada (dataset). Um exemplo de dataset utilizado neste MVP pode ser um dataset de doenças cardíacas.
- Os dados passam por pré-processamento, como normalização, preenchimento de valores faltantes e seleção de recursos relevantes.

# Treinamento do Modelo:

- Utiliza-se a biblioteca Scikit-learn para criar e treinar o modelo de machine learning com algoritmos como Random Forest, Decision Tree ou Logistic Regression.
- O modelo é treinado com os dados de entrada e ajustado com base em técnicas de validação cruzada.

# Exposição da API:
Com o modelo treinado, ele é integrado à API criada com Flask ou FastAPI.

# Endpoints são configurados para permitir:
- Envio de novos dados para predição.
- Obtenção de resultados em tempo real.
  
## Tecnologias Utilizadas

# Backend:
- Python
- Pandas, Scikit-learn
- Flask/FastAPI
- Joblib/Pickle
  
# Frontend:
-HTML/CSS
- JavaScript (Fetch API/Axios)

