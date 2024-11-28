from flask import Flask, request, render_template
import mysql.connector
import time
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Database configuration

import os

db_config = {
    'host': 'db',
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': 'Model_Logger',
    'port': 3306
}


# Load and train the model
data = pd.read_csv('temperaturedata.csv')
X = data[['day']]
y = data['temperature']
model = LinearRegression()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_time = time.time()
        input_day = request.form.get('input_day')
        output_temperature = model.predict(np.array([[float(input_day)]]))[0]
        response_time = time.time() - start_time
        log_to_database(input_day, output_temperature, response_time)
        return render_template('index.html', input_day=input_day, output_temperature=output_temperature)
    return render_template('index.html')

def log_to_database(input_day, output_temperature, response_time):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Log (Current_Date_Time, Input_Params, Output, Response_Time) VALUES (NOW(), %s, %s, %s)",
            (str(input_day), str(output_temperature), response_time)
        )
        conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
