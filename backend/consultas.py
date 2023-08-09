from connection import Connection



def inserir_dados():
    #Assegurar conexao
    conexao = Connection()
    conexao.faz_conexao()
    conexao.verificar_operador_de_consultas()
    cursor = conexao.cursor()
    
    #Alterações na tabela
    inserir_dados_query = """
    INSERT INTO produtos (nome, preco) VALUES (%s, %s);
    """
    dados_produto = ("Produto 1", 10.99)
    cursor.execute(inserir_dados_query, dados_produto)
    conexao.commit()
    
    
    