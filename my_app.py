from flask import render_template, Flask
from datetime import datetime 
from flask_bootstrap import Bootstrap
from flask import render_template, Flask, redirect
from datetime import datetime 
from flask_bootstrap import Bootstrap 



from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, BooleanField
from wtforms.validators import Required
import pandas as pd



tips = pd.read_csv('data/tips.csv')


class tips_form(FlaskForm):

	#string field
	name = StringField('Name:', validators=[Required()])

	#select field is options
	time = SelectField('time', choices = [(i,i) for i in  ['Lunch', 'Dinner']])

	# Submit Field
	submit = SubmitField('Submit')



#dynamic variable
todays_date = datetime.now()
date_as_string = todays_date.strftime('%m/%d/%Y %H:%M:%S')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html', 
                           date = date_as_string)

@app.route('/like', methods = ['GET', 'POST'])
def like():
	form = tips_form()

	if form.validate_on_submit():

		name = form.name.data 
		time = form.time.data 
		

		mean_tip = round(tips[tips.time == time].tip.mean(), 2)

		
		return render_template('results.html', date = date_as_string, form = form,
		 name = name, time = time, mean_tip = mean_tip)
	else:

		return render_template('things_i_like.html', date = date_as_string, 
			form = form)


@app.route('/routine')
def routine():
    return render_template('routine.html', 
                           date = date_as_string)


if __name__ == '__main__':
    app.run(debug=True)