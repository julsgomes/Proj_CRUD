import psycopg2

class Connection:
    def faz_conexao(self):
        self = psycopg2.connect(
            host = "",
            database = "",
            user = "",
            password = ""
        )
        
    def verificar_operador_de_consultas(self):
        cursor = self.cursor()
        
        #verificar existencia de tabelas
        criar_tabela_query = """
        CREATE TABLE IF NOT EXISTS Usuario (
            email NOT NULL PRIMARY KEY,
            nome VARCHAR NOT NULL,
        );
        """
        cursor.execute(criar_tabela_query)
        #aplicar mudança
        self.commit()

