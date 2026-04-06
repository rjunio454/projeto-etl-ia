from ai import generate_message
import time

def transform_data(df):
    """
    Realiza a transformação dos dados, gerando mensagens personalizadas
    para cada cliente utilizando IA.

    Etapas:
    1. Itera sobre cada linha do DataFrame
    2. Gera mensagens com base no nome e cartão
    3. Utiliza cache para evitar chamadas repetidas à API
    4. Trata erros sem interromper o pipeline
    5. Adiciona a coluna 'mensagem' ao DataFrame

    Parâmetros:
    ----------
    df : pandas.DataFrame
        DataFrame contendo os dados dos clientes.
        Deve possuir as colunas 'nome' e 'cartao'.

    Retorno:
    -------
    pandas.DataFrame
        DataFrame original com a nova coluna 'mensagem'.
    """

    # Lista que armazenará as mensagens geradas
    mensagens = []

    # Cache para evitar chamadas repetidas à API para o mesmo cliente
    cache = {}

    # Total de registros (para log de progresso)
    total = len(df)

    # Itera sobre cada linha do DataFrame
    for i, row in df.iterrows():
        nome = row["nome"]
        cartao = row["cartao"]

        # Cria uma chave única para identificar combinações repetidas
        chave = f"{nome}_{cartao}"

        # Log de progresso
        print(f"🧠 Processando {i+1}/{total} - {nome}")

        # Verifica se já existe no cache
        if chave in cache:
            msg = cache[chave]

        else:
            try:
                # Gera mensagem usando IA
                msg = generate_message(nome, cartao)

                # Armazena no cache para reutilização
                cache[chave] = msg

            except Exception as e:
                # Log de erro sem interromper o pipeline
                print(f"❌ Erro com {nome}: {e}")
                msg = "Erro ao gerar mensagem"

            # Pequeno delay para evitar rate limit da API
            time.sleep(1)

        # Adiciona a mensagem à lista final
        mensagens.append(msg)

    # Cria nova coluna no DataFrame com as mensagens geradas
    df["mensagem"] = mensagens

    return df