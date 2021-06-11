from flask import Flask, render_template
from flask import url_for
from commands import create_tables
from extensions import db, login_manager
from models import User
from routes.auth import auth
from routes.main import main
from routes.about import about_page
from routes.activity import activity_page
from routes.evidence import evidence_page
from routes.community import community_page
from routes.progress import progress_page


config_file = 'settings.py'
app = Flask(__name__)
app.config.from_pyfile(config_file)
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(main)
app.register_blueprint(auth)

app.cli.add_command(create_tables)
app.register_blueprint(about_page)
app.register_blueprint(activity_page)
app.register_blueprint(evidence_page)
app.register_blueprint(community_page)
app.register_blueprint(progress_page)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)