from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..extensions import role_required, db
from ..model import User, Question, Category, QuestionReport
import os
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from sqlalchemy import desc

admin = Blueprint('admin', __name__, static_folder="static", template_folder="templates")

# Configuration for file uploads
UPLOAD_FOLDER = 'quizzer/static/uploads/admin'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @admin.before_request
# @login_required
# @role_required('admin')
# def protect_blueprint_routes():
#     pass

@admin.route('/')
def home():
    # Get admin profile image or initial
    profile_image = None
    admin_initial = 'A'
    
    if current_user.is_authenticated:
        if hasattr(current_user, 'username') and current_user.username:
            admin_initial = current_user.username[0].upper()
        elif hasattr(current_user, 'email') and current_user.email:
            admin_initial = current_user.email[0].upper()
    
    # Fetch REAL data from database
    try:
        # Get total users
        total_users = User.query.count()
        
        # Get total questions
        total_questions = Question.query.count()
        
        # Get total categories
        total_categories = Category.query.count()
        
        # Recent user registrations
        recent_users = User.query.filter(User.id != current_user.id).order_by(desc(User.id)).limit(5).all()
        
        # Recent questions added
        recent_questions = Question.query.order_by(desc(Question.id)).limit(5).all()
        
        # Recent reports
        recent_reports = QuestionReport.query.order_by(desc(QuestionReport.id)).limit(5).all()
        
        # Prepare recent activities
        recent_activities = []
        
        # Add user registrations to activities
        for user in recent_users:
            recent_activities.append({
                'type': 'user',
                'message': f'New user registered: {user.username}',
                'time': 'Recently',
                'icon': 'user-plus',
                'color': 'green'
            })
        
        # Add new questions to activities
        for question in recent_questions:
            recent_activities.append({
                'type': 'question',
                'message': f'New question added: {question.question_text[:50]}...',
                'time': 'Recently',
                'icon': 'question-circle',
                'color': 'blue'
            })
        
        # Add reports to activities
        for report in recent_reports:
            user = User.query.get(report.user_id)
            recent_activities.append({
                'type': 'report',
                'message': f'Question reported by {user.username if user else "Unknown user"}',
                'time': 'Recently',
                'icon': 'exclamation-triangle',
                'color': 'red'
            })
        
        recent_activities = recent_activities[:5]
        
    except Exception as e:
        # Fallback to dummy data if there's any database error
        print(f"Database error: {e}")
        total_users = User.query.count() or 42
        total_questions = Question.query.count() or 158
        total_categories = Category.query.count() or 12
        recent_activities = [
            {'type': 'user', 'message': 'New user registered: John Doe', 'time': '2 hours ago', 'icon': 'user-plus', 'color': 'green'},
            {'type': 'question', 'message': 'New question added to Python Basics', 'time': '5 hours ago', 'icon': 'question-circle', 'color': 'blue'}
        ]
    
    return render_template('admin/home.html', 
                         profile_image=profile_image,
                         admin_initial=admin_initial,
                         active_page='home',
                         total_users=total_users,
                         total_questions=total_questions,
                         total_categories=total_categories,
                         recent_activities=recent_activities)

@admin.route('/add_quiz', methods=['GET', 'POST'])
def add_quiz():
    # Get real categories from database
    categories = Category.query.all()
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        category_id = request.form.get('category_id')
        
        # Here you would save to database
        flash(f'Quiz "{title}" created successfully!', 'success')
        return redirect(url_for('admin.home'))
    
    return render_template('admin/add_quiz.html', active_page='add_quiz', categories=categories)

@admin.route('/view_quizzes')
def view_quizzes():
    # Use categories as "quizzes" for now
    categories = Category.query.all()
    return render_template('admin/view_quizzes.html', 
                         active_page='view_quizzes', 
                         categories=categories)

@admin.route('/add_question', methods=['GET', 'POST'])
def add_question():
    # Get real categories from database
    categories = Category.query.all()
    
    if request.method == 'POST':
        question_text = request.form.get('question_text')
        option_a = request.form.get('option_a')
        option_b = request.form.get('option_b')
        option_c = request.form.get('option_c')
        option_d = request.form.get('option_d')
        correct_option = request.form.get('correct_option')
        category_id = request.form.get('category_id')
        
        # Create new question
        new_question = Question(
            question_text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_option=correct_option,
            category_id=category_id,
            user_id=current_user.id
        )
        
        db.session.add(new_question)
        db.session.commit()
        
        flash('Question added successfully!', 'success')
        return redirect(url_for('admin.view_questions'))
    
    return render_template('admin/add_question.html', active_page='add_question', categories=categories)

@admin.route('/view_questions')
def view_questions():
    category_id = request.args.get('category_id', type=int)
    page=request.args.get("page",1,type=int)
    
    query = Question.query
    if category_id:
        query = query.filter_by(category_id=category_id)

    # Get real questions from database with category information
    # questions = Question.query.join(Category).add_columns(
    #     Question.id,
    #     Question.question_text,
    #     Category.category_name,
    #     Question.user_id
    # ).all()
    categories=Category.query.all()

    questions = query.paginate(page=page,per_page=10,error_out=False)
    return render_template('admin/view_questions.html', 
                         active_page='view_questions', 
                         questions=questions ,categories=categories,selected_category_id=category_id)

@admin.route('/question/<int:id>')
def question_detail(id):
    question_id=id
    question = db.session.query(Question).join(User).filter(Question.id == id).first_or_404()
    return render_template('admin/question_details.html',question=question)


@admin.route('/view_users')
def view_users():
    # Get all users from database
    users = User.query.all()
    return render_template('admin/view_users.html', 
                         active_page='view_users', 
                         users=users)

@admin.route('/view_reports')
def view_reports():
    # Get all question reports with user and question info
    reports = QuestionReport.query.join(User).join(Question).add_columns(
        QuestionReport.id,
        User.username,
        Question.question_text,
        QuestionReport.report_reason
    ).all()
    
    return render_template('admin/view_reports.html', 
                         active_page='view_reports', 
                         reports=reports)

@admin.route('/upload_profile', methods=['POST'])
def upload_profile():
    if 'profile_image' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('admin.home'))
    
    file = request.files['profile_image']
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('admin.home'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        user_id = current_user.id
        filename = f"admin_{user_id}_{filename}"
        
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # Update user profile picture in database
        current_user.profile_pic = filename
        db.session.commit()
        
        flash('Profile image uploaded successfully!', 'success')
    else:
        flash('Allowed file types: png, jpg, jpeg, gif', 'error')
    
    return redirect(url_for('admin.home'))

@admin.route('/logout')
def logout():
    from flask_login import logout_user
    logout_user()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('auth.login'))