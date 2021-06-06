# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user

from extensions import login_manager
from public.forms import LoginForm
from user.forms import RegisterForm
from user.models import User
from utils import flash_errors

blueprint = Blueprint('public', __name__, template_folder='templates')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))

@blueprint.route("/", methods=["GET", "POST"])
def home():

    kwargs = {
        'title': 'Home',
        'jumbotron': {
            "header": "Welcome to 8D Wellness Club!",
            # To choose bg images
            "bg_image": url_for('static', filename='/images/'),
            "text": "Act now for your wellness. "
        },
        'homePageContents': [{
            'Title': "What is wellness",
            "Text": "Wellness is a state beyond absence of illness but rather aims to optimize well-being.The notions behind the term share the same roots as the alternative medicine movement, in 19th-century movements in the US and Europe that sought to optimize health and to consider the whole person, like New Thought, Christian Science, and Lebensreform.The term wellness has also been misused for pseudoscientific health interventions.[4]",
            "imagePath": url_for('static', filename='/images/Eight_Dimensions_of_Wellness.png'),
            "Link": "/styletransfer",
            "Action": "+ The science behind it"
        },

        ]
    }

    form = LoginForm(request.form)
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("home.html", form=form, **kwargs)

@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.home"))


@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""

    kwargs = {
        'title': 'Register',
        'jumbotron': {
            "header": "mHealth & Human",
            "text": ""
        },
        'registerPageContents': [{
            'Title': "Responsibility when providing health related content online",
            "Text": " "

        },
            {
            "Title": "Aware: technology is only small part in health care system, human play much larger role in health care procedure",
            "Text": " "

        },
            {
            "Title": "Be patient, it takes time!",
            "Text": ""

        }
        ]
    }
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("register.html", form=form, **kwargs)