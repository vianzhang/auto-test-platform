#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    :author: WENHAO ZHANG
"""
import hashlib
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from autotest.extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String(128))
    email = db.Column(db.String(254), unique=True, nullable=False)
    nick_name = db.Column(db.String(30))
    password_hash = db.Column(db.String(128))
    email_hash = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    state = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.generate_email_hash()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_email_hash(self):
        if self.email is not None and self.email_hash is None:
            self.email_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()

    @property
    def is_admin(self):
        return self.email == current_app.config['ADMIN_EMAIL']


class Guest(AnonymousUserMixin):

    @property
    def is_admin(self):
        return False


login_manager.anonymous_user = Guest


