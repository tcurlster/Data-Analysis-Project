# Fake News Recognition & Classification Project

## Overview
With the abundance of media outlets in the modern world it has become increasingly difficult to separate credible news from fakes and clickbaits. This project aims to help the readers navigate the sea of news articles by providing a credibility scale and classifying news into various categories, ranging from “Satire” to “Hate News” and everything in between.

## Goals
1. Create a machine learning model that determines the validity of information contained within news articles and classifies that article into several categories
2. Develop a website that takes the input of a news article and outputs whether it is real or fake and puts that article into a pre-defined category based on previous learning

## Data Source
- https://github.com/several27/FakeNewsCorpus/blob/master/websites.csv

## Milestones
1. Create a database to store the dataset
    - Use an AWS RDS database to store the original dataset for training the models. 
    - Due to the high volume of data, Google Collab or DeepNote will be used to extract, transform, and then load the data back into the RDS database. 

2. Build NLP model to calculate the credibility confidence score
    - Preprocessing and tokenizing of dataset in preparation of adding it to the model
    - Use train, test, split to create a training and testing dataset for model evaluation
    - Use Scikit-Learn and imb_learn libraries to test multiple unsupervised classification machine learning models that will be evaluated for performance, optimized and the best performing model will be selected for the end product.
    - Google Collab/PySpark or DeepNote will be utilized to train the models due to high volume of training data (9+ mln records)
    - OpenAI’s GPT-2 and HuggingFace NLP models will be used for reference


3. Build classification algorithm to classify the news in various categories
    - Use the preprocessed training and testing data from milestone II for model evaluation
    - Use Scikit-Learn and imb_learn libraries to test multiple unsupervised classification machine learning models that will be evaluated for performance, optimized and the best performing model will be selected for the end product.
    - PySpark and Google Collab or DeepNote will be utilized to train the models due to high volume of training data (9+ million records)


4. Build a user-facing website for analyzing the news
   - The website will provide an ability for the user to paste the desired news article or a link. The user will then be able to analyze the article by running the classification and NLP algorithms and results will be displayed.
    - Flask application will be built to support the back end functionality of the website
    - Front end will leverage html, css, bootstrap. 
 
						
5. Additional News/Source Analytics (optional) within website
    - As time allows, we will be including additional news analytics for the user, such as:
        - % of credible articles from the source they are checking
        - Some semantic words/structures that point to news being credible/not credible, etc.
    - Plotly Dash and/or d3.js would be used to build the graphics.

