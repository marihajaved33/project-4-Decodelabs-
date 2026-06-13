# Image and Text Recognition System using OCR

## Project Overview

This project implements an Optical Character Recognition (OCR) system using Python, OpenCV, and Tesseract OCR. The system is capable of recognizing printed text and simple handwritten text from images. It processes images, extracts text, displays confidence scores, and highlights detected text regions using bounding boxes.

## Features

* Image preprocessing
* Grayscale conversion
* Noise reduction
* Thresholding techniques
* Text extraction using OCR
* Confidence score calculation
* Bounding box generation
* Multiple image processing
* Result storage in text files

## Technologies Used

* Python
* OpenCV
* Tesseract OCR
* NumPy

## Project Structure

ImageTextRecognition/

├── images/

│ ├── sample1.jpg

│ ├── sample2.jpg

├── output/

├── main.py

├── requirements.txt

└── README.md

## Installation

Install the required libraries:

pip install opencv-python pytesseract numpy pillow

Install Tesseract OCR and update its path in main.py if required.

## Running the Project

python main.py

## Output

The program generates:

* Extracted text files (.txt)
* Images with detected text bounding boxes
* Confidence scores displayed in the terminal

## Applications

* Document digitization
* Form processing
* Educational tools
* Text extraction from images
* Information retrieval systems

## Future Enhancements

* Deep learning based handwriting recognition
* Real-time webcam OCR
* Multi-language support
* Mobile application integration

## Author

Mariha Javed

BS Computer Science
