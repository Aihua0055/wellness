from flask import render_template,Blueprint

progress_page = Blueprint('progress',__name__,template_folder='templates')
@progress_page.route('/progress',methods=['GET','POST'])

def default_progress_page():
    kwargs = {
        'title': 'Progress',
        'jumbotron': {
            "header": "Make a progress",
            "bg_image": "static/images/1182_650_gallery.jpeg",
            "text": ""
        }
    }
    return render_template('progress.html', **kwargs)    
