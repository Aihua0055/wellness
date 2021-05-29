from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from .extensions import db
#from ..models import Question, User

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    # Kwargs store data to render on template
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
    return render_template('home.html', **kwargs)

@main.route('/about')
def about():
    kwargs = {
        'title': 'About',
        'jumbotron': {
            "header": "mHealth & Human",
            "bg_image": "static/images/1182_650_gallery.jpeg",
            "text": ""
        },
        'aboutPageContents': [{
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
    return render_template('about.html', **kwargs)