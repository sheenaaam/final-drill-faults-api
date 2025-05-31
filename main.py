from flask import Flask
from models import db
from api.faults import faults_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(faults_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
