import os

def load_data(df, path):
    """
    Realiza a etapa de carga (Load) do pipeline ETL.

    Salva o DataFrame em um arquivo CSV no caminho especificado.
    Caso o diretório não exista, ele será criado automaticamente.

    Etapas:
    1. Verifica/cria o diretório de destino
    2. Salva o DataFrame como CSV
    3. Exibe logs de sucesso ou erro

    Parâmetros:
    ----------
    df : pandas.DataFrame
        DataFrame contendo os dados a serem salvos.

    path : str
        Caminho completo (incluindo nome do arquivo) onde o CSV será salvo.

    Retorno:
    -------
    None
        A função não retorna valor, apenas salva o arquivo no sistema.
    """
    try:
        # Log informando onde o arquivo será salvo
        print(f"💾 Salvando arquivo em: {path}")

        # Cria o diretório caso ele não exista
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Salva o DataFrame no formato CSV
        df.to_csv(path, index=False, encoding="utf-8")

        # Log de sucesso com quantidade de registros
        print(f"✅ Arquivo salvo com sucesso! ({len(df)} registros)")

    except Exception as e:
        # Log de erro em caso de falha na gravação
        print(f"❌ Erro ao salvar dados: {e}")
        raise