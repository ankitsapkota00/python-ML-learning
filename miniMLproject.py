import numpy as np
from sklearn.linear_model import LogisticRegression

    
#hours studied     attendance percentage      assignment score
X = np.array(
            [[10, 55, 75],
             [2,  25, 33],
             [15, 95, 100],
             [10, 67, 79],
             [23, 85, 85],
             [12, 77, 100],
             [11, 51, 55],
             [23, 89, 81],
             [12, 77, 45],
             [11, 49, 75],
            ]).reshape(10,3)

#pass - 1, fail - -0
Y = np.array([1,0,1,1,1,1,0,1,0,0]).reshape(10,)

print("X's shape is",X.shape,"\n")
print("Y's shape",Y.shape,"\n")
print(X[:3])
print(Y[:3])

X_train = X[:7]
X_test = X[7:]
Y_train =Y[:7]
Y_test = Y[7:]

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)


Y_pred =[]
for row in X_test:
    if row[1] > 50 and row[2] > 60:
        Y_pred.append(1)
    else:
        Y_pred.append(0)    

print(Y_pred)
print(Y_test)   

correct = 0
for i in range(len(Y_test)):
    if Y_pred[i] == Y_test[i]:
        correct += 1

accuracy = correct/(len(Y_test))
print("Accuracy is ",accuracy * 100,"%")

model = LogisticRegression() #Create an empty brain that knows how to learn

model.fit(X_train,Y_train)
'''Look at patterns in X_train
    Adjust internal weights
    Try to match Y_train'''

Y_pred_ml = model.predict(X_test)

correct = 0
for i in range(len(X_test)):
    if Y_pred_ml[i] == Y_pred[i]:
        correct += 1


accuracy = correct/(len(Y_test))
print("ML Accuracy:", accuracy * 100, "%")     

print("Y_test:", Y_test)
print("Rule-based:", Y_pred)
print("ML:", Y_pred_ml)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

''' this tells
How important each feature is
Whether it contributes positively or negatively
'''

#manually compute the score for the sample it got wrong.
#z=w1​x1​+w2​x2​+w3​x3​+b

sample = X_test[-1]
z = (model.coef_[0][0]* sample[0] + model.coef_[0][1] * sample[1] 
     + model.coef_[0][2] * sample [2] + model.intercept_[0])
print("Raw score z:", z)