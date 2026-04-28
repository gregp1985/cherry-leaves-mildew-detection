# Mildew Detection in Cherry Leaves

## Dataset Content

The dataset contains images of cherry leaves provided by Farmy & Foods.

The images are categorised into two classes:
- Healthy: images of cherry leaves without disease
- Powdery Mildew: images of cherry leaves affected by fungal infection

Each image is a colour image with a resolution of 256x256 pixels.

The dataset is used to:
- Perform a visual study to differentiate healthy and infected leaves
- Train a machine learning model to classify leaf health status

## Business Requirements

The client is interested in:

1. Conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
2. Predicting if a cherry leaf is healthy or contains powdery mildew using an ML system.

The client requires a dashboard that presents both the visual study and the predictive system.

## Mapping Business Requirements to Data Visualisation and ML Tasks

### Business Requirement 1: Visual Differentiation

- User Story: As a client, I want to understand the visual differences between healthy and infected leaves so that I can identify mildew patterns.

- Data Visualisation Tasks:
  - Generate average images for each class
  - Generate variability images for each class
  - Compare differences between average images
  - Create image montages

### Business Requirement 2: Prediction System

- User Story: As a client, I want to upload leaf images and receive predictions so that I can quickly identify infected leaves.

- ML Tasks:
  - Train a Convolutional Neural Network (CNN)
  - Evaluate model performance using accuracy, confusion matrix, and classification report
  - Deploy model in a Streamlit dashboard for real-time predictions

## ML Business Case

The aim of this predictive analytics task is to build a supervised binary classification model that predicts whether a cherry leaf is healthy or affected by powdery mildew.

- Learning Method: Supervised learning using a Convolutional Neural Network (CNN)
- Ideal Outcome: A model capable of accurately classifying leaf images
- Success Metric: Minimum 97% prediction accuracy
- Model Output: Binary classification (Healthy / Powdery Mildew) with probability score
- Heuristics: Image resizing to 100x100 pixels to reduce model size and training time
- Training Data: Labelled dataset of cherry leaf images provided by the client

The model achieved 99% accuracy on the test dataset, exceeding the business requirement.

## Hypothesis and Validation

### Hypothesis

Cherry leaves affected by powdery mildew have visible patterns that can be distinguished from healthy leaves through image analysis, and these patterns can be learned by a neural network classifier.

### Validation

The visual analysis demonstrated clear differences in colour, texture, and visible fungal patches between healthy and infected leaves.

The trained CNN model achieved 99% accuracy on unseen test data, confirming that the patterns can be successfully learned.

Therefore, the hypothesis was validated.

## Dashboard Design

### Page 1: Project Summary

![Project Summary Page](assets/images/project_summary.png)

- Content:
  - Project background
  - Dataset description
  - Business requirements
- Purpose:
  - Provide context for the problem and dataset
- Business Requirement:
  - Supports understanding of both requirements

---

### Page 2: Leaf Visualiser

![Leaf Visualiser Page](assets/images/leaf_visualiser.png)

- Content:
  - Average images (healthy vs mildew)
  - Variability images
  - Difference image
  - Image montage
  - Interpretations for each visual
- Purpose:
  - Demonstrate visual differences between leaf classes
- Business Requirement:
  - Addresses Business Requirement 1

#### Plots

##### Average Images

The average images show clear differences in colour and texture between classes.

![Average Healthy](assets/images/avg_healthy.png)
![Average Mildew](assets/images/avg_mildew.png)

##### Variability Images

The Variability images show how pixel values differ across samples. Higher variability in mildew leaves suggests irregular patterns caused by infection.

![Variability Healthy](assets/images/var_healthy.png)
![Variability Mildew](assets/images/var_mildew.png)

##### Difference Images

The difference image highlights regions where healthy and mildew leaves diverge, confirming that visual features can distinguish between classes.

![Difference](assets/images/difference.png)

##### Image Samples

The montages show sample images from each class. Mildew leaves display visible white fungal patterns, while healthy leaves are uniformly green.

![Healthy Montage](assets/images/montage_healthy.png)
![Mildew Montage](assets/images/montage_mildew.png)

---

### Page 3: Mildew Detector

![Mildew Detector Page](assets/images/mildew_detector.png)

- Content:
  - Image upload widget (multiple images)
  - Prediction results with probability
  - Results table
  - CSV download button
- Purpose:
  - Provide real-time prediction capability
- Business Requirement:
  - Addresses Business Requirement 2

---

### Page 4: Project Hypothesis

![Project Hypothesis Page](assets/images/project_hypothesis.png)

- Content:
  - Project hypothesis
  - Validation using visual analysis
  - Validation using model performance
- Purpose:
  - Demonstrate reasoning and validation of the approach

---

### Page 5: ML Performance

![ML Performance Page](assets/images/ml_performance.png)

- Content:
  - Accuracy plot
  - Loss plot
  - Confusion matrix
  - Final evaluation statement
- Purpose:
  - Show model performance and confirm it meets business requirements
- Business Requirement:
  - Addresses Business Requirement 2

#### Plots

##### Accuracy Curve

The accuracy curve shows how the model improved during training and validation.

![Accuracy](assets/images/accuracy_plot.png)

##### Loss Curve

The loss curve helps show whether the model learned effectively and whether there were signs of overfitting.

![Loss](assets/images/loss_plot.png)

##### Confusion Matrix

The confusion matrix shows how many test images were correctly or incorrectly classified.

![Confusion Matrix](assets/images/confusion_matrix.png)

## CRISP-DM Process

### Business Understanding
The goal was to reduce manual inspection time by developing a system to identify powdery mildew in cherry leaves.

### Data Understanding
The dataset consisted of labelled images of cherry leaves categorised into healthy and powdery mildew classes.

### Data Preparation
Images were resized to 100x100 pixels and split into training, validation, and test datasets.

### Modelling
A Convolutional Neural Network (CNN) was trained using augmented image data.

### Evaluation
The model was evaluated using accuracy, loss curves, confusion matrix, and classification report.

### Deployment
The model was deployed using a Streamlit dashboard to allow user interaction and prediction.

## Epics and User Stories

### Epic: Data Analysis
- As a client, I want to understand visual differences between healthy and infected leaves so that I can identify mildew patterns.

### Epic: Machine Learning
- As a client, I want a system that predicts leaf health so that I can reduce manual inspection time.

### Epic: Dashboard
- As a client, I want a dashboard interface so that I can interact with the system easily.

## Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Streamlit
- Git & GitHub

## Deployment

The application was deployed using Heroku.

Steps:
1. Create a Heroku app
2. Connect the app to the GitHub repository
3. Set buildpacks to Python
4. Deploy the application

Required files:
- Procfile
- requirements.txt
- runtime.txt
- setup.sh

The application can be accessed via the deployed URL.

## Testing

### Model Testing

The model was evaluated on a test dataset that was not used during training.

- Test Accuracy: 99%
- The model exceeded the required 97% accuracy threshold.
- Confusion matrix showed high accuracy across both classes.

### Dashboard Testing

The dashboard was tested to ensure all functionality works as expected:

- All pages load correctly
- Images display properly
- Expanders open and close correctly
- File uploader accepts multiple images
- Predictions display correctly with probability
- Results table is generated correctly
- CSV download functionality works

### Manual Testing

- Uploaded healthy leaf images → correctly predicted as healthy
- Uploaded mildew images → correctly predicted as powdery mildew
- Tested with multiple images → results displayed correctly

This image shows 4 images uploaded to the mildew detector (in this case two with mildew and two without).

![Multiple Images Uploaded](assets/images/mildew_detector_testing_1.png)

This image shows the results of the 4 uploaded images (identifying both healthy and mildew leaves correctly).

![Multiple Images Results](assets/images/mildew_detector_testing_2.png)

### Responsiveness Testing

- Dashboard tested on different screen sizes
- Layout remains readable and functional

### Bugs and Fixes

- TensorFlow environment issues resolved by recreating virtual environment
- Path issues resolved by correcting directory structure

## Credits

- Dataset provided by Code Institute and Farmy & Foods
- Project guidance from course materials