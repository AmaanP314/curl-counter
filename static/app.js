const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const repsElem = document.getElementById('reps');
const stageElem = document.getElementById('stage');
const cameraSwitch = document.getElementById('cameraSwitch');
const cameraStatus = document.getElementById('cameraStatus');

let stream;

// Access the user's camera
function startCamera() {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(s => {
            stream = s;
            video.srcObject = stream;
            cameraStatus.textContent = "Camera On";
        })
        .catch(err => {
            console.error('Error accessing the camera', err);
        });
}

function stopCamera() {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        cameraStatus.textContent = "Camera Off";
    }
}

// Send video frames to the backend for processing
async function sendFrame() {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = canvas.toDataURL('image/jpeg');

    try {
        const response = await fetch('/process_frame', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ image: imageData })
        });

        if (!response.ok) {
            throw new Error('Server responded with an error');
        }

        const data = await response.json();
        // Display reps and stage for both arms
        repsElem.textContent = `Right: ${data.reps.right}, Left: ${data.reps.left}`;
        stageElem.textContent = `Right: ${data.stage.right}, Left: ${data.stage.left}`;
    } catch (err) {
        console.error('Error sending frame to the server', err);
    }

    requestAnimationFrame(sendFrame);
}

cameraSwitch.addEventListener('change', (event) => {
    if (event.target.checked) {
        startCamera();
        sendFrame();
    } else {
        stopCamera();
    }
});
