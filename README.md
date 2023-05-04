# Revolutionizing Stroke Diagnosis: A Highly Accurate and Efficient Machine Learning Model.

### Harnessing the Power of Data to Identify Patients at Risk of Stroke with incredible results.

### Author: 
Kamal Muhamed

### Business problem:
Detecting Heart Stroke in patients is difficult using traditional methods. We are solving this by making the detection of stroke in a patient automated/semi-automated using advanced technology by studying the outlining patterns associated with people who are known to have stroke. 

### Data
The dataset used in this project is the stroke-data.csv

## Getting Started
### Prerequisites
To run this project, you will need to have the following software installed on your system:

Python 3

Google Colab

Required packages - pandas, numpy, scikit-learn, seaborn, matplotlib

## Results
Here are some of the insights after our analysis

![age](https://user-images.githubusercontent.com/103885606/232896533-f91f52ec-f643-4d56-a806-6bf7bdc7643b.png)

![smoking](https://user-images.githubusercontent.com/103885606/232896581-ad47af23-e461-4c84-9538-c9a3a5d4f285.png)


## Model Used 
I used a KNN to make the Stroke predictions.

Our model peformed amazingly having a recall of 100% meaning that our model can predict 100% of the time patients with stroke. It also has a precision of 100%
meaning our model can predict 100% of the time patients that don't have stroke

![score](https://user-images.githubusercontent.com/103885606/232896745-f6c6d51d-197b-460f-84fb-dc2b508e2d3c.JPG)

## Deployment
I have deployed this model and turned it into an interactive web app using Streamlit. Interact with the web app by clicking this link:
https://kamal-moha-stroke-prediction-app-r89nxn.streamlit.app/

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

