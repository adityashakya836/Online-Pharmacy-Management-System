# #Classification of Iris Flower dataset using K-Nearest Neighbors(K-NN)

# #Load the required module
# import numpy as np
# import pandas as pd

# #For classification we use sklearn library

# from sklearn.datasets import load_iris #iris dataset from sklear.datasets
# from sklearn.model_selection import train_test_split, KFold
# from sklearn.neighbors import KNeighborsClassifier # K-NN classifier
# from sklearn.metrics import accuracy_score # for finding accuracy score
# from sklearn.preprocessing import Normalizer # for nomalizing the data set
# from sklearn.ensemble import RandomForestClassifier

# iris=load_iris() #load the data set
# # print(iris)
# #convert the dataset into DataFrame for classification
# #for DataFrame conversion use pandas framework

# df=pd.DataFrame(
#     data=np.c_[iris['data'],iris['target']],
#     columns=iris['feature_names']+['target']
# )
# #Here np.c_ is the numpy conatenate function which concatenate data and target
# # print(df.head())
# #we get the output of above satement is speal length, sepal width, petal width, petal length, target
# # to descirbe our data frame use df.dscribe() function
# # print(df.describe())
# #The above function give count, mean, std, max etc
# # Now split the dataset into X and Y 
# X = df.iloc[:,:-1]
# Y = df.iloc[:,-1]

# #The dataset X gives all the data like sepal length, sepal widht, petal length, petal width or the flower
# #The dataset Y give the target of the flower

# # No we are going to split our data into train and test sets
# X_train,X_test,y_train,y_test = train_test_split(
#     X,Y,
#     test_size=0.4, # we take our test size as 0.4 which incluse 40% of our data is for testing and remaining 60% is for training
#     shuffle=True,
#     random_state=0
# )
# # Now normalize the dataset
# #define a variable named as normalizer
# normalizer= Normalizer().fit(X_train)
# normalized_X_train = normalizer.transform(X_train)
# normalized_x_test = normalizer.transform(X_test)

# # print('X train before Normalization')
# # print(X_train[0:5])
# # print("X train after normalization")
# # print(normalized_X_train[0:5])

# # Now Classify the DataSet using KNN Algorithm
# # we have 10 fold cross validation 
# K_Nearest_Neigbor = KNeighborsClassifier(10) # define KNeighborsClassifier with fold cross validation 10
# K_Nearest_Neigbor.fit(normalized_X_train,y_train) # fit the model
# prediction=K_Nearest_Neigbor.predict(normalized_x_test) # predict the model

# # Random Forest Classifier Model
# Random_Forset_Classifier = RandomForestClassifier(10)
# Random_Forset_Classifier.fit(normalized_X_train,y_train)
# random_classifier = Random_Forset_Classifier.predict(normalized_x_test)

# print("Accuracy using K-Nearest Neighbor classifier",accuracy_score(y_test,prediction))
# # we have the accuracy of 0.9666666666666667
# print("Accuracy using RandomForestClassifer : ",accuracy_score(y_test,random_classifier))
# # we have the accuracy of  0.9333333333333333 with 10 fold cross validation using Random Forest Algorithm

import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(0,10,100)
y=5+4*t-np.exp(t)

fig=plt.figure(figsize=(5,6))
plt.plot(t,y)
plt.show()
