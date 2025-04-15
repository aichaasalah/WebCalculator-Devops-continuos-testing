from flask import Flask
from app.routes import calculator

app = Flask(__name__)

# Enregistrement du blueprint pour les routes de calcul
app.register_blueprint(calculator)

if __name__ == "__main__":
    app.run(debug=True)
