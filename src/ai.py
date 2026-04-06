from groq import Groq
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente da API Groq utilizando a chave definida no .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_message(nome, cartao):
    """
    Gera uma mensagem personalizada para um cliente utilizando IA.

    A função envia uma solicitação para o modelo de linguagem (LLaMA 3 via Groq),
    pedindo a criação de uma mensagem curta de incentivo ao investimento.

    Caso ocorra qualquer erro na comunicação com a API (ex: falta de internet,
    limite de requisições, chave inválida), a função retorna uma mensagem padrão
    (fallback), garantindo que o pipeline não seja interrompido.

    Parâmetros:
    ----------
    nome : str
        Nome do cliente.
    
    cartao : str
        Tipo ou identificação do cartão do cliente.

    Retorno:
    -------
    str
        Mensagem personalizada gerada pela IA ou uma mensagem padrão em caso de erro.
    """
    try:
        # Realiza a chamada para a API de IA
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em marketing bancário."
                },
                {
                    "role": "user",
                    "content": f"Crie uma mensagem curta incentivando {nome}, cliente com cartão {cartao}, a investir dinheiro."
                }
            ]
        )

        # Retorna o conteúdo da resposta gerada pelo modelo
        return response.choices[0].message.content

    except Exception as e:
        # Em caso de erro, retorna uma mensagem padrão (fallback)
        return f"{nome}, com seu cartão {cartao}, que tal começar a investir?"