from flask import render_template,Blueprint

community_page = Blueprint('community',__name__,template_folder='templates')
@community_page.route('/community',methods=['GET','POST'])

def default_activity_page():
    kwargs = {
        'title': 'Community',
        'jumbotron': {
            "header": "You are not alone.",
            "bg_image": "",
            "text": ""
        },
        'communityPageContents': [{
            'Title': "Forum",
            "Text": " "

        },
            {
            "Title": "Social Media",
            "Text": " "

        },
            {
            "Title": "Other",
            "Text": ""

        }
        ]
    }
    return render_template('community.html', **kwargs)    
