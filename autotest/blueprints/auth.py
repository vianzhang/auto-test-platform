#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    :author: WENHAO ZHANG
"""

from flask import render_template, flash, redirect, url_for, Blueprint, request, session
from flask_login import login_user, logout_user, login_required, current_user
from ..extensions import db
from ..models import User


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember_me = request.form.get('remember', False)

        if remember_me:
            remember_me = True

        user = User.query.filter_by(email=email).first()

        if user is not None:
            if user.password_hash is None:
                flash('用户名或密码错误')
                return redirect(url_for('.login'))

            if user.verify_password(password):
                login_user(user, remember_me)
                session['nick_name'] = user.nick_name
                return redirect(url_for('main.home'))
            flash('用户名或密码错误')
            return redirect(url_for('.login'))
        else:
            flash('用户名或密码错误')

    return render_template('auth/login.html')


@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    session.pop('nick_name')
    logout_user()
    return redirect(url_for('.login'))


@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        email = request.form['email'].lower()
        user = User.query.filter_by(email=email).first()
        if user is not None:
            flash('The email is already registered, please log in.')
            return redirect(url_for('.login'))
        nick_name = request.form['nickname']
        password = request.form['password']
        user = User(nick_name=nick_name, email=email)
        user.set_password(password)
        user.state = 0
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        session['nick_name'] = user.nick_name
        return redirect(url_for('main.home'))

    return render_template('auth/register.html')

