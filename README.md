# Stroke_Prediction
This project predicts whether someone will have a stroke or not



My final model with the best results is the KNeighbors(KNN) model

The evaluation metrics of the KNN model show that it has performed extremely well on the given dataset. The model has high recall for both the positive and negative classes, indicating that it can accurately identify both people with stroke and people without stroke. The f1 score, which is the harmonic mean of precision and recall, is also high for both classes. Moreover, the accuracy and AUC score are both 0.97, indicating that the model can make accurate predictions overall.

![auc](https://user-images.githubusercontent.com/103885606/230763263-60d5d9f5-4133-4fe0-802d-a6db8e4b058b.png)


Given the high performance of the KNN model, it can be useful in production if the dataset used to train the model is representative of the population it is applied to. To use the model in production, we have to ensure that there is balance in the dataset being used.

Balance in our target vector is very important in the dataset as that limits bias & improves results.

So Yes my model will be useful in production and will make correct predictions using a balanced dataset.





-----------------------

# Revolutionizing Stroke Diagnosis: A Highly Accurate and Efficient Machine Learning Model.

#### Harnessing the Power of Data to Identify Patients at Risk of Stroke with incredible results.

### Author: 
Kamal Muhamed

### Business problem:
Detecting Heart Stroke in patients is difficult using traditional methods. We are solving this by making the detection of stroke in a patient automated/semi-automated using advanced technology by studying the outlining patterns associated with people who are known to have stroke. 

### Data
The dataset used in this project is the sales_predictions.csv

## Getting Started
### Prerequisites
To run this project, you will need to have the following software installed on your system:

Python 3

Google Colab

Required packages - pandas, numpy, scikit-learn, seaborn, matplotlib

## Results
Here are some of the insights after our analysis


## Model Used 
I used a KNN to make the Stroke predictions.

Our model peformed amazingly having a recall of 100% meaning that our model can predict 100% of the time patients with stroke. It also has a precision of 100%
meaning our model can predict 100% of the time patients that don't have stroke
## Limitations & Next Steps

### Limitations

**Limited feature set**: This dataset was very imbalanced with over 95% of the patients not having stroke. This created bias as our model would learn more of one side. But we solved this by oversampling the positive class.

### Next Steps
**Take it to the Real World**: We need to use our model to make predictions using unseen data to see how it performs

**Incorporate more data**: To improve our dataset in the next iterations, we need to include more data points of people with stroke so that we can create target balance before modeling

## Acknowledgments
**Scikit-learn** for the machine learning library.

**Matplotlib** and **Seaborn** for data visualization.


## For further information
For any additional questions, please email **Kamalmohapy@gmail.com

