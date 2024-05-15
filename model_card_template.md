# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Developed by Pianjo Glad, 2024, v1.
The model type is a logistic regression model. For more information, see Udacity project, "Deploying a Maching Learning Model with FastAPI". Project can be cited as "Deploying a Machine Learning Model with FastAPI - pglad". For further information, contact pglad5@wgu.edu.

## Intended Use
The Primary intended use is to predict someones income based on background informaiton about them. The Primary intended use was made for educational purposes in learning about machine learning. Out-of-scope uses include applying to real life situations. There needs to be more data in the training model. 

## Training Data
The Census dataset was used. It is publicly available and generally considered accurate. 

## Evaluation Data
The Census dataset was used. It is publicly available and generally considered accurate. 

## Metrics
_Please include the metrics used and your model's performance on those metrics._
Precision: 0.7319 | Recall: 0.2807 | F1: 0.4058


## Ethical Considerations
The data does use sensitive data (age, race, etc). It is not intended to inform decisions. Assumption on salary is not necessarily a positive for any individual person. The risks were considered but remain unknown. However, a user should be cautious in how they apply the usage of this model. 

## Caveats and Recommendations
The data set did not seem to include children or older adults. The data also did not split ethnicities very well (combining multiple like asian/pacific-islanders). This could result in disproporitionate erros within these groups. 
