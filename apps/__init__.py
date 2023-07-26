# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
#arquivo principal do flask
import os #os -> acessar funcionalidades do sistema operacional

from flask import Flask #flask -> classe principal do Flask, usada para criar o aplicativo web.
from flask_login import LoginManager # extensão do Flask que gerencia a autenticação e o login dos usuários.
from flask_sqlalchemy import SQLAlchemy #ornece suporte a banco de dados e permite interações com o banco de dados usando o SQLAlchemy ORM
from importlib import import_module #É uma função do Python que permite importar módulos dinamicamente, com base em nomes de strings.


db = SQLAlchemy() # Objeto da classe SQLAlchemy, usado para interagir com o banco de dados.
login_manager = LoginManager() #Objeto da classe LoginManager, responsável pela gerência de autenticação de usuários.


def register_extensions(app): # Registra as extensões db e login_manager no aplicativo Flask app.
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app): # Registra os blueprints (rotas) das partes "authentication" e "home" no aplicativo Flask app.
    for module_name in ('authentication', 'home'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app): #Configura o banco de dados.

    @app.before_first_request #cria as tabelas do banco de dados antes da primeira requisição ao aplicativo.
    def initialize_database(): #Se ocorrer um erro ao criar as tabelas do banco de dados (por exemplo, 
                               #se o banco de dados não estiver configurado corretamente), ele irá criar um banco de dados SQLite como fallback
        try:
            db.create_all()
        except Exception as e:

            print('> Error: DBMS Exception: ' + str(e) )

            # fallback to SQLite
            basedir = os.path.abspath(os.path.dirname(__file__))
            app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')

            print('> Fallback to SQLite ')
            db.create_all()

    @app.teardown_request #encerra a sessão do banco de dados após cada requisição.
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config): #função principal do aplicativo Flask
    app = Flask(__name__)
    app.config.from_object(config) #Ela cria uma instância do aplicativo Flask e aplica as configurações definidas no objeto config. 
                                   #Em seguida, chama as funções de registro e configuração para adicionar extensões e rotas ao aplicativo. 
                                   # Por fim, retorna o objeto app para que possa ser executado.
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app
