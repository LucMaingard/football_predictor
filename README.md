# football_predictor
testing different supervised learning algorithms for an English Premier league match predictor.

## Overview
The aim of this project was to test the performance of different machine learning algorithms on a very difficult and multifaceted problem. The problem at hand is predicting the outcomes of premier league football matches. Football is an immensely popular game worldwide and predicting the outcomes of a match is an incredibly difficult, nuanced challenge. The data was taken from www.football-data.co.uk, a great source of highly detailed historical data, looking at the last 10 seasons in the premier league. 

## Features
A total of 6 features were decided on after an initial EDA to find the most relevant and leave out the most redundant features. The features used were for each game: Number of shots, number of shots on target, number of fouls, number of corners, number of yellow cards, and bet365 odds. 

## Algorithms
The algorithms used were naive bayes, logistic regression, random forest classifier, and a LSTM neural network. 

## Results
Interestingly the top performer was a Random Forest performing at 60%, closely followed by Logistic Regression and Gaussian Naive Bayes which had an accuracy of 59%. The bottom performer was the LSTM Neural Network, which had an accuracy of 47%. 

Precision, Recall, F1-Score:
Random Forrest (max_depth=0, random_state=7) Classification Report (normalised)
               precision    recall  f1-score   support

          -1       0.57      0.64      0.60       312
           0       0.36      0.14      0.20       254
           1       0.66      0.82      0.73       479

    accuracy                           0.60      1045
   macro avg       0.53      0.53      0.51      1045
weighted avg       0.56      0.60      0.57      1045


Log Reg Classification Report (standardised)
              precision    recall  f1-score   support

          -1       0.56      0.69      0.62       312
           0       0.29      0.11      0.16       254
           1       0.66      0.78      0.72       479

    accuracy                           0.59      1045
   macro avg       0.50      0.53      0.50      1045
weighted avg       0.54      0.59      0.55      1045


The labels:  “-1” refers to “away wins”; “0” to “draws” and “1” to “home wins”. As can be seen above both Random Forest and Logistic Regression performed the best on predicting home wins, and worst on draws. This is unsurprising as logic would dictate that playing at home results in an advantage and an increased likelihood of coming away with a win. While draws are the least likely of the three outcomes and are thus unpredictable. 

## Usage

### Packages Required:
- python 3>
- pandas
- numpy
- scipy
- scikit-learn
- seaborn
- matplotlib

### Instructions
Simply download the Jupyter Notebook "footy_pred.ipynb" and the accompanying "E(n).csv"'s and run it in any IDE.
