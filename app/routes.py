from flask import Blueprint, render_template, jsonify

calculator = Blueprint('calculator', __name__)

# Route pour l'interface utilisateur
@calculator.route('/')
def index():
    return render_template('index.html')

# Route API pour addition
@calculator.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify(result=a + b)

# Route API pour soustraction
@calculator.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return jsonify(result=a - b)
