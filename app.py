import datetime
import os

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items
from database import db_session
from tabulate import tabulate
from tables import Results

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route("/success")
def success():
    qry = db_session.query(Items)
    results = qry.all()
    results_list = [[item.id, item.name, item.quantity, item.description] for item in results]
    print(tabulate(results_list, headers=['Id', 'Name', 'Qty', 'Descr'], tablefmt='orgtbl'))
    #return str(results)
    table = Results(results)
    table.border = True
    return render_template('results.html', table=table)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
