import datetime
import random

from flask import Blueprint, render_template, session, redirect, flash, url_for

from app.extentions import sms_api, db
from app.users.forms import UserRegistrationForm, UserCodeVerifyForm
from app.users.models import Code, User

blueprint = Blueprint('users', __name__)


@blueprint.route('/register', methods=['post', 'get'])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        rand_num = random.randint(10000, 99999)
        session['user_phone'] = form.phone.data
        params = {
            'sender': '',
            'receptor': int(form.phone.data),
            'message': rand_num
        }
        sms_api.sms_send(params)
        code = Code(
            number=rand_num,
            expire=datetime.datetime.now() + datetime.timedelta(minutes=10),
            phone=form.phone.data
        )
        db.session.add(code)
        db.session.commit()
        return redirect(url_for('users.verify'))
    return render_template('users/register.html', form=form)


@blueprint.route('/verify', methods=['post', 'get'])
def verify():
    user_phone = session.get('user_phone')
    code = Code.query.filter_by(phone=user_phone).first()
    form = UserCodeVerifyForm()
    if form.validate_on_submit():
        if code.expire < datetime.datetime.now():
            flash('Expiration Error, Please try again', 'warning')
            return redirect('users.register')
        if form.code.data != str(code.number):
            flash('your code is wrong', 'danger')
            return redirect(url_for('users.register'))
        else:
            user = User(phone=user_phone)
            db.session.add(user)
            db.session.commit()
            flash('your account created successfully','info')
            return redirect('/')
    return render_template('users/verify.html', form=form)
