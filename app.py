from bd import mysql
import json
from flask import jsonify, session
from flaskext.mysql import MySQL
from flask import Flask, render_template, request, redirect, url_for        #Ao instalar a biblioteca do flask importaremos o Flask dessa biblioteca.
app = Flask(__name__)                                                       #Para criar se site.

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:Ju1031&68@127.0.0.1/bdtrab'
db = SQLAlchemy(app)

#Criando a primeira pagina do site:
    #Toda pagina tem que ter um "Rout" e uma "Função":
        #Rout   -> é a rota/caminho para acessar seu site pela URL e assim interagir com seu projeto
        #Função -> é o que vc quer exibir na tela


@app.route('/')                                                     #Criando o Rout
def homepage():                                                     #Criando a Função
    return render_template("homepage.html")
    


@app.route('/Login')                                                #Criando o Rout
def homepageLogin():                                                #Criando a Função
    return render_template("login.html")


@app.route('/Create')                                               #Criando o Rout
def homepageRegister():                                             #Criando a Função
    return render_template("create.html")



#______________________________________________________________________________________________________________________
@app.route('/', methods=['POST', 'GET'])
def adicionar_usuario():

    if request.method=='POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        senha = request.form['password']


        if(nome and cpf and email and senha):
            with mysql.cursor() as cur:
                cur.execute('INSERT INTO pessoa (Nome, Email, CPF, Senha) VALUES (%s,%s,%s,%s)', (nome, email, cpf, senha))
                cur.connection.commit()

                return redirect(url_for('usuarios', nome_usuario=nome))
        else:
            return render_template("create.html")

    return render_template("create.html")
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
@app.route('/verificar', methods=['POST', 'GET'])
def verificar_usuario():

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']

        try:
            with mysql.cursor() as cur:
                comando = "SELECT Email, Nome, Senha FROM pessoa WHERE Email = %s;"
                cur.execute(comando, email)
                resultado = cur.fetchall()
                print(resultado)
                if resultado[0][0] != None:
                    if resultado[0][2] != senha:
                        return render_template("login.html")
                    else:
                        session['nome_usuario'] = resultado[0][1]
                        return redirect(url_for('usuarios', nome_usuario=resultado[0][1]))

        except Exception as e:
            return render_template("login.html")

#______________________________________________________________________________________________________________________

app.secret_key = 'alguma_chave_secreta'

#______________________________________________________________________________________________________________________
@app.route('/contas', methods=['POST', 'GET'])
def contas():

    if request.method == 'POST':
        cpf = request.form['cpf']
        nconta = request.form['nomeconta']
        valor = request.form['quantity']
        dat = request.form['data']

        with mysql.cursor() as cur:
            cur.execute('INSERT INTO contas (C_Cpf, Nome_Conta, valor, Data_Vencimento) VALUES (%s,%s,%s,%s)', (cpf, nconta, valor, dat))
            cur.connection.commit()



        with mysql.cursor() as cur:
            comando = "SELECT P.CPF, C.C_Cpf, P.Nome, C.Nome_Conta, C.Valor, C.Data_Vencimento FROM	pessoa P, contas C WHERE	P.CPF = C.C_Cpf and C_Cpf = %s and Nome_Conta = %s;"
            cur.execute(comando, (cpf, nconta))
            resultado = cur.fetchall()
            print(resultado)
            if (resultado[0][0] == resultado[0][1]):
                Conta = resultado[0][3]
                Valor = resultado[0][4]
                Data = resultado[0][5]
                url = url_for('tabelas', nome_usuario=resultado[0][2], conta=Conta, valor=Valor, data=Data)
                return redirect(url)
            else:
                return redirect(url_for('tabelas', nome_usuario=resultado[0][2]))

#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
@app.route('/apagar', methods=['POST', 'GET'])
def apagar():

    if request.method == 'POST':
        cpf = request.form['cpf']
        nconta = request.form['nomeconta']

        try:
            with mysql.cursor() as cur:

                comando1 = "SELECT P.CPF, C.C_Cpf, P.Nome FROM	pessoa P, contas C WHERE	P.CPF = C.C_Cpf and C_Cpf = %s and Nome_Conta = %s;"
                cur.execute(comando1, (cpf, nconta))
                resultado = cur.fetchall()
                print(resultado)

                comando2 = "DELETE FROM contas WHERE Nome_Conta = %s AND C_cpf = %s;"
                cur.execute(comando2, (nconta, cpf))
                cur.connection.commit()

                return redirect(url_for('tabelas', nome_usuario=resultado[0][2]))

        except Exception as e:
            return render_template("ctabela.html")
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
@app.route('/salario', methods=['POST', 'GET'])
def salario():

    gasto = 0

    if request.method == 'POST':
        cpf = request.form['cpf']
        valor = request.form['quantity']

        with mysql.cursor() as cur:
            comando1 = 'UPDATE pessoa SET Salario = %s WHERE CPF = %s;'
            cur.execute(comando1, (valor, cpf))
            cur.connection.commit()

            comando2 = "SELECT Nome From pessoa WHERE CPF = %s"
            cur.execute(comando2, cpf)
            resultado1 = cur.fetchall()
            print(resultado1)

            comando3 = "SELECT	P.Salario, C.Valor FROM	pessoa P, contas C WHERE	CPF = C_cpf and CPF = %s;"
            cur.execute(comando3, cpf)
            resultado2 = cur.fetchall()

            for i in range(0, len(resultado2)):
                gasto = gasto + resultado2[i][1]

            print(resultado1)
            url = url_for('graficos', nome_usuario=resultado1[0][0], salario=resultado2[0][0], gasto=gasto)
            return redirect(url)
#______________________________________________________________________________________________________________________
        
@app.route('/usuario/<nome_usuario>/salva_salario', methods=['POST'])
def salva_salario(nome_usuario):
    result = None
    print("Teste")
    print(nome_usuario)
    dados_tabela = request.json['table']
    print(dados_tabela)
    
    with mysql.cursor() as cur:
        print("Teste2222")
        cur.execute('Select cpf FROM pessoa WHERE nome = %s', nome_usuario)
        print("Teste2222")
        result = cur.fetchone() 
        print("Teste2222")
        if result:
            cpf_do_usuario = result[0]
            print("CPF")
            print(cpf_do_usuario)
            query = f'Update pessoa SET Salario = {dados_tabela} where Cpf = "{cpf_do_usuario}"'
            cur.execute(query)
            cur.connection.commit()
        else:
            print("Usuário não encontrado.")
            

@app.route('/usuario/<nome_usuario>/monta_grafico', methods=['GET'])
def monta_grafico(nome_usuario):
    with mysql.cursor() as cur:
        cur.execute('Select cpf FROM pessoa WHERE nome = %s', nome_usuario)
    result = cur.fetchone()  
    if result:
        cpf_do_usuario = result[0]
    else:
        print("Usuário não encontrado.")
        
    with mysql.cursor() as cur:
        cur.execute('Select p1.Salario, c2.valor  FROM pessoa p1 Join contas c2 on p1.cpf = c2.c_cpf where c2.c_cpf = %s', cpf_do_usuario)
        resultado = cur.fetchall()
         
    return jsonify(resultado)

#______________________________________________________________________________________________________________________
@app.route('/usuario/<nome_usuario>/mostrar_tabelas', methods=['GET'])
def mostrar_tabelas(nome_usuario):
    with mysql.cursor() as cur:
        cur.execute('Select cpf FROM pessoa WHERE nome = %s', nome_usuario)
    result = cur.fetchone()  
    if result:
        cpf_do_usuario = result[0]
    else:
        print("Usuário não encontrado.")
        
    with mysql.cursor() as cur:
        cur.execute('Select *  FROM Contas where C_cpf = %s', cpf_do_usuario)
        result = cur.fetchall()
         
    return jsonify(result)

@app.route('/usuario/<nome_usuario>/deleta_conta', methods=['POST'])
def deleta_conta(nome_usuario):
    dados_tabela = request.json['tabela']
    json_tabela = json.dumps(dados_tabela)
    
    with mysql.cursor() as cur:
        cur.execute('Select cpf FROM pessoa WHERE nome = %s', nome_usuario)
    
    result = cur.fetchone()
    if result:
        cpf_do_usuario = result[0]
    else:
        print("Usuário não encontrado.")
        
    # Remover dados da tabela Conta
    with mysql.cursor() as cur:
        cur.execute('Delete FROM contas Where C_cpf = %s and Nome_conta = %s', (cpf_do_usuario, dados_tabela[1]))
        cur.connection.commit()

    return jsonify(success=True)

@app.route('/usuario/<nome_usuario>/salvar_tabela', methods=['POST'])
def salvar_tabela(nome_usuario):
    dados_tabela = request.json['tabela']
    json_tabela = json.dumps(dados_tabela)
    
    with mysql.cursor() as cur:
        cur.execute('Select cpf FROM pessoa WHERE nome = %s', dados_tabela['nome_usuario'])
        print(dados_tabela['nome_usuario'])
        print( dados_tabela['conta'])
    result = cur.fetchone()
    if result:
        cpf_do_usuario = result[0]
    else:
        print("Usuário não encontrado.")

    # Salvar os dados_tabela no banco de dados para o nome_usuario
    with mysql.cursor() as cur:
        cur.execute('Insert into contas(c_cpf, Nome_Conta, valor, Data_Vencimento) Values(%s, %s, %s, %s)', (cpf_do_usuario, dados_tabela['conta'], dados_tabela['valor'], dados_tabela['data_vencimento']))
        cur.connection.commit()

    return jsonify(success=True)


@app.route('/usuario/<nome_usuario>/carregar_tabela', methods=['GET'])
def carregar_tabela(nome_usuario):
    # Carregar a tabela do banco de dados para o nome_usuario
    with mysql.cursor() as cur:
        cur.execute('SELECT dados_tabela FROM user_tables WHERE nome_usuario = %s', (nome_usuario,))
        resultado = cur.fetchone()
        if resultado:
            dados_tabela = json.loads(resultado[0])
        else:
            dados_tabela = [] # Ou qualquer valor padrão

    return jsonify(tabela=dados_tabela)






@app.route('/usuario/<nome_usuario>/ctabela')
def tabelas(nome_usuario):
    return render_template("Ctabela.html", nome=nome_usuario)


@app.route('/usuario/<nome_usuario>/cgrafico')                              #Criando o Rout
def graficos(nome_usuario):                                                 #Criando a Função
    return render_template("cgrafico.html", nome=nome_usuario)


@app.route('/usuario/')
@app.route('/usuario/<nome_usuario>')   # Para a página de usuários
def usuarios(nome_usuario=None):
    return render_template("usuarios.html", nome=nome_usuario)

@app.route('/SobreNos/<nome_usuario>') # Para a página "Sobre nós" com nome do usuário
def sobre_nos_usuario(nome_usuario):
    return render_template("SobreNos.html", nome=nome_usuario)


@app.route('/SobreNos')  # Para a página "Sobre nós"
def sobre_nos():
    nome_usuario = session.get('nome_usuario')
    return render_template("SobreNos.html", nome=nome_usuario)


#Colocando o site no ar
if(__name__ == "__main__"):
    app.run(debug = True)


class UserTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('pessoa.CPF'))
    table_data = db.Column(db.Text)

    def __init__(self, user_id, table_data):
        self.user_id = user_id
        self.table_data = table_data

db.create_all()


@app.route('/save_table', methods=['POST'])
def save_table():
    user_id = request.form['user_id']
    table_data = json.dumps(request.form['table_data'])

    user_table = UserTable(user_id, table_data)
    db.session.add(user_table)
    db.session.commit()

    return jsonify(status='success')


@app.route('/load_table', methods=['GET'])
def load_table():
    user_id = request.args.get('user_id')

    user_table = UserTable.query.filter_by(user_id=user_id).first()
    table_data = json.loads(user_table.table_data)

    return jsonify(table_data=table_data)
