# Fake News Recognition & Classification Project

## Project Overview 
With the abundance of media outlets in the modern world it has become increasingly difficult to separate credible news from the unreliable. Because of this, we have decided to create an application that allows a users to input articles into a website and return the validity of the article contents and the category type of the article.

From this analysis, we hope to answer the following questions:
- What categories of articles are more likely to include false information?
- What words or phrases tend to show up the most in fake news compared?

## Architecture
In order to accomplish our goal, we've used the following tools to develop the different aspects of our application:
- Website development: HTML, CSS, Bootstrap, D3 & Flask
- Data Cleaning & Preprocessing: Beautiful Soup, NLTK for Stop Word removal
- NLP Classification Models: Sci-kit Learn & pre-trained Hugging Face model (VERIFY THIS ONE)
- Database: MongoDB
- Visualizations: MatPlotLib
- Deployment: Heroku

(ADD Architecture Diagram here)

## Project Milestones
1. Identify Data Sources to train models
    - Article Categories: https://www.kaggle.com/datasets/rmisra/news-category-dataset
    - Article Validity: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

2. Preprocessing of datasets: Categorical dataset web scraping and removal of stop words
    - Utilize BeautifulSoup to pull out the article contents to allow for training of models

3. Training of Validity model: splitting the datasets into training and testing subsets and using those datasets to test which model types have the best accurary. After testing Naive Bayes, Logistical Regression, Decision Tree and Random Forest models, we selected the Decision Tree model due to it's highest rate of accuracy.

4. Training of Categorical model:

5. Website development & database creation: create a site utilizing HTML, CSS and Bootstrap to allow for the input of an article, return of a prediction and display visualizations. The Flask app supports the back end interaction of the website, database and models.

6. Application Deployment: Heroku

## Project Challenges
- At the beginning of the project, we found a training dataset that included both the category and whether the article was determined to be true or false. The issue that we ran into was that the data was not very clean and didn't lend itself to be very easy to work with for our purpose. This resulted in our team deciding to switch to the 2 datasets approach that accomplished our goal
- The categorical dataset that we decided to use only included a link to the article instead of the full content which required us to scrape the data from the site. With scraping, we ran into 2 different problems: 
    1) The site limiting the amount of articles one person could scrape
    2) Other team members gaining access to the S3 bucket to be able to scrape and store the articles
    
These issues resulted in a limited amount of articles that we were able to scrape and ultimately train the model with.

## Results