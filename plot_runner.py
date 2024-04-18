import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, request, send_file, jsonify
import traceback
import io
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('cities_for_map.csv')

@app.route('/runplot', methods=['POST'])
def run_plot():
    code = request.data.decode('utf-8')

    try:
        # Execute the received code
        exec(code, {'plt': plt, 'sns': sns, 'pd': pd, 'data': data})
        buf = io.BytesIO()
        plt.savefig(buf, format='jpeg')
        plt.close()  # Close the plot to free memory
        buf.seek(0)

        return send_file(buf, mimetype='image/jpeg')

    except Exception as e:
        error_trace = traceback.format_exc()
        return jsonify({'error': str(e), 'trace': error_trace}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)