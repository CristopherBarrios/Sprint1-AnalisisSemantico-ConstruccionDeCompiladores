##################################
# Cristopher Barrios
# COMPILADORES 
##################################
# gui.py
##################################

from flask import Flask, render_template, request, session
from antlr4 import *
import antlr4
from antlr4.error.ErrorListener import ErrorListener
from YAPL.YAPLLexer import YAPLLexer
from YAPL.YAPLListener import YAPLListener
from YAPL.YAPLParser import YAPLParser
from antlr4.tree.Trees import Trees
from YAPL.YAPLVisitor import YAPLVisitor
import backend.visitor as Visitor
import backend.listener as Listener
from backend.custom_error import CustomErrorListener
from graphviz import Digraph
import shutil
import sys
import os


app  = Flask(__name__)
app.secret_key = "compis:D"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0







def cleaner():
    output_folder = "output" #nombre de la carpeta
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    # Crea la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)
    return output_folder


def graphner(output_folder,Grafic):
    output_path = os.path.join(output_folder, "tree.png")
    dot_data = Grafic.pipe(format='png')
    with open(output_path, 'wb') as file:
        file.write(dot_data)
    print("")
    print("======================")
    print("Se creo .png del arbol")
    print("======================")
    print("")

# inicio
print("start everything")
output_folder = cleaner()


@app.route('/')
def home():
    errors = []
    return render_template("home.html")


@app.route('/', methods = ["POST"])
def get_code():

    errors = []
    code = ""
    code = request.form["codigo"]
    session.code = code
    print("")
    if code!= " ":
        
        text = antlr4.InputStream(code)
        lexer = YAPLLexer(text)
        stream = CommonTokenStream(lexer)
        parser = YAPLParser(stream)

        # Registra el error listener personalizado
        error_listener = CustomErrorListener()
        errors = parser.addErrorListener(error_listener)

        # Ejecuta el parser para obtener el árbol sintáctico
        tree = parser.program()
        print("")
        print("______________________________________________________________________________________________________________________________________________________________")
        print(tree.toStringTree(recog=parser))
        print("______________________________________________________________________________________________________________________________________________________________")
        print("")

        listenator = Listener.MyYAPLListener()
        walker = ParseTreeWalker()
        walker.walk(listenator, tree)
        table = listenator.getTable()

        Grafic = Digraph()
        def nod(node, parent=None):
            if isinstance(node, ParserRuleContext):
                label = parser.ruleNames[node.getRuleIndex()]
            else:
                label = str(node)
            Grafic.node(str(id(node)), label=label)
            if parent is not None:
                    Grafic.edge(str(id(parent)), str(id(node)))
            if isinstance(node, ParserRuleContext) and node.children is not None:
                for child in node.children:
                    nod(child,parent=node)
        nod(tree)

        #Crear png de la Grafica
        graphner(output_folder,Grafic)



        visitonator = Visitor.MyYAPLVisitor(table)
        visitonator.visit(tree)
        errors = visitonator.ERRORS

        listen = listenator.ERRORS
        errors += listen
        SyntaxErrors = error_listener.ERRORS
        errors += SyntaxErrors

    else:
        errors = []
    return render_template("home.html", errors = errors, code = code)


@app.route('/tree.html')
def tree_page():
    return render_template('tree.html')




if __name__ == "__main__":
    app.run(host='localhost', port = 5000, debug = True)