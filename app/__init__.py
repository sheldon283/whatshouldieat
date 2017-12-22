from flask import Flask, render_template, request
import yelpLib	
import sys

print(yelpLib)
sys.stdout.flush()
app = Flask(__name__)

yelpLib.test()
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def homePost():
	term = request.form["term"]
	location = request.form["location"]

	if not term or not location:
		return render_template("home.html", result=None)



	result = yelpLib.search(term, location)
	global reviews
	if result.get('businesses') is None:
		retValue = None
		reviews = None
	else:
		retValue = yelpLib.query_api(result)
		if retValue is None:
			reviews = None
		else:
			reviews=yelpLib.getReviews(retValue)

	return render_template('item.html', object=result, result=retValue, reviews=reviews, text=term, location=location)

if __name__ == '__main__':
	app.run(debug=True)

# from flask import Flask, render_template, request
# from yelp import yelp

# y = yelp()
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("home.html")

# @app.route('/', methods=['POST'])
# def homePost():
# 	term = request.form["term"]
# 	location = request.form["location"]

# 	if not term or not location:
# 		return render_template("home.html", result=None)



# 	result = y.search(term, location)
# 	global reviews
# 	if result.get('businesses') is None:
# 		retValue = None
# 		reviews = None
# 	else:
# 		retValue = y.query_api(result)
# 		if retValue is None:
# 			reviews = None
# 		else:
# 			reviews=y.getReviews(retValue)

# 	return render_template('item.html', object=result, result=retValue, reviews=reviews, text=term, location=location)

# if __name__ == '__main__':
# 	app.run(debug=True)

