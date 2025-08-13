import psycopg2

def conectar():
    conectar = None
    cursor = None
    db_parametros = "postgresql://neondb_owner:npg_eofApGy3ENI2@ep-damp-credit-acl67pm4-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    try:
        conectar = psycopg2.connect(db_parametros)
        cursor = conectar.cursor()
        print("conexao bem sucedida")
    except:
        print("erro ao conectar")

    return conectar,cursor


def fechar(cursor,conexao):
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
        print("conexao fechada")
        
