from flask import Flask, render_template, request, jsonify
from cv import processor_frame  # Import the vision logic from another file

app = Flask(__name__)

# Route to serve the frontend HTML
@app.route('/')
def index():
    return render_template('index.html')

# Route to process video frames
@app.route('/process_frame', methods=['POST'])
def process_frame_route():
    data = request.json
    image_data = data['image']
    
    # Call the function from the separate Python file
    reps, stages = processor_frame(image_data)  # Adjusted to return reps and stages
    
    return jsonify({'reps': reps, 'stage': stages})  # Send reps and stages for both arms

if __name__ == '__main__':
    app.run(debug=True)


