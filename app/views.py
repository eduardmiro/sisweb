from flask import render_template
from app import app
@app.route('/')
@app.route('/home')
def home():
	user = { 'name': 'Barcenas','city':'Madrid' } # Mockup User

	sobres = [
		{
			'Company':{ 'name': 'ACS'},
			'Amount' : '100.000EUR'
		},
		{
			'Company':{ 'name': 'BANKIA'},
			'Amount' : '199999.9999.000EUR'
		},
		{
			'Company':{ 'name': 'TELEFONICA'},
			'Amount' : '100.000.000.000EUR'
		},
	]


	return render_template("index.html",
		pagetitle = 'Home',
		user = user, envelopes=sobres)
