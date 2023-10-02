import os
from datetime import timedelta
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=30)
bootstrap = Bootstrap(app)
app.static_folder = 'static'

# Configuración de mensajes de 'flash'
app.config['FLASH_MESSAGES'] = True
app.config['FLASH_MESSAGES_CATEGORY'] = 'message'

# Definir el formulario de contacto
class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=5)])
    email = StringField('Correo Electrónico', validators=[DataRequired()])
    message = StringField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.route('/')
def index():
    name = session.get('name')
    return render_template('index.html',name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Aquí puedes manejar el envío del formulario, por ejemplo, enviar un correo electrónico
        # y luego redirigir a otra página o mostrar un mensaje de éxito.
        session['name'] = form.name.data
        flash('Formulario enviado con éxito', 'success')
        return redirect(url_for('index'))

    return render_template('contact.html', form=form)

@app.route('/info')
def modal_content():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True)