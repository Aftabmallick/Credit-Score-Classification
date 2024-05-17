from flask import Flask, request, jsonify
from flask_cors import CORS
import util
app = Flask(__name__)
CORS(app)
@app.route('/get_credit_score', methods=['GET'])
def get_location_names():
    response = jsonify({
        'credit-mix': util.get_credit_mix(),
        'occupation': util.get_occupation_names(),
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
@app.route('/predict_credit_score',methods = ['POST'])
def predict_home_price():
    age = int(request.form['age'])
    annual_income = int(request.form['annual_income'])
    monthly_inhand_salary = int(request.form['monthly_inhand_salary'])
    num_bank_accounts = int(request.form['num_bank_accounts'])
    num_credit_card = int(request.form['num_credit_card'])
    interest_rate = int(request.form['interest_rate'])
    delay_from_due_date = int(request.form['delay_from_due_date'])
    num_of_delayed_payment = int(request.form['num_of_delayed_payment'])
    changed_credit_limit = int(request.form['changed_credit_limit'])
    num_credit_inquiries = int(request.form['num_credit_inquiries'])
    outstanding_debt = int(request.form['outstanding_debt'])
    credit_utilization_ratio = int(request.form['credit_utilization_ratio'])
    total_emi_per_month = int(request.form['total_emi_per_month'])
    amount_invested_monthly = int(request.form['amount_invested_monthly'])
    monthly_balance = int(request.form['monthly_balance'])
    credit_history_age_months = int(request.form['credit_history_age_months'])
    occupation = request.form['occupation']
    credit_mix = request.form['credit_mix']
    var=[age,annual_income,monthly_inhand_salary,num_bank_accounts,num_credit_card,interest_rate,delay_from_due_date,num_of_delayed_payment,
            changed_credit_limit,num_credit_inquiries,outstanding_debt,credit_utilization_ratio,total_emi_per_month,amount_invested_monthly,
            monthly_balance,credit_history_age_months]
    response = jsonify({
        'estimated_credit_score': util.get_estimated_price(
            var,occupation,credit_mix
        )
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ =="__main__":
    print("Starting Python Flask Server For Home Price Predction...")
    util.load_saved_artifacts()
    app.run()