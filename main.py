from flask import Flask
from flask import render_template
from flask import request
import sec

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method=='POST':
   		f = request.files['file']
		matrix = sec.generateMatrixFromFile(f)
		return render_template('index.html', matrix=matrix)
   	else:
   		return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
