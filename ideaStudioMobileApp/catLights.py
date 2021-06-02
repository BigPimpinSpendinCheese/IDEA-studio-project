from flask import Flask, render_template, request, jsonify
from pythonosc import udp_client

client = udp_client.SimpleUDPClient('127.0.0.1', 12000)

app = Flask(__name__)

@app.route('/')
def homePage():
	# print("Message received")
    return render_template('home.html')

@app.route('/lightControl')
def lightControl():
	# print("Message received")
    return render_template('index.html')

@app.route('/timecapsule')
def timecapsule():
	# print("Message received")
    return render_template('timecapsule.html')

@app.route('/explanation')
def explanation():
	# print("Message received")
    return render_template('explanation.html')

@app.route('/shakingLights')
def shakingLights():
	# print("Message received")
    return render_template('shakingLights.html')

@app.route('/gridPicker')
def gridPicker():
	# print("Message received")
    return render_template('gridPicker.html')

@app.route('/enjoyTheLights')
def enjoyTheLights():
	# print("Message received")
    return render_template('enjoyTheLights.html')

@app.route('/sendMessage', methods=['POST'])
def sendMessage():
	if request.is_json:
		data = request.get_json();
		name = data.get('address')
		value = data.get('value')
		# print(data)
		client.send_message(name, value)
	else:
		print("###### MESSAGE RECEIVED, BUT NOT JSON #####")
	return render_template('index.html')

# if __name__ == '__main__':
# 	app.run(debug=True)

