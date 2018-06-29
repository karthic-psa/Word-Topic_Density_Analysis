# Word-Topic_Density_Analysis #

A word/topic density analyzer to take in an URL and identify the most relevent words and topics in that page.

## About the Project: ##

In SEO, it’s important to write good content and signal to the search engines what your article or page is about. One way to ensure that is by focusing your content on the core topics. In this assignment, you’ll be responsible for building an engine that will take any URL and identify the most relevant topics on the page.

## Dependencies for Project: ##

1. Python 2.7
2. BeautifulSoup
3. NLTK - not used at this point; can be used in the future once the projects scales to handle lemmatization (can be used stemming or lemmatization)

## Instructions on how run the project: ##

1. Make sure you have Python 2.7 and BeautifulSoup installed
2. Clone or download the repo
3. Go to the root directory of the project where the ```main.py``` file is located
4. From your terminal or command line, type ```python main.py <URL>```


## Design ## 

1. First, we parse through the URL page got as an input from the user using urllib2 to read all the site data and BeautifulSoup to create a soup object (of the page) that makes parsing the data of the page easier
2. Create a dictionary of stop words - with the ```stopwords.py``` file using the nltk generic stop words or add words to the stop words file on your own in the ```stopwords.txt``` file, if you want to avoid specific words and topics you are not interested about or find them umipmorant
3. Next, once we get a response and get our site data and the soup object, we use our methods to filter the data according to our needs and remove any stop words in the data we are parsing
  - Here is were the code and design is scalable and can be experimented on as per our requirments, by adding different weights to different tags we are going through the HTML content (HTML parse-tree search)
  - Also you can add, edit or remove tags and weights that you dont want parse
4. A Linked List has been used to get ordered data of top topics and words ordered by weight and frequency

## Comments and Notes ##

1. Just an intial implemetation of the code and structured planned,
  - [ ] Need to figure out if we can optimize the code in order to achieve better time and memory efficieny, which is critical when the project scales and evolves
  - [ ] Keep improving the algorithm to better track important topics and words in the page and their usage
  - [ ] Need to handle lemmatization of words - (did not need it for pages tested; hence did not include it)
  - [x] Error and exception handling are taken care of to an extent, but can be improved
  
2. Followed Test Driven Development (TDD) while building the views. However, need to perform more robust and automated testing to ensure proper functionality (Performed unit testing for the features provided in the application and ensured it works properly)
