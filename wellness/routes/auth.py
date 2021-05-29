from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
#from wellness.extensions import db
from wellness.models import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        unhashed_password = request.form['password']

        user = User(
            name=name, 
            unhashed_password=unhashed_password,
            admin=False,  
            expert=False
        )

        #db.session.add(user)
        #db.session.commit()

        return redirect(url_for('auth.login'))

    kwargs = {
        'title': 'Register',
        'jumbotron': {
            "header": "Sign up for an account!",
            "text": "Act now for your wellness. "
        },
        'registerPageContents': [{
            'Title': "Register"
        },

        ]
    }
    return render_template('register.html', **kwargs)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()

        error_message = ''

        if not user or not check_password_hash(user.password, password):
            error_message = 'Could not login. Please check and try again.'

        if not error_message:
            login_user(user)
            return redirect(url_for('main.index'))
    kwargs = {
        'title': 'Login',
        'jumbotron': {
            "header": "Log into your account!",
            "text": "Act now for your wellness. "
        },
        'loginPageContents': [{
            'Title': "Login"
        },

        ]
    }
    return render_template('login.html', **kwargs)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))