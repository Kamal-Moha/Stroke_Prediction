# Stroke_Prediction
This project predicts whether someone will have a stroke or not



My final model with the best results is the KNeighbors(KNN) model

The evaluation metrics of the KNN model show that it has performed extremely well on the given dataset. The model has high recall for both the positive and negative classes, indicating that it can accurately identify both people with stroke and people without stroke. The f1 score, which is the harmonic mean of precision and recall, is also high for both classes. Moreover, the accuracy and AUC score are both 0.97, indicating that the model can make accurate predictions overall.

![auc](https://user-images.githubusercontent.com/103885606/230763263-60d5d9f5-4133-4fe0-802d-a6db8e4b058b.png)


Given the high performance of the KNN model, it can be useful in production if the dataset used to train the model is representative of the population it is applied to. To use the model in production, we have to ensure that there is balance in the dataset being used.

Balance in our target vector is very important in the dataset as that limits bias & improves results.

So Yes my model will be useful in production and will make correct predictions using a balanced dataset.

