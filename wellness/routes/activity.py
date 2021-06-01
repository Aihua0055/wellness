from flask import render_template,Blueprint

activity_page = Blueprint('activity',__name__,template_folder='templates')
@activity_page.route('/activity',methods=['GET','POST'])

def default_activity_page():
    kwargs = {
        'title': 'Activity',
        'jumbotron': {
            "header": "Act NOW",
            "bg_image": "static/images/1182_650_gallery.jpeg",
            "text": ""
        },
        'activityPageContents': [{
            'Title': "Daily Activity",
            "Text": " "

        },
            {
            "Title": "Weekly Activity",
            "Text": " "

        },
            {
            "Title": "Monthly Activity",
            "Text": ""

        }
        ]
    }
    return render_template('activity.html', **kwargs)    
