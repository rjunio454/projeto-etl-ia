import os
from extract import extract_data
from transform import transform_data
from load import load_data

# ================================
# CONFIGURAÇÃO DE CAMINHOS
# ================================

# Diretório base do projeto (volta 2 níveis a partir do src/)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Caminho do arquivo de entrada (dados brutos)
INPUT_PATH = os.path.join(BASE_DIR, "data", "clientes.csv")

# Caminho do arquivo de saída (dados processados)
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "output.csv")


def run_pipeline():
    """
    Executa o pipeline completo de ETL:

    Etapas:
    1. Extração: leitura dos dados do CSV
    2. Transformação: geração de mensagens com IA
    3. Carga: salvamento dos dados processados

    O pipeline possui tratamento de erro global para evitar falhas silenciosas
    e facilitar o debug.
    """
    try:
        # Log inicial
        print("🚀 Iniciando pipeline ETL...\n")

        # ================================
        # ETAPA 1 - EXTRAÇÃO
        # ================================
        print("🔄 [1/3] Extraindo dados...")
        df = extract_data(INPUT_PATH)

        # ================================
        # ETAPA 2 - TRANSFORMAÇÃO
        # ================================
        print("🧠 [2/3] Transformando dados com IA...")
        df = transform_data(df)

        # ================================
        # ETAPA 3 - CARGA
        # ================================
        print("💾 [3/3] Carregando dados...")
        load_data(df, OUTPUT_PATH)

        # Log final de sucesso
        print("\n✅ ETL finalizado com sucesso!")

    except Exception as e:
        # Tratamento de erro global do pipeline
        print(f"\n❌ Erro no pipeline: {e}")


# ================================
# PONTO DE ENTRADA DO SCRIPT
# ================================
if __name__ == "__main__":
    run_pipeline()