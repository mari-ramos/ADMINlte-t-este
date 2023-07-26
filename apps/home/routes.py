# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index') 
@login_required
def index(): #rota para a página inicial do aplicativo. É decorada com @login_required, o que significa que o usuário deve estar autenticado para acessar essa página. A função renderiza o template 'home/index.html' e passa um contexto 'segment' com valor 'index'.

    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
@login_required
def route_template(template): #Esta função é uma rota genérica para renderizar templates dentro do diretório 'templates/home/'

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request): #função auxiliar para obter o nome da página atual a partir do objeto request do Flask.
                          #Ela extrai o nome da página da parte final da URL e retorna 'index' se a URL for vazia. Essa função é usada internamente na função route_template() para determinar o valor do contexto 'segment'.
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
