from flask import Flask, render_template, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load dataset
df = pd.read_csv("/Users/vigneshalle/Downloads/asi_dashboard/data/asi_features.csv")

@app.route('/')
def home():
    # Serve the main dashboard HTML
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # Return CSV as JSON
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
