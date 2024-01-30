from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/litecoin_value', methods=['GET'])
def get_litecoin_value():
    coingecko_api_url = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'
    
    try:
        response = requests.get(coingecko_api_url)
        data = response.json()
        litecoin_value_usd = data['litecoin']['usd']
        return jsonify({'litecoin_value_usd': litecoin_value_usd})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
