from flask import Flask, render_template        #Ao instalar a biblioteca do flask importaremos o Flask dessa biblioteca.
app = Flask(__name__)                           #Para criar se site.



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


@app.route("/usuario/<nome_usuario>")                               #Criando o Rout
def usuarios(nome_usuario):                                         #Criando a Função
    return render_template("usuarios.html", nome=nome_usuario)


#Colocando o site no ar
if(__name__ == "__main__"):
    app.run(debug = True)