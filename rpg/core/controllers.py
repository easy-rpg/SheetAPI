from flask import Blueprint, render_template, flash, session, g, redirect
from rpg import db
from rpg.core.forms import LoginForm, UsuarioForm
from rpg.core.models import Usuario

mod_core = Blueprint('core', __name__)


@mod_core.route('/')
def index():
    if g.usuario is None:
        return redirect('/login')

    return render_template('core/index.html', usuario=g.usuario)


@mod_core.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()

        if usuario is not None and usuario.senha == form.senha.data:
            flash('Seja bem vindo '+usuario.nome+'!')
            session['id_usuario'] = usuario.id_usuario
            return redirect('/')
        else:
            flash('Email ou senha incorretos. Tente novamente!')
            return render_template('core/login.html', form=form, usuario=g.usuario)
    return render_template('core/login.html', form=form, usuario=g.usuario)


@mod_core.route('/logout')
def logout():
    session.pop('id_usuario', None)
    flash('You were logged out')
    return redirect('/')


@mod_core.route('/campanhas')
def campanhas():
    if g.usuario is None:
        return redirect('/login')

    return render_template('/core/campanhas.html', usuario=g.usuario)


@mod_core.route('/novo_usuario')
def novo_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        usuario = Usuario(form.nome.data, form.email.data, form.senha.data)
        db.session.add(usuario)
        db.session.commit()
        flash('Usuário criado com sucesso')

        return redirect('/')
    return render_template('core/cadastrar.html', title='Sign In', form=form)
