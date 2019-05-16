# Twitter Sentiment Analysis

This repository consist of 2 files and are created as a showcase samples for the blog - https://medium.com/syncfusion/twitter-sentiment-analysis-dashboard-on-event-management-fd97c3154671

1. TwitterSentimentAnalysis.xml - Syncfusion Data integration platform template contains a sample dataflow to gather twitter tweets, process and clean the data, perform sentiment analysis over the text and move the data into SQL Server for Dashboarding requirements.
Refer this link to deploy the template within Data integration platform - https://help.syncfusion.com/data-integration/how-to/working-with-templates

2. sentiment.py - a basic python script to perform sentiment analysis over input text.

To configure the environment to run Python sentiment analysis script within DIP, follow these steps:

a. Install Stanford NLP package from this link - https://stanfordnlp.github.io/CoreNLP/.
   
   Start the server using the following command.
    
    C:\<installed location>\stanford-corenlp-full-2018-10-05> java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000
    
    Note: Java in the command refers to JAVA_PATH, If the JAVA_PATH is set already just run the above command or else mention the JAVA_PATH in place of java used in the command.

b. Install the “pycorenlp” python package using below command.
   
   pip install pycorenlp

c. Use the (sentiment.py) Python script to perform sentiment analysis. It is a very basic one that uses default settings in CoreNLP to gauge sentiment.
