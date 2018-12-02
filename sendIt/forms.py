from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sendIt.models import User, Post


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)],render_kw={"placeholder": "Enter Username"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "password"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')],render_kw={"placeholder": "Confirm password"})
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()],render_kw={"placeholder": "Enter email"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "Enter password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()],render_kw={"placeholder": "item name"})
    content = TextAreaField('Content', validators=[DataRequired()],render_kw={"placeholder": "Quantity of Item"})
    location= StringField('Location', validators=[DataRequired()],render_kw={"placeholder": "Destination Location"})
    current_location= StringField('Now', validators=[DataRequired()],render_kw={"placeholder": "Pick up location"})
    submit = SubmitField('Post')
render_kw={"placeholder": "Enter password"}