# Lane Change Safety System

## Overview
The **Lane Change Safety System** enhances driving safety by detecting and tracking vehicles in adjacent lanes, calculating their relative speeds, and issuing alerts for unsafe lane changes. Using YOLO, DeepSORT, and Time-to-Collision (TTC) algorithms, this system provides an early warning mechanism to prevent potential collisions.

---
![image](https://github.com/user-attachments/assets/a420daf0-63b6-4545-bf2f-e3b1d7d65fe1)
___

## Features
- **Object Detection**: Detects cars, trucks, and bikes using the YOLO model.
- **Object Tracking**: Tracks detected objects with unique IDs across frames using DeepSORT.
- **Speed Estimation**: Calculates relative speeds of tracked objects using optical flow and TTC.
- **Alert System**: Notifies drivers of potential collision risks based on speed and TTC analysis.


___
![image](https://github.com/user-attachments/assets/dfe15d0b-ab84-4ec6-8f65-b83daac45634)
___


## Project Architecture
1. **YOLO Object Detection**: Identifies vehicles in each frame with bounding boxes.
2. **DeepSORT Tracking**: Maintains object IDs for continuity across frames.
3. **Speed Estimation**: Calculates relative speed using TTC and displays it with the bounding boxes.
4. **Alert System**: Issues warnings if unsafe lane change conditions are detected.

---

## Technologies Used
- **YOLO (You Only Look Once)**: Object detection.
- **DeepSORT**: Tracking objects across video frames.
- **OpenCV**: Video frame processing and optical flow.
- **Python**: Core programming language.
- **TTC Algorithm**: Time-to-collision computation.

---

## Output
![image](https://github.com/user-attachments/assets/4e01c8da-faef-4f89-ab40-f940156a1960)
___

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/lane-change-safety-system.git
cd lane-change-safety-system
```


## Install Dependencies
 Ensure Python 3.8+ is installed. Then, run:
```bash
pip install -r requirements.txt
```

## Download YOLO Weights
### Download YOLO pre-trained weights from YOLO's official site.
### Save the weights file in the weights/ directory.

## Run the System
```bash
python lane_safety_system.py --input <path_to_video_file> --output <path_to_output_file>
```
### Replace <path_to_video_file> with your video input and <path_to_output_file> with your desired output location.

## Usage
- Processes video footage (e.g., dashcam).
- Detects vehicles and assigns bounding boxes with unique IDs and speed labels.
- Displays alerts in unsafe conditions and outputs the annotated video.

## Future Improvements
- **Real-Time Processing:** Enable live video feed processing.
- **V2X Communication::** Add Vehicle-to-Everything (V2X) for broader situational awareness.
- **Enhanced Alerts::** Implement visual/audible alerts for better driver attention.
- **Multi-Lane Awareness::** Extend support to track vehicles across multiple lanes.
- **Emergency Braking::** Integrate with braking systems to prevent collisions.

## Limitations
- Works with video files only (not real-time).
- Speed accuracy depends on frame rate and camera calibration.
- Only detects objects visible in the camera’s field of view.
























