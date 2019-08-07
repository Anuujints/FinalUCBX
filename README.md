# FinalUCBX
Final group project—Peter, Ivan, Michel, Ema and Anu.

<<<<<<< HEAD
Acronyms 
Centers for Disease Control and Prevention’s (CDC)
Inﬂuenza-like Illness (ILI) 

The Epidemiology and Prevention Branch in the Influenza Division at CDC collects, compiles and analyzes information on influenza activity year-round in the United States and produces FluView, a weekly influenza surveillance report, and FluView Interactive, which allows for more in-depth exploration of influenza surveillance data.

nationwide staring from 1997/98
statewide starting from 2010


Data sources for final project


1. EHR data obtained from athenahealth:- collected from 2009 to 2016
    3 independent variables extracted from this data source 
        (flu visit counts)/ (total patient visit counts)
        (ILI visit counts)/ (total patient visit counts) and
        (unspecified viral or ILI visit counts)/ (total patient visit counts)

2.  Google trend data: - collected from October 2009 to 2016
    We will extract 129 search query term, will be 129 independent variablesTo build our machine learning models

3.  CDC historical ILI values: collected from 2009 to 2016
    unweighted ILI activity level
=======

# Objective of this project 
## build machine learning model that predicts flu activity in the US within 1 week, 2 week, 3 week and 4 week ahead of CDC ILI epi weeks. 

### Data source 
Data were extracted from already available and relatively clean data source, previously used for influenza forecasting.
#### EHR data obtained from athenahealth
#### CDC historical Influenza Like Illnesses (ILI) values
#### Google trend data 

We limit the year based on athenahealth Electronic Helath Record (EHR) data availability which starts from 2009 week 40 and ends 2016 week 20. 
Dataset is sliced by epi week for model building.
Dataset year window is ranges from first week of October to second week of May in each flu season. 

Example 
2009 – 2010 flu season starts on epi week 40, 2009 (first week of October) and ends on epi week 20, 2010 20 (mid-May))
##### -	week 40, 2009 to week 20, 2010 
##### -	week 40, 2010 to week 20, 2011
##### -	week 40, 2011to week 20, 2012
##### -	week 40, 2012to week 20, 2013
##### -	week 40, 2013 to week 20, 2014
##### -	week 40, 2014 to week 20, 2015
##### -	week 40, 2015 to week 20, 2016

The maximum season week in each ﬂu season is 33 or 34. 
Total number of weeks count  is 231. 

## Independent variables 
#### Athena EHR 
    -	flu visit counts/total patient visit counts
    -	ILI visit counts/total patient visit counts and
    -	unspecified viral or ILI visit counts/total patient visit counts
#### CDC ILI
    -	unweighted ILI activity level selected as independent variable
#### Google trend
    -	129 flu query search terms
    
## Dependent variables 
-	ILI_lag_week 1  
-	ILI_lag_week 1  
-	ILI_lag_week 1  
-	ILI_lag_week 1  

## Training and testing dataset defined 
### Training data set 
#### week 40, 2009 to week 20, 2015

### Testing data set 
#### week 40, 2015 to week 20, 2016

Machine learning model built using dataset sliced by epi week 40 t0 20 (see folder name FinalUCBX\flu_indicator\data\ML_models_on week40-20epiweek

    Gradient Boosting Regression
    Random Forest Regression  
    SVM Regression 
    kNN Regression 
    Deep Neural Networks Regression

Please checkout STATS xls summary obtained from the above ML models in folder(FinalUCBX\flu_indicator\data\ML_models_on week40-20epiweek) file name (ILI_weeks_testscores_allMLmodels).

We built feature vector importance analysis and run two top machine learning models, using 74 feature vectors and 20 feature vectors. 
Checkout folder (FinalUCBX\flu_indicator\data\ML_models_on week40-20epiweek)
 
#### Conclusion from feature vectors analysis

There is no significant test score performance improvement in terms of r_score.
Increment noted on test scores
Mean Squared Error(MSE) and 
Mean Absolute Error(MAE). 
The lowest MSE and/or MAE the better the machine learning model predicting ability. 
Based on this analysis and proof of evidence we decided run our machine learning models on all feature vectors and we summarize results.
Please checkout summary STATS xls file in folder(FinalUCBX\flu_indicator\data\feature_vector_importance_analysis_epiwk40-20)

We also noted successive decrement on r_score and increments on MSE and/or MAE as we perform predicting ILI weeks in all machine learning models. This means all machine learning models works consistently. 

Please check out feature importance percentages in folder name  
ML_models_on week40-20epiweek (ILINet_by_ILIweek_Random_Forest_Regressor ipynb) and 
feature_vector_importance_analysis_epiwk40-20 (ILINet_by_ILIweek_Gradient_Boost_Regressor-w74_important_features ipynb, ILINet_by_ILIweek_Gradient_Boost_Regressor-w74_important_features ipynb)

Most important feature vector: -
(0.889018040832374, 'CDC_Unweighted_ILI') from all 133 feature vectors
(0.88892895726736, 'CDC_Unweighted_ILI') from all 74 feature vectors
(0.8974309613919637, 'CDC_Unweighted_ILI') from all 20 feature vectors

Based on feature vector analysis result displayed above, CDC_Unweighted_ILI is the fundamental feature vector in explaining the variability of our regression models. Removing other related google search terms including feature vectors with scored zero, no evidence on improvement noted on the explanatory power of this feature vector. 

This feature vectors analysis adds proof of evidence on using internet based information helps in augmenting the predictive power of machine learning models in predicting flu. 

We also noted huge gap between on training and testing data test score with Neural Networks. This shows Neural network works good on big dataset on on small dataset. Please checkout test scores xls file and ipynb for DNN regression in folder (FinalUCBX\flu_indicator\data\ML_models_on week40-20epiweek)
      
      
      
   
      

       
 
>>>>>>> 2fc1866c121590abe744ed1db0b3a004cce3624e
