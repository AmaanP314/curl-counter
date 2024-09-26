# Curl Counter

This project is a web application designed to track and count bicep curls using computer vision. The app utilizes MediaPipe for real-time pose estimation and OpenCV to process video frames from the user's camera. The core functionality of this app is to count repetitions of bicep curls, providing feedback based on the user's arm movements.

## Table of Contents

- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [Contact](#contact)

## Features
- **Real-time Bicep Curl Counting**: Automatically counts the number of curls based on arm movements.
- **Dual Arm Support**: Tracks both left and right arms simultaneously.
- **Stage Feedback**: Detects and displays the current state of the curl, whether the arm is "Relaxed" or "Flexed."
- **MediaPipe Pose Estimation**: Leverages Google's MediaPipe library for real-time, accurate pose detection.
- **User-Friendly**: Simple and intuitive UI for starting the camera and viewing the curl count.
  
## Setup and Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/AmaanP314/curl-counter.git
    ```
2. Navigate to the project directory:
    ```bash
    cd curl-counter
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask server:
    ```bash
    python app.py
    ```
5. Open your web browser and go to `http://127.0.0.1:5000/`.
6. Start the camera feed and perform bicep curls. The application will count the repetitions automatically.

## Usage
- This tool is ideal for tracking exercise form and counting reps for workouts.
- Can be used by fitness enthusiasts, trainers, or developers interested in understanding computer vision applications.
- Demonstrates real-world use cases of OpenCV and MediaPipe for pose detection.

## Project Structure

 ```bash
    curl-counter/
    │
    ├── static/
    │   ├── styles.css/             # CSS files for styling
    │   └── app.js/              # JavaScript files for front-end logic
    │
    ├── templates/
    │   └── index.html       # HTML file for the front-end interface
    │
    ├── app.py               # Flask application
    ├── cv.py                # OpenCV and MediaPipe logic
    ├── requirements.txt     # List of dependencies

 ```

## Technologies Used
- **Flask**: Python web framework to handle the backend.
- **MediaPipe**: Library for real-time pose detection.
- **OpenCV**: Used for processing the camera input.
- **JavaScript**: To handle video streaming and communicate with the backend for frame processing.

## Future Improvements
- Adding support for multiple exercises.
- Providing feedback on form quality.
- Implementing a database to track user performance over time.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests.

## Contact

Amaan Poonawala - [GitHub](https://github.com/amaanp314) | [LinkedIn](https://www.linkedin.com/in/amaan-poonawala)

Feel free to reach out for any questions or feedback.

