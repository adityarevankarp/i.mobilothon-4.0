# Crowd Estimation using YOLOv8 and Deep SORT

This repository contains the implementation of a crowd estimation system using the YOLOv8 (You Only Look Once version 8) object detection algorithm and the Deep SORT (Simple Online and Realtime Tracking with a Deep Association Metric) algorithm. The system can detect and track people in video streams, providing an estimation of the crowd count in real-time.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Modifications to Deep SORT](#modifications-to-deep-sort)

## Introduction

Crowd estimation is a critical task for public safety and management. This project leverages the power of YOLOv8 for object detection and Deep SORT for tracking to estimate the number of people in a given frame or video stream. The combined approach allows for accurate and efficient real-time crowd estimation.

## Features

- Real-time person detection using YOLOv8.
- Robust tracking of detected persons with Deep SORT.
- Accurate crowd count estimation.
- Easy integration with various video input sources (e.g., video files, webcams).

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KalmathAjay/Crowd-Estimation-using-YOLO-and-Deep-SORT.git
   cd Crowd-Estimation-using-YOLO-and-Deep-SORT
   ```

2. **Install the required dependencies:**

   All dependencies can be installed using the provided requirements.txt file.

   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLOv8 weights:**

Download the pre-trained YOLOv8 weights from the [Ultralytics repository](https://github.com/ultralytics/ultralytics).
Place the weights file in the model_data directory.

## Modifications to Deep SORT

Changes were made to the original Deep SORT implementation to support TensorFlow for compatibility with this project. The modified Deep SORT implementation is based on the original repository [Deep SORT](https://github.com/nwojke/deep_sort).
