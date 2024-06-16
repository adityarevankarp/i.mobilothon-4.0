import os
import random
import cv2
from ultralytics import YOLO
from tracker import Tracker

# Setting up Video Paths
video_in_path = os.path.join(".", "data", "input", "3.mp4")
video_out_path = os.path.join(".", "data", "output", "out3.mp4")

# Initialize video capture for reading the input video
cap = cv2.VideoCapture(video_in_path)
ret, frame = cap.read()

# Initialize video writer for writing the processed video with the same frame size and FPS as the input video
cap_out = cv2.VideoWriter(
    video_out_path,
    cv2.VideoWriter_fourcc(*"MP4V"),
    cap.get(cv2.CAP_PROP_FPS),
    (frame.shape[1], frame.shape[0]),
)

model = YOLO("yolov8n.pt")

tracker = Tracker()

colors = [
    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for j in range(20)
]

detection_threshold = 0.7

while ret:
    # Perform object detection on the current frame
    results = model(frame)

    # Extract bounding box coordinates, confidence score, and class ID for each detected object
    for result in results:
        detections = []
        for r in result.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = r
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            class_id = int(class_id)
            if score > detection_threshold:
                detections.append([x1, y1, x2, y2, score])

        tracker.update(frame, detections)

        # Draw bounding boxes and count the number of tracked objects
        num_tracked_objects = 0
        for track in tracker.tracks:
            bbox = track.bbox
            x1, y1, x2, y2 = bbox
            track_id = track.track_id

            # Draw the bounding box
            cv2.rectangle(
                frame,
                (int(x1), int(y1)),
                (int(x2), int(y2)),
                (colors[track_id % len(colors)]),
                2,
            )
            num_tracked_objects += 1

        # Display the count of tracked objects on the frame
        cv2.putText(
            frame,
            f"Persons: {num_tracked_objects}",
            (15, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

    # Write the processed frame to the output video
    cap_out.write(frame)

    # Read the next frame
    ret, frame = cap.read()

# Release resources
cap.release()
cap_out.release()
cv2.destroyAllWindows()

