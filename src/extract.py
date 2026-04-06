import pandas as pd

def extract_data(path):
   
    try:
        print(f"📂 Lendo arquivo: {path}")

        df = pd.read_csv(path)

        # Padronizar nomes das colunas
        df.columns = df.columns.str.strip().str.lower()

        # Validar colunas obrigatórias
        required_columns = {"nome", "cartao"}
        missing = required_columns - set(df.columns)

        if missing:
            raise ValueError(f"❌ Colunas obrigatórias ausentes: {missing}")

        # Remover linhas vazias
        df = df.dropna(subset=["nome", "cartao"])

        print(f"✅ Dados carregados: {len(df)} registros")

        return df

    except FileNotFoundError:
        print("❌ Arquivo não encontrado.")
        raise

    except Exception as e:
        print(f"❌ Erro ao extrair dados: {e}")
        raise