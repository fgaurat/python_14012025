from flask import Flask,render_template
from CustomerDAO import CustomerDAO

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>" 

@app.route("/old_customers")
def old_customers():
    html =""
    dao = CustomerDAO("customers_db.db")
    for customer in dao.find_all():
        # print(customer)
        html+=f"<li>{customer.first_name} {customer.last_name}</li>"
        
    html = f"<ul>{html}</ul>" 
    return "<h1>Les Customers</h1>" +html

@app.route("/")
def customers():
    dao = CustomerDAO("customers_db.db")
    return render_template('customers.html',customers = dao.find_all())
