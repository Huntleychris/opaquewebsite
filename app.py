from flask import Flask, render_template, request, jsonify
from your_module import calculate_amortization_schedule

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    principal_amount = float(data['principal'])
    annual_interest_rate = float(data['annual_interest_rate'])
    loan_term_years = int(data['loan_term_years'])
    extra_principal_payments = data['extra_principal_payments']

    amortization_schedule, total_paid = calculate_amortization_schedule(
        principal_amount, annual_interest_rate, loan_term_years, extra_principal_payments)

    return jsonify({
        'amortization_schedule': amortization_schedule,
        'total_paid': total_paid
    })

if __name__ == '__main__':
    app.run(debug=True)
