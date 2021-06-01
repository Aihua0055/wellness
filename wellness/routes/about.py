from flask import render_template,Blueprint

about_page = Blueprint('about',__name__,template_folder='templates')
@about_page.route('/about',methods=['GET','POST'])

def default_about_page():
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
