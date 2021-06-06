from flask import Flask, render_template
from commands import create_tables
from extensions import db, login_manager
from routes.about import about_page
from routes.activity import activity_page
from routes.evidence import evidence_page
from routes.community import community_page
import public
import user

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errorhandlers(app)
    return app

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    return None

def register_blueprints(app):
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(about_page)
    app.register_blueprint(activity_page)
    app.register_blueprint(evidence_page)
    app.register_blueprint(community_page)
    return None

def register_commands(app):
    app.cli.add_command(create_tables)

def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template(f"{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

if __name__ == '__main__':
    app=create_app()
    app.run(threaded=True, port=5000)