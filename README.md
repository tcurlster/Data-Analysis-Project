# Fake News Recognition & Classification Project

## Overview
With the abundance of media outlets in the modern world it has become increasingly difficult to separate credible news from fakes and clickbaits. This project aims to help the readers navigate the sea of news articles by providing a credibility scale and classifying news into various categories, ranging from “Satire” to “Hate News” and everything in between.

## Goals
1. Create a machine learning model that determines the validity of information contained within news articles and classifies that article into several categories
2. Develop a website that takes the input of a news article and outputs whether it is real or fake and puts that article into a pre-defined category based on previous learning

## Data Source
- Article Categories: https://www.kaggle.com/datasets/rmisra/news-category-dataset
- Article Validity: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

## Milestones
1. Scrape article from links provided in categorical dataset for training the model
    - Utilize BeautifulSoup to pull out the article contents and store back into the dataframe or MongoDB

2. Build NLP model to calculate the credibility confidence score
    - Preprocessing and tokenizing of dataset in preparation of adding it to the model
    - Use train, test, split to create a training and testing dataset for model evaluation
    - Use Scikit-Learn and imb_learn libraries to test multiple unsupervised classification machine learning models that will be evaluated for performance, optimized and the best performing model will be selected for the end product.
    
    Or
    - Use a pre-trained HuggingFace Model that accomplishes the same goal
    - DeepNote will be utilized to train the models 
    - OpenAI’s GPT-2 and HuggingFace NLP models will be used for reference

3. Build classification algorithm to classify the news in various categories
    - Use the preprocessed training and testing data from milestone II for model evaluation
    - Use Scikit-Learn and imb_learn libraries to test multiple unsupervised classification machine learning models that will be evaluated for performance, optimized and the best performing model will be selected for the end product.
    
    Or

    - Use a pre-trained HuggingFace Model that accomplishes the same goal
    - DeepNote will be utilized to train the models

4. Build a user-facing website for analyzing the news
   - The website will provide an ability for the user to paste the desired news article or a link. The user will then be able to analyze the article by running the classification and NLP algorithms and results will be displayed.
    - Flask application will be built to support the back end functionality of the website
    - Front end will leverage html, css, bootstrap

5. Create a database to store the input data to interact with the website
    - Use a MongoDB database that is incorporated into Flask to store articles that are input into the site and then ran within the model

6. Additional News/Source Analytics (optional) within website
    - As time allows, we will be including additional news analytics for the user, such as:
        - % of credible articles from the source they are checking
        - Some semantic words/structures that point to news being credible/not credible, etc.
    - Plotly Dash and/or d3.js would be used to build the graphics.

