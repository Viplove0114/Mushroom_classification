from flask import Flask, request, render_template, url_for
import pickle
import numpy as np
import logging.config

#create logger 
logger = logging.getLogger('simpleExample')


#application code
logging.basicConfig(filename = 'example.log', encoding = 'utf-8', level = logging.DEBUG)
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


#prediction function
def mush(result_data):
    prediction = np.array(result_data).reshape(1,12)
    load_model = pickle.load(open('XGBoost.pkl', "rb"))
    result = load_model.predict(prediction)
    return result[0]

#flask constructor
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result',methods = ['POST'])
def result():
    result_data = request.form.to_dict()
    result_data = list(result_data.values())
    result_data = list(map(float, result_data))
    result = mush(result_data)
    if result == 0:
        mushroom_type = ' this is POISONOUS'
    else:
        mushroom_type = 'this is Eatable'
    return render_template('result.html', results = mushroom_type)


if __name__ == '__main__':
    logging.config.fileConfig(fname='logger.ini')
    app.run(debug=True)