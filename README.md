# Apple Disease Detection

This project explores the use of deep learning and image processing techniques to create a reliable system for spotting diseases in apple trees. The goal is to innovate agriculture by improving crop health monitoring and management.

## Introduction

This project aims to innovate agriculture by improving crop health monitoring and management through the use of deep learning and image processing techniques. It focuses on developing a machine learning model using Convolutional Neural Networks (CNNs) to detect and classify diseases in apple trees. The model is trained on a dataset of images of healthy and diseased apples, categorizing them into diseases like apple scab, blotch apple, and rotten apple.

## Dataset

The dataset used for training and testing the model is sourced from a variety of images available on the internet. It consists of 512 RGB images of healthy and diseased apples, including scab, blotch, rotten, and healthy apples. The images are labeled by disease category.

| Normal Apple                                                                                                                  | Blotch Apple                                                                                                                                      | Rotten Apple                                                                                              | Scab Apple                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| ![Normal Apple](https://static.wikia.nocookie.net/fruits-information/images/2/2b/Apple.jpg/revision/latest?cb=20180802112257) | ![Blotch Apple](https://d31n3wj3oi4lt9.cloudfront.net/wp-content/uploads/sites/36/2019/07/Apple-Sooty-blotch-and-flyspeck-belmishes-1024x845.jpg) | ![Rotten Apple](https://upload.wikimedia.org/wikipedia/commons/7/7f/Bitter_rot_on_a_Honeycrisp_apple.jpg) | ![Scab Apple](https://realenglishfruit.co.uk/wp-content/uploads/2021/12/apple-scab_pixabay-W1200.jpg) |

## Methodology

We used the Keras library in Python to construct and train the CNN model. The architecture includes convolutional, max pooling, and dropout layers to prevent overfitting. Data augmentation techniques were employed to increase diversity in the training set.

## Results

The model achieved 91.5% accuracy on the training set and 67% on validation and test sets. It showed high accuracy for healthy apples but lower for blotch and rotten apples. Visualizations of convolutional layer activations provided insights into the learned features.

## Web Application

The project includes a simple web application for testing the apple disease detector. The web application is built using Flask and integrates HTMX for dynamic content updates. Access the application by running `main.py` and visiting [http://localhost:3000](http://localhost:3000) in your web browser.

## Screenshots

- **Normal Apple**
  ![Normal Apple](https://github.com/MrMDrX/Apple-Disease-Detection/blob/main/screenshots/normal_apple_detected.png)

- **Blotch Apple**
  ![Blotch Apple](https://github.com/MrMDrX/Apple-Disease-Detection/blob/main/screenshots/blotch_apple_detected.png)

## Quick Start

1. Clone the repository:

   ```bash
   git clone https://github.com/MrMDrX/Apple-Disease-Detection.git
   ```

2. Navigate to the Project Directory:

   ```bash
   cd Apple-Disease-Detection
   ```

3. Create and Activate a Virtual Environment (Optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the apple disease detector:\*\*

   ```bash
   python main.py
   ```

6. Open a web browser and navigate to `http://localhost:3000` to access the web application.

## Usage

1. Upload an image of an apple.
2. Click the "Detect" button to analyze the image and predict the disease.
3. View the predicted disease class and confidence level.

## Technologies Used

- Python
- TensorFlow/Keras
- Flask
- HTML/CSS
- Bootstrap
- HTMX

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
