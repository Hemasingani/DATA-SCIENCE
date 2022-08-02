from flask import Flask , render_template , request , redirect

app = Flask(__name__)

db = {"Pallavi":8605720703,"Kavya":9852467150,"Hema":8452167360,"Tejashree":8965741230}

@app.route("/")
def index():
	return render_template("index.html") 


@app.route("/add" , methods = ['GET' , 'POST'])    
def add_num  ():
	if request.method == 'POST':
		a = request.form.get('nme')
		num = request.form.get('num')
		db.update({a:num})
		#print(db)
	return render_template("add.html") 

	 

@app.route("/display")    
def display():
	#db = {"Pallavi":8605720703,"Kavya":9852467150,"Hema":8452167360,"Tejashree":8965741230}
	return render_template("display.html" , db = db)


@app.route("/search" , methods = ['GET','POST'])
def search():
	if request.method == 'POST':
		name = request.form.get('name')
		if name in db.keys():
			b = db[name]
			str(b)
			return render_template("search.html" , name = name , b=b)
		else:
			c = "User not found"
			return render_template("search.html" , c=c )

	return render_template("search.html")




# to run the application 
if __name__ == '__main__' :
    app.run(debug = True , port ="5001")  #debug will save the changes eventually so must to be used.
