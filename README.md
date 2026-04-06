# 🚀 Projeto ETL com IA - Geração de Mensagens Personalizadas

Pipeline de dados desenvolvido em Python que realiza extração, transformação e carga (ETL), integrando Inteligência Artificial para gerar mensagens personalizadas para clientes bancários.

---

## 📌 Objetivo

Automatizar a geração de mensagens de incentivo financeiro com base nos dados dos clientes, utilizando IA e boas práticas de engenharia de dados.

---

## 🧠 Tecnologias Utilizadas

- Python
- Pandas
- API de IA (Groq - LLaMA 3)
- python-dotenv
- Arquitetura ETL

---

## 🏗️ Estrutura do Projeto

```
projeto-etl/
│
├── data/
│   ├── clientes.csv        # Dados de entrada
│   └── output.csv          # Dados processados
│
├── src/
│   ├── extract.py          # Extração de dados
│   ├── transform.py        # Transformação + IA
│   ├── load.py             # Carga dos dados
│   ├── ai.py               # Integração com IA
│   └── main.py             # Orquestração do pipeline
│
├── .env                    # Variáveis de ambiente (não versionado)
├── .gitignore
├── requirements.txt
└── README.md
```
---
## 🔄 Pipeline ETL

### 1️⃣ Extração
- Leitura de arquivo CSV
- Padronização de colunas
- Validação de dados obrigatórios

### 2️⃣ Transformação
- Geração de mensagens personalizadas com IA
- Implementação de cache para otimização
- Tratamento de erros e fallback automático

### 3️⃣ Carga
- Salvamento dos dados processados em CSV
- Criação automática de diretórios

---

## ⚡ Diferenciais do Projeto

✅ Integração com API de Inteligência Artificial  
✅ Arquitetura modular (separação por camadas ETL)  
✅ Tratamento de erros robusto  
✅ Cache para redução de chamadas à API  
✅ Fallback automático (funciona mesmo sem IA)  
✅ Logs de execução (observabilidade)  
✅ Código limpo e documentado  

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/projeto-etl.git
cd projeto-etl
```

### 2. Criar ambiente virtual

```bash
python -m venv env
```
## Ativar o ambiente:

####  Linux/Mac
```
source env/bin/activate
```
####  Windows
```
env\Scripts\activate
```

### 3. Instalar dependências
```
pip install -r requirements.txt
```
### 4. Configurar variáveis de ambiente

#### Crie um arquivo .env na raiz do projeto:
```
GROQ_API_KEY=sua_chave_aqui
```
### 5. Executar o pipeline
```
python src/main.py
```
### Exemplo de Entrada

| nome        | cartao   |
| ----------- | -------- |
| João Silva  | Gold     |
| Maria Souza | Platinum |

### Exemplo de Saída
| nome        | cartao   | mensagem                             |
| ----------- | -------- | ------------------------------------ |
| João Silva  | Gold     | Invista com inteligência...          |
| Maria Souza | Platinum | Seu futuro financeiro começa hoje... | 

## 🛡️ Tratamento de Erros

- ❌ Falha na API → fallback automático  
- 📁 Arquivo inexistente → erro tratado  
- ⚠️ Dados inválidos → limpeza automática  
- ⏱️ Rate limit → controle com delay  

## 👨‍💻 Autor

**Romário Ferreira**

Projeto desenvolvido para:

- Bootcamp **DIO-TOTVS - Fundamentos de Engenharia de Dados e Machine Learning**
- Laboratório: *Explorando IA Generativa em um Pipeline de ETL com Python*

### 🎯 Foco do Projeto

- Engenharia de Dados  
- Integração com Inteligência Artificial  
- Boas práticas de desenvolvimento  
