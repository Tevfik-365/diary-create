# Import
form_password = request.form['password']
#Assignment #4. implement authorisation
users_db = User.query.all
for user in users_db:
if form_login==user.email and form_password==user.password:
return redirect("/index")
else:
error="Incorrect login. There is a hacker!!!"
else:
return render_template("login.html",error=error)






@app.route('/reg', methods=['GET','POST'])
def reg():
if request.method == 'POST':
login= request.form['email']
password = request.form['password']
#Assignment #3 Ensure that user data is saved in the database
user = User(email=login,password=password)
db.session.add(user)
db.session.commit()


return redirect('/')
else:
return render_template('registration.html')




# Running the content page
@app.route('/index')
def index():
# Display database entries
cards = Card.query.order_by(Card.id).all()
return render_template('index.html', cards=cards)


# Running the registration page
@app.route('/card/<int:id>')
def card(id):
card = Card.query.get(id)


return render_template('card.html', card=card)


# Run the login creation page
@app.route('/create')
def create():
return render_template('create_card.html')


# Entry form
@app.route('/form_create', methods=['GET','POST'])
def form_create():
if request.method == 'POST':
title = request.form['title']
subtitle = request.form['subtitle']
text = request.form['text']


# Create an object to send to the database
card = Card(title=title, subtitle=subtitle, text=text)


db.session.add(card)
db.session.commit()
return redirect('/index')
else:
return render_template('create_card.html')










if __name__ == "__main__":
app.app_context().push()
db.create_all()
app.run(debug=True)
