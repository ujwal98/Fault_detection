# Importing necessary packages
import pandas as pd
import sklearn
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

#Importing the data
detection_train = pd.read_csv('Detection_train.csv').dropna(axis=1)
detection_test = pd.read_csv('Detection_test.csv').dropna(axis=1)
class_train = pd.read_csv('classData.csv').dropna(axis=1)
zone_train = pd.read_csv('isolationTRAIN.csv').dropna(axis=1)
zone_test = pd.read_csv('isolationTEST.csv').dropna(axis=1)
features=['Ic','Ib','Ia','Vc','Vb','Va']
class_target = ['G','C','B','A']
zone_target = ['Z3','Z2','Z1']

#Defining different Models for different classification problems
detection_model = GaussianNB()
class_model = DecisionTreeClassifier()
zone_model = DecisionTreeClassifier()

#Defining the inputs and outputs
detection_train_X = detection_train[features]
detection_test_X = detection_test[features]
class_data_X = class_train[features]
zone_train_X = zone_train[features]
zone_test_X = zone_test[features]
detection_train_Y = detection_train['Output (S)']
detection_test_Y = detection_test['fault']
class_data_Y = class_train[class_target]
zone_train_Y = zone_train[zone_target]
zone_test_Y = zone_test[zone_target]

#Splitting the data 
class_train_X,class_test_X,class_train_Y,class_test_Y= train_test_split(class_data_X,class_data_Y,test_size=0.33,random_state=1)

#Fitting the data in different models
detection_model.fit(detection_train_X,detection_train_Y)
class_model.fit(class_train_X,class_train_Y)
zone_model.fit(zone_train_X,zone_train_Y)

#Predicting test values and printing out Mean Squared Error
detection_preds = detection_model.predict(detection_test_X)
print(mean_squared_error(detection_test_Y,detection_preds))

class_preds = class_model.predict(class_test_X)
print(mean_squared_error(class_test_Y,class_preds))

zone_preds = zone_model.predict(zone_test_X)
print(mean_squared_error(zone_test_Y,zone_preds))

# Printing out accuracy scores of our models
print('The accuracy score of our Detection Model is: ',(accuracy_score(detection_test_Y,detection_preds)))
print('The accuracy score of our Classification Model is: ',(accuracy_score(class_test_Y,class_preds)))
print('The accuracy score of our Isolation Model is: ',(accuracy_score(zone_test_Y,zone_preds)))