# Fault_detection
Fault Detection, Classification and Isolation using Machine Learning models

In this project, we'll be building simple Machine learning models(Classifiers) to detect fault, classify it into L-G or L-L or L-L-L fault and to isolate the fault so as to know in which zone did the fault occur.

Faults are one of the most commonly occuring phenomenon in a power system .
To detect the fault is also important for a power system to maintain it's stability.

In this code, we make use of GaussianNb and DecisionTreeClassifier to create three Simple Machine Learning models to solve the above mentioned problems
The data we are using in this project is fairly clean, so it won't be needing any pre-processing

The input variables to all our models are per unit values of currents and volatges in different lines (Ic,Ib,Ia,Vc,Vb,Va)
The output of our first model is a single value which is either '1' or '0'. An output of '1' means there is a fault in the system and '0' means that the system has no fault.

The output of our second model is an array of four values which are all again either '1' or '0'. These four values correspond to ['G','C','B','A']. This lets us know what kind of fault it is. For example, if the output is [1,0,0,1], it is an L-G fault with A-phase and ground shorted. If the output is [0,1,1,1], it is a L-L-L fault.

The output of the third model is an array of three elements which are all either '1' or '0'. These three values correspond to ['Zone 3','Zone 2','Zone 1'] . This indicates where the fault occured.
