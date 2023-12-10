'''
-----DESIGN-----
I will solve the problem by creating a website for the vegetable database.
I solved the problem by creating a website for the vegetable database.
I tested by making sure it added, saved, and showed the vegtables and worked appropriately. I
also tested that the website ran, which I had a bunch of problems with.
My code creates a vegetable database and allows users to add, change,
delete, and show all vegetables in the database through a website.
'''
'''
-----USER DOCUMENTATION-----
To add a vegetable to the database type in a vegetable and a quantity into the boxes.
Then hit add, it will then update the status to tell you whether it was successfully added
and what it added.
To delete a vegetable type in the vegetable name and then set the quantity to -1.
To update a vegetable value type in the same name and a new quantity. 
'''
'''
Name: Jordyn Kuhn
Date: 3/8/23
CRN: 23199
CIS 226: Advanced Python Programming
Time Estimate: 7 hours
'''

from vegetables import Vegetables
import sqlite3
from flask import Flask, render_template, redirect, url_for, request, flash
PATH = 'db.sqlite3'

app = Flask(__name__)
app.secret_key = b'sgjH0K3UlPxJDd588Et-de9_WkOvbkLaaotrcKG-_hg'

def db_setup():
    with sqlite3.connect(PATH) as conn:
        v = Vegetables(conn)
        v.setup()

app.before_first_request(db_setup)

@app.route('/', methods =['GET', 'POST'])
def index():
    name = ''
    quantity = ''
    valid = False

    if request.method == 'POST':
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        valid = True

        if not name or not quantity:
            flash('Please provide both a vegetable and a quantity')
            valid = False
        else:
            try: 
                quantity = int(quantity)
            except ValueError:
                flash('Quantity has to be an integer')
                valid = False

    with sqlite3.connect(PATH) as conn:
        v = Vegetables(conn)

        if quantity == '-1' or quantity == -1:
            v.del_vegetable(name)
        if valid and quantity != '0' and quantity != -1:
            v.add_vegetable(name, quantity)
            flash('Successfully added {} {} to the table.'.format(quantity, name))
            return redirect(url_for('index'))
        
        vegetables = v.show_all()

    return render_template(
        'main.html',
        title="Vegetable Database",
        vegetables=vegetables,
        name=name,
        quantity=quantity,
    )
