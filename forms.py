from flask_wtf import FlaskForm
import wtforms as forms

class LoginForm(FlaskForm):
  username = forms.StringField('Username')
  password = forms.PasswordField('Password')
  submit = forms.SubmitField('Login')


class RegisterForm(FlaskForm):
  username = forms.StringField('Username')
  password = forms.PasswordField('Password')
  confirm_password = forms.PasswordField('Confirm Password')
  submit = forms.SubmitField('Register')