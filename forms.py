from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=35)])
    submit = SubmitField('Login')

class CreateStudentForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired(), Length(min=3, max=100)])
    submit = SubmitField('Create Student')

class CreateTeacherForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=35)])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Create Teacher')

class CreateParentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=35)])
    child_id = SelectField('Child', coerce=int)  # Dynamic field to select a student
    submit = SubmitField('Create Parent')

class CreateFinanceForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=35)])
    submit = SubmitField('Create Finance')
