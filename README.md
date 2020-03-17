# Fault_detection
Fault Detection, Classification and Isolation using Machine Learning models

In this project, we'll be building simple Machine learning models(Classifiers) to detect fault, classify it into L-G or L-L or L-L-L fault and to isolate the fault so as to know in which zone did the fault occur.

Faults are one of the most commonly occuring phenomenon in a power system .
To detect the fault is also important for a power system to maintain it's stability.
Please note that although I'll be calling the problems fault_detection, fault_classification and fault_isolation, they are all Classification Problems.


# Dataset
The data we are using in this project is fairly clean, so it won't be needing any pre-processing. The data for detection and isolation are divided into train and test data beforehand. However, the classification data is not available that way. So we'll be using train_test_split method from sklearn.metrics to divide the data into train_batch and test_batch


# Input
The input variables to all our models are per unit values of currents and volatges in different lines (Ic,Ib,Ia,Vc,Vb,Va).


# Output
The output of our first model is a single value which is either '1' or '0'.
An output of '1' means there is a fault in the system and '0' means that the system has no fault.

The output of our second model is an array of four values which are all again either '1' or '0'. These four values correspond to ['G','C','B','A']. This lets us know what kind of fault it is. For example, if the output is [1,0,0,1], it is an L-G fault with A-phase and ground shorted. If the output is [0,1,1,1], it is a L-L-L fault.

The output of the third model is an array of three elements which are all either '1' or '0'. These three values correspond to ['Zone 3','Zone 2','Zone 1'] . This indicates where the fault occured.

However, when you run the code you'll be getting output of our model's evaluation. The first three lines(or numbers) are mean squared errors of our models and the next three lines are accuracy scores of our models.


# Model
In this code, we make use of GaussianNb and DecisionTreeClassifier to create three Simple Machine Learning models to solve the above mentioned problems. 
We are using DecisionTreeClassifier for fault_classification and fault_isolation as they are multi-class classification problems and looking at the data we can say that a tree is better  suited for these problems as the current in a branch changes drastically when a fault occurs. 
So, DecsionTreeClassifier would provide a better chance to obtain an accuracy score of 1.0 or closer  to 1.0
