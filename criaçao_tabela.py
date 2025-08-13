import psycopg2
import funçao

#criar a conexao
conexao,ponteiro = funçao.conectar()

if conexao:
    try:
        comando = '''
        DROP TABLE teste
        '''
        
        ponteiro.execute(comando)
        conexao.commit()
        print("tabela criada com sucesso")

    except:
        print("ocorreu um erro ao tentar mexer no banco")
    finally:
        funçao.fechar(ponteiro,conexao)
