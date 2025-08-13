import psycopg2
import funçao

#criar a conexao
conexao,ponteiro = funçao.conectar()

if conexao:
    try:
        comando = '''
        SELECT
            servico.tiposervico,
            pagamento.tipopagamento,
            SUM(orcamento.valor)
        FROM servico
        INNER JOIN
            servico_conserto ON servico.num_os = servico_conserto.num_os
        INNER JOIN
            conserto ON servico_conserto.id_conserto = conserto.id_conserto
        INNER JOIN
            orcamento ON conserto.id_orcamento = orcamento.id_orcamento
        INNER JOIN
            pagamento ON orcamento.id_orcamento = pagamento.id_orcamento
        GROUP BY
           servico.tiposervico,
            pagamento.tipopagamento
        ORDER BY
            sum(orcamento.valor)DESC
        '''

        ponteiro.execute(comando)
        resultado = ponteiro.fetchall()

        print("relatorio")
        for coluna in resultado:
            print(f"""
            tiposervico {coluna[0]}
            tipopagamento {coluna[1]}
            somadosvalores {coluna[2]}
            """)

    except:
        print("ocorreu um erro ao tentar mexer no banco")
    finally:
        funçao.fechar(ponteiro,conexao)
