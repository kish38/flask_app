from wtforms import Form, StringField, TextAreaField, PasswordField, validators


class RegisterForm(Form):
    username = StringField('UserName', [validators.Length(min=3, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')