# Financial Webscraping and Model Predicting

This repository is dedicated for a python webscraper. This will consist files related to a scraper that will scrape data from Yahoo Finance including stocks, close/open values, volume, and more within. Then, another file is responsible for the prediction of said data using a RandomForestClassifier model, displaying the predictions in a plot-based image and producing reports per the model in .txt files.

Can be run after closing for a day to update stock close price and vary predictions.

More to come...👀

New additions ( After week of 9/28 )

- Added datetime import to update csv per new day/stock open
- Updated csv's path and download to specific folder in both .py files
- Included 'reports' folder for the results of RandomForest model. Consists of f1-score, accuracy, etc.
- Overriding of certain reports and plots depending on new information and if run multiple times per day (same file)

# News Webscraping

This is the news scraper portion of this repository. It attains past news articles over 24 hours, alerting users about new information regarding stocks, finance, etc.

Includes:

- 24-hour fetching
- CSV Updates based on each day upon running
- Overrides information upon running
- Attain sources for a single source right now

Areas to improve:

- Inclusion of more news sources
- Gear proogram towards specific stocks and coins to investigate certain trends/chatter
- Expand to a 7-day span

This tool and data provides opportunity for investors, stock brokers, and salespeople to potentially find their next buy in with the power of machine learning. Model predicting allows for future buy-ins and the webscraping provides resources. A summarizer still needs to be made for the news articls and hopefully, I can expand this into a webpage during the summer. 
