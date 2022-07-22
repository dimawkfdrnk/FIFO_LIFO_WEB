from flask import Flask, request, render_template

from fifo_lifo import Stock

stock_1 = Stock('lifo')
stock_2 = Stock('lifo')
app = Flask(__name__)


@app.route('/', methods=['GET'])
def start_page():
    return render_template('home_page.html')


@app.route('/request/donation', methods=['POST'])
def gift_page():
    stocks = {'stock_1': stock_1.gift()}
    return render_template('donation_page.html', stocks=stocks)


@app.route('/donate', methods=['POST'])
def donate_page():
    name = request.form['name']
    amount = int(request.form['amount'])
    stock_1.donation(name, amount)
    return render_template('donate_page.html')


if __name__ == "__main__":
    app.run(debug=True)
