from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='My Calculator')

@app.route('/loan', methods=['GET', 'POST'])
def loan():
   if request.method == 'POST':
        form = request.form
        amount = float(form['amount'])
        nperyear= float(form['nperyear'])
        years= float(form['years'])
        rate= float(form['rate'])
        n = nperyear * years
        i = rate / nperyear
        D = ((( 1 + i ) ** n ) - 1 ) / ( i * ( 1 + i) ** n )
        calc = "Your loan payment is $" + str(round(amount / D, 2))
        return render_template('index.html', display=calc, pageTitle='My Calculator')
    
     

if __name__ == '__main__':
    app.run(debug=True)
