# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os #acessa funcionalidades do sistema operacional
from   flask_migrate import Migrate #permite realizar migrações de banco de dados usando o Flask e o SQLAlchemy.
from   flask_minify  import Minify #extensão que permite compactar (minificar) os arquivos HTML, JavaScript e CSS para melhorar o desempenho do aplicativo.
from   sys import exit #Usado para sair do programa se ocorrer algum erro.

from apps.config import config_dict #importa dicionario para atuar nas configurações do aplicativo para diferentes modos (Debug e Production)
from apps import create_app, db

# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True') #permite que você escolha se deseja executar o aplicativo em modo de depuração ou produção.

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db) #configura a migração do banco de dados. útil para gerenciar as alterações no esquema do banco de dados à medida que o projeto evolui.

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False) # em modo produção -> compacta os arquivos HTML.
    
if DEBUG: #em modo de depuração, ele registra algumas informações no log, como o valor de DEBUG e a configuração do banco de dados.
    app.logger.info('DEBUG            = ' + str(DEBUG)             )
    app.logger.info('Page Compression = ' + 'FALSE' if DEBUG else 'TRUE' )
    app.logger.info('DBMS             = ' + app_config.SQLALCHEMY_DATABASE_URI)
#bota pra rodar -> verifica se o arquivo está sendo executado diretamente como um script 
if __name__ == "__main__":
    app.run() #se sim, inicia o servidor Flask com o comando app.run().
