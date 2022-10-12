

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/')
def page():
    return render_template('blog/welcome.html')


@bp.route('/names/')
def get_uniq_names():
    db = get_db()
    artists = db.execute("SELECT DISTINCT artist FROM tracks ").fetchall()
    return render_template('blog/names.html', artists=str(len(artists)))


@bp.route('/tracks/')
def record():
    db = get_db()
    records = db.execute(" SELECT id FROM tracks ").fetchall()
    return render_template('blog/record.html', records=str(len(records)))


@bp.route('/tracks/<genre>')
def count_genre(genre):
    db = get_db()
    if genre == 'Pop':
        ans = db.execute("SELECT genre FROM tracks WHERE genre='Pop'").fetchall()
        return render_template('blog/count_genre.html', ans=str(len(ans)))
    elif genre == 'Classik':
        ans = db.execute("SELECT genre FROM tracks WHERE genre='Classik'").fetchall()
        return render_template('blog/count_genre.html', ans=str(len(ans)))
    elif genre == 'HardRock':
        ans = db.execute("SELECT genre FROM tracks WHERE genre='HardRock'").fetchall()
        return render_template('blog/count_genre.html', ans=str(len(ans)))
    elif genre == 'Rap':
        ans = db.execute("SELECT genre FROM tracks WHERE genre='Rap'").fetchall()
        return render_template('blog/count_genre.html', ans=str(len(ans)))
    else:
        return 'Genre not found'


@bp.route('/tracks-sec/')
def tracks_time():
    db = get_db()
    tracks = db.execute("SELECT title, length FROM tracks ").fetchall()
    return render_template('blog/time.html', tim=tracks)


@bp.route('/tracks-sec/statistics/')
def statistic():
    db = get_db()
    tracks = db.execute('SELECT SUM(length), COUNT(id) FROM tracks').fetchall()
    return render_template('blog/stat.html', tracks=tracks)


