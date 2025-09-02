from flask import Blueprint,render_template
from flask_login import login_required
from ..extensions import role_required

admin=Blueprint('admin',__name__, static_folder="static",template_folder="templates")

@admin.before_request
@login_required
@role_required('admin')
def protect_blueprint_routes():
    pass


@admin.route('/')
def home():
    return render_template('admin/home.html')


@admin.route('/question')
def question():
    return "this is question"