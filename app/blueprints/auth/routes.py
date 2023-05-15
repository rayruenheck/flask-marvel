from flask import render_template, url_for,flash,redirect
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User
from app import db

from . import bp
from app.forms import RegisterForm, LoginForm



@bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u = User(username=form.username.data, email=form.email.data, )
            u.password = u.hash_password(form.password.data)
            u.add_token()
            u.commit()
            
            flash(f"{form.username.data} registered", 'success')
            return redirect(url_for("main.home"))
        if user:
            flash(f'{form.username.data} already taken, try again', 'warning')
        
        else:
            flash(f'{form.email.data} already taken, try again', 'warning')

    return render_template('register.j2', title='register', form=form)

@bp.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@bp.route('/signin', methods=['GET','POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash(f'{form.username.data} has Entered!', 'success')
            login_user(user)
            return redirect(url_for('main.home'))
    return render_template('signin.j2', title='Sign In', form=form)