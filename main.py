from flask import Flask, request

from fifo_lifo import Stock

stock_1 = Stock("lifo")

app = Flask(__name__)


@app.route('/')
def start_page():
    return '''
        <html>
            <body>
                <h3>Регистрация прошения</h2>
                    <form action='/request/donation' method='get'>
                    <button type="submit">Попросить</button>
                </form><br><br>
                <h3>Регистрация пожертвования</h3>
                    <form action='/donate' method='post'>
                    <label for="name">Что жертвуете?</label>
                    <p><input type='text' name="name" id="name"><p>
                    <label for="amount">Сколько?</label>
                    <p><input type='number' name="amount" id="amount"><p>
                    <button type="submit">Пожертвовать</button>
                 </form>
            </body>
        </html>
        '''


@app.route('/request/donation', methods=['GET'])
def gift_page():
    return f'''
            <html>
                <body>
                    <h2>{stock_1.gift()}<h2>
                    <a href="/"><button type="submit">На главную</button></a>
                </body>
            </html>
            '''


@app.route('/donate', methods=['POST'])
def donate_page():
    name = request.form['name']
    amount = int(request.form['amount'])
    stock_1.donation(name, amount)
    return f'''
            <html>
                <body>
                    <h2>Спасибо!</h2>
                    <a href="/"><button type="submit">На главную</button></a>
                </body>
            </html>
            '''


if __name__ == "__main__":
    app.run(debug=True)
