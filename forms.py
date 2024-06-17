from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    name = StringField("Name of the cafe:", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired(), URL()])
    img_url = StringField("Cafe Image URL", validators=[DataRequired(), URL()])
    location = StringField("Location of the cafe", validators=[DataRequired()])
    seats = StringField("Available seats: ", validators=[DataRequired()])
    has_toilet = BooleanField("Is there any toilet? ", validators=[DataRequired()])
    has_wifi = BooleanField("Is WiFi available? ", validators=[DataRequired()])
    has_sockets = BooleanField("Is power sockets available? ", validators=[DataRequired()])
    can_take_calls = BooleanField("Can take phone calls? ", validators=[DataRequired()])
    coffee_price = StringField("Coffee price: ", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Create a form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

