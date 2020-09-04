#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    :author: WENHAO ZHANG
"""

import os
import click
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFError
from .settings import config
from .extensions import db, login_manager, csrf, moment, oauth
from .blueprints.auth import auth_bp
from .blueprints.main import main_bp
from .blueprints.api import api_bp
from flask_login import current_user
import re


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('auto_test')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_errors(app)
    register_commands(app)
    register_request_security(app)

    return app


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    moment.init_app(app)
    oauth.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('error.html', description=e.description, code=e.code), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', description=e.description, code=e.code), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('error.html', description=e.description, code=e.code), 500

    @app.errorhandler(CSRFError)
    def handler_crsf_error(e):
        return render_template('error.html', description=e.description, code=e.code), 400


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop')
    def initdb(drop):
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')


# 请求URL控制拦截器
def register_request_security(app):
    @app.before_request
    def check_login():
        path = request.path
        ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
        pattern = re.compile('{}'.format('|'.join(ignore_check_login_urls)))
        if pattern.match(path):
            return None
        else:
            if current_user.is_authenticated:
                return None
            else:
                return redirect(url_for('auth.login'))


