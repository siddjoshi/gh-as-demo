from flask import Flask, render_template, request, redirect, url_for, flash
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'Jc7tSeejd1CVWtoCvbsGTcIdsWFo'  # For session management and flash messages

# Load and save expenses
class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        with open(self.filename, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, amount, description):
        expense = {
            'amount': amount,
            'description': description,
            'date': datetime.now().isoformat()
        }
        self.expenses.append(expense)
        self.save_expenses()

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            self.save_expenses()

tracker = ExpenseTracker()

@app.route('/')
def index():
    return render_template('index.html', expenses=tracker.expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    description = request.form['description']

    if not amount or not description:
        flash('Amount and description are required!')
        return redirect(url_for('index'))

    try:
        amount = float(amount)
    except ValueError:
        flash('Amount must be a number!')
        return redirect(url_for('index'))

    tracker.add_expense(amount, description)
    flash('Expense added successfully!')
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_expense(index):
    tracker.delete_expense(index)
    flash('Expense deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
