import requests
from flask import Flask, request
from faker import Faker
import random
import string
import csv
import pandas as pd

app = Flask(__name__)


@app.route("/requirements/")
def file():
    res = ''
    with open('requirements.txt') as f:
        res += f.read()
    requirements_splitted = res.split('\n')
    res = ''
    for l in requirements_splitted:
        res += f'<p>{l}</p>'
    return res


@app.route('/generate-users/')
def users():
    fake = Faker()
    r = int(request.args.get('count'))
    dictionary = {}
    while r:
        s = fake.name()
        dictionary[s] = s.replace(' ', '') + '@gmail.com'
        r -= 1
    strings = []
    for key, item in dictionary.items():
        strings.append("{}: {}".format(key.capitalize(), item))
    result = "; ".join(strings)
    res_split = result.replace(';', '<p></p>')
    return res_split

3
@app.route('/mean/')
def average():
    df = pd.read_csv('flaskr/hw.csv')
    metres = df['Height(Inches)'].mean() * 0.025399987500778
    kg = df['Weight(Pounds)'].mean() / 2.2046
    return f'Средний вес человека: {kg} <p></p>  Средний рост: {metres}'


@app.route('/space/')
def astronavts():
    r = requests.get('http://api.open-notify.org/astros.json')
    a = str(r.json()["number"])
    return a + ' Космонавтов сейчас в космосе'