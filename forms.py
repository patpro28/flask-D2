from flask_wtf import FlaskForm
import wtforms as forms

class LoginForm(FlaskForm):
  username = forms.StringField('Username')
  email = forms.EmailField('Email')
  school = forms.StringField('School')
  graded = forms.BooleanField('Đã tốt nghiệp hay chưa')
  point = forms.FloatField('Diem')
  date = forms.DateField('Thời gian vào trường')
