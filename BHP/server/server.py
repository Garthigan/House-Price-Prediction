from flask import Flask,request ,jsonify, render_template
import util
app = Flask(__name__, static_url_path='', static_folder='static', template_folder='static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        print("Total Sqft:", total_sqft)
        print("Location:", location)
        print("BHK:", bhk)
        print("Bath:", bath)

        response = jsonify({
            'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
        })

        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': 'Invalid request format'}), 400



if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction")
    util.load_saved_artifacts()
    app.run(debug=True)