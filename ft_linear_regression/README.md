* -> GOAL:
Project goal is to implement gradient descent with the provided formulas to train a linear regression model for predicting car prices.

Linear Regression Formula: After training, you’ll use a linear function
estimatePrice(mileage) = theta_0 + (theta_1 ∗ mileage)

Implement Gradient Descent: Update the parameters (theta_0, theta_1) iteratively using the gradient descent formula provided in the subject
tmp_theta_0=learningRate*1/m ∑_(i=0)^(m-1)▒〖(estimatePrice(mileage[i]) - price[i])〗
tmp_theta_1=learningRate*1/m ∑_(i=0)^(m-1)▒〖((estimatePrice(mileage[i])- price[i])* mileage[i])〗


* -> PROGRAMS:

- train.py will read the dataset, perform linear regression and plot a graph.
1. Loading and validating the dataset (CSV file with km and price columns).
2. Normalizing the mileage data to improve gradient descent performance.
3. Performing linear regression using gradient descent.
4. Save the trained parameters theta_0 and theta_1 to a file .txt for future use.
5. Plotting the actual and predicted prices to visualize the model's performance.

- predict.py will prompt the user for a mileage input, calculate the predicted price based on the learned parameters, and print the result.
1. Prompt for mileage input (ensuring valid input).
2. Load the trained model parameters: read theta_0 and theta_1 from the trained_model.txt file.
3. If no trained model is found, the program should assume theta_0 = 0 and theta_1 = 0.
4. Use the model to predict the price.
5. Display the result/price.


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

