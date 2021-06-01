from flask import render_template,Blueprint

evidence_page = Blueprint('evidence',__name__,template_folder='templates')
@evidence_page.route('/evidence',methods=['GET','POST'])

def default_activity_page():
    kwargs = {
        'title': 'Evidence',
        'jumbotron': {
            "header": "The science behind Wellness",
            "bg_image": "",
            "text": ""
        },
        'evidencePageContents': [{
            'Title': "Physical",
            "Text": " "

        },
            {
            "Title": "Emotional",
            "Text": " "

        },
            {
            "Title": "Social",
            "Text": ""

        },
            {
            "Title": "Occupational",
            "Text": ""

        },
        {
            "Title": "Intellectual",
            "Text": ""

        }
        ,
            {
            "Title": "Environment",
            "Text": ""

        },
            {
            "Title": "Financial",
            "Text": ""

        },
        {
            "Title": "Spiritual",
            "Text": ""

        }
        ]
    }
    return render_template('evidence.html', **kwargs)    
