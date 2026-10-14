# Virtual Calculator

A Python-based virtual calculator that lets you perform arithmetic using hand gestures in front of a webcam. The app uses OpenCV, MediaPipe powered hand tracking via `cvzone`, and a lightweight Flask web interface to display the live camera feed and calculator UI.

## Features

- Real-time hand tracking with a webcam
- Virtual on-screen calculator buttons
- Gesture-based input via fingertip detection
- Live arithmetic evaluation with support for operators like `+`, `-`, `*`, `/`, and `^`
- Clear and equals functionality
- Simple web interface served by Flask

## Tech Stack

- Python
- OpenCV
- cvzone / HandTrackingModule
- MediaPipe
- Flask
- HTML template for the browser UI

## Project Structure

```text
Virtual-Calculator/
├── main.py                 # Flask app and calculator logic
├── button.py              # Button class used for UI and input detection
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Browser UI that displays the video feed
├── .gitignore
└── README.md              # Project documentation
```

## How It Works

1. The app opens the webcam using OpenCV.
2. A hand is detected with `HandDetector` from `cvzone`.
3. The calculator buttons are drawn onto the video frame.
4. When the index finger is close to a button, it is treated as a click.
5. The selected value is appended to the current expression.
6. Pressing `=` evaluates the expression and displays the result.

## Prerequisites

Before running the app, make sure you have:

- Python 3.8+
- A working webcam
- `pip` installed

## Installation

Clone the repository:

```bash
git clone https://github.com/Souvik-31/Virtual-Calculator.git
cd Virtual-Calculator
```

Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the app:

```bash
python main.py
```

Then open the browser and visit:

```text
http://localhost:5000
```

The app will start the webcam and display a live virtual calculator on the page.

## Notes

- Good lighting improves gesture detection.
- The app uses one hand at a time for interaction.
- The calculator is intended for demo and experimentation rather than production use.

## License

This project does not currently specify a license.

## Author

Souvik-31

## Contributing

Contributions are welcome. If you want to improve the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
