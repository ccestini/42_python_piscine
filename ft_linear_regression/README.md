* -> GOAL:
Project goal is to implement gradient descent with the provided formulas to train a linear regression model for predicting car prices.

Linear Regression Formula: After training, you’ll use a linear function
estimatePrice(mileage) = theta_0 + (theta_1 ∗ mileage)

Implement Gradient Descent: Update the parameters (theta_0, theta_1) iteratively using the gradient descent formula provided in the subject
tmp_theta_0=learningRate*1/m ∑_(i=0)^(m-1)▒〖(estimatePrice(mileage[i]) - price[i])〗
tmp_theta_1=learningRate*1/m ∑_(i=0)^(m-1)▒〖((estimatePrice(mileage[i])- price[i])* mileage[i])〗


* -> PROGRAMS:

----- train.py will read the dataset, perform linear regression and plot a graph.
1. Loading and validating the dataset (CSV file with km and price columns).
2. Normalizing the mileage data to improve gradient descent performance.
3. Performing linear regression using gradient descent.
4. Save the trained parameters theta_0 and theta_1 to a file .txt for future use.
5. Plotting the actual and predicted prices to visualize the model's performance.

----- predict.py will prompt the user for a mileage input, calculate the predicted price based on the learned parameters, and print the result.
1. Prompt for mileage input (ensuring valid input).
2. Load the trained model parameters: read theta_0 and theta_1 from the trained_model.txt file.
3. If no trained model is found, the program should assume theta_0 = 0 and theta_1 = 0.
4. Use the model to predict the price.
5. Display the result/price.

-----precision.py calculates the precision of the price of my model with the actual prices.
1. Load dataset (actual prices)
2. Load my trained model (my predict prices)
3. Calculates the MAE: the average of the absolute differences between the predicted prices and the actual prices in $.


* -> LINEAR REGRESSION:
Linear regression is a data analysis technique that predicts the value of unknown data by using another related and known data value.

https://www.ibm.com/think/topics/linear-regression
What is linear regression?
Linear regression analysis is used to predict the value of a variable based on the value of another variable. The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable.

More Info: https://en.wikipedia.org/wiki/Linear_regression
Linear regression is also a type of machine learning algorithm, more specifically a supervised algorithm, that learns from the labelled datasets and maps the data points to the most optimized linear functions that can be used for prediction on new datasets.
Linear regression plays an important role in the subfield of artificial intelligence known as machine learning. The linear regression algorithm is one of the fundamental supervised machine-learning algorithms due to its relative simplicity and well-known properties.


* -> GRADIENT DESCENT

https://www.ibm.com/think/topics/gradient-descent
What is gradient descent?
Gradient descent is an optimization algorithm which is commonly-used to train machine learning models and neural networks. It trains machine learning models by minimizing errors between predicted and actual results.
https://www.geeksforgeeks.org/gradient-descent-in-linear-regression/

Gradient Descent Overview
Gradient descent is an optimization algorithm used to minimize the cost function, in this case, the error between the predicted and actual prices. The goal is to find the optimal values of the parameters 
theta0 and theta1 that minimize this error.
Cost Function
The cost function being minimized in my implementation is based on the Mean Squared Error (MSE), although it simplifies the gradient calculation by not squaring the errors.


* -> Why Normalize
Normalization helps in speeding up the convergence of gradient descent by ensuring that all features are on a similar scale.

* -> Cost Function
The implementation of the cost function in the gradient_descent function is based on the Mean Squared Error (MSE) principles as per the formula inside the project subject. However it is not exactly the same as the traditional MSE formula. The formula in the subject is not squared.
MSE= 1/m  ∑_(i=1)^m▒(h_θ (x^i )-(y^i ))^2 
MYERROR= 1/m  ∑_(i=1)^m▒(h_θ (x^i )-(y^i )) 


* -> MORE USEFULL INFO ABOUT ML

-> Types of Machine Learning

1. Supervised Learning:
Definition: The algorithm is trained on a labeled dataset, meaning that each training example is paired with an output label.
Common Algorithms:
Linear Regression: Used for predicting a continuous outcome.
Logistic Regression: Used for binary classification problems.
Decision Trees: Used for both classification and regression tasks.
Support Vector Machines (SVM): Used for classification tasks.
Neural Networks: Used for complex tasks such as image and speech recognition.
Applications: Predicting house prices, spam detection, image classification, medical diagnosis.

2. Unsupervised Learning:
Definition: The algorithm is used to find patterns in data without pre-existing labels.
Common Algorithms:
K-Means Clustering: Used to partition data into clusters.
Hierarchical Clustering: Builds a hierarchy of clusters.
Principal Component Analysis (PCA): Used for dimensionality reduction.
Anomaly Detection: Identifies unusual data points.
Applications: Customer segmentation, anomaly detection, market basket analysis.

3. Reinforcement Learning:
Definition: The algorithm learns by interacting with an environment to achieve a goal. It receives rewards or penalties based on actions taken.
Common Algorithms:
Q-Learning: A value-based method for learning policies.
Deep Q-Networks (DQN): Combines Q-learning with deep neural networks.
Policy Gradient Methods: Directly optimize the policy.
Applications: Game playing (e.g., AlphaGo), robotics, autonomous driving.

4. Semi-Supervised Learning:
Definition: Combines a small amount of labeled data with a large amount of unlabeled data during training.
Applications: Text classification, image classification with limited labeled data.

5. Self-Supervised Learning:
Definition: A form of unsupervised learning where the data provides the supervision. Often used in natural language processing (NLP).
Applications: Language modeling, generative models.

-> Frequency of Use for Linear Regression
Linear Regression is one of the simplest and most interpretable machine learning algorithms. It is widely used for the following reasons:
Simplicity: Easy to implement and understand.
Interpretability: The coefficients provide insights into the relationship between features and the target variable.
Speed: Very efficient for small to medium-sized datasets.
Common Use Cases:
Predicting continuous outcomes like prices, sales, or temperatures.
Analyzing relationships between variables in exploratory data analysis.
Despite its simplicity, it remains a valuable tool for many practical applications where interpretability and speed are crucial.
Limitations: Not suitable for capturing complex relationships in the data.
Assumes a linear relationship between features and the target variable.
Conclusion
While linear regression remains a fundamental and widely-used technique in machine learning, it is often complemented or replaced by more advanced algorithms tailored to specific problems. The choice of algorithm depends on the nature of the problem, the data, and the desired outcome.

