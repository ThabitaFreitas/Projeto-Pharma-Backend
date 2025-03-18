from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta

# projeto flask
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class MarketingActions(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    action = db.Column(db.String(100), nullable = False)
    predicted_date = db.Column(db.String(100), nullable = False)
    predicted_investment = db.Column(db.Float(100), nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "action": self.action,
            "predicted_date": self.predicted_date,
            "predicted_investment": self.predicted_investment
        }

@app.route('/')
def index():
    return 'Ola Mundo'

@app.get('/marketing-actions')
def marketing_get():
    actions = MarketingActions.query.all()
    return jsonify([action.to_dict() for action in actions])

@app.post('/marketing-actions')
def marketing_post():
    data = request.get_json() 

    action, predicted_investment, predicted_date, error, status = validate_data(data)

    if error:
        return error, status 

    marketingAction = MarketingActions(action = action, predicted_date = predicted_date, predicted_investment = predicted_investment)

    db.session.add(marketingAction)
    db.session.commit()
    return jsonify({}), 200

@app.delete('/marketing-actions/<id>')
def  marketing_delete(id):
    marketingAction = db.get_or_404(MarketingActions, id)

    db.session.delete(marketingAction)
    db.session.commit()
    return jsonify({ "message": "acao de marketing deletada!" }), 200

@app.patch('/marketing-actions/<id>')
def marketing_patch(id):
    marketingAction = db.get_or_404(MarketingActions, id)
    
    data = request.get_json()

    action, predicted_investment, predicted_date, error, status = validate_data(data)

    if error:
        return error, status

    marketingAction.action = action
    marketingAction.predicted_date = predicted_investment
    marketingAction.predicted_investment = predicted_date
    
    db.session.commit()
    return jsonify({ "message": "acao de marketing atualizada!" }), 200

def validate_action(action):
    if action not in ["Palestra", "Evento", "Apoio Gráfico"]:
        return None, False
    return action, True

def validate_investment(investment):
    try:
        investment = float(investment)
        return investment, investment > 0
    except ValueError:
        return None, False

def validate_date(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        limite = datetime.today() + timedelta(days=10)
        return data.strftime("%d/%m/%Y"), data > limite
    except ValueError:
        return None, False
    
def validate_data(data):
    action, action_valid = validate_action(data.get('action'))
    predicted_investment, investment_valid = validate_investment(data.get('predicted_investment'))
    predicted_date, date_valid = validate_date(data.get('predicted_date'))

    if not action_valid:
        return  None, None, None, jsonify({ "message": "Ação inválida!" }), 400
    if not investment_valid:
        return  None, None, None, jsonify({ "message": "Investimento inválido!" }), 400
    if not date_valid:
        return  None, None, None, jsonify({ "message": "Data inválida!" }), 400

    return action, predicted_investment, predicted_date, None, 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5153)