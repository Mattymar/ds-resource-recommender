# ds-resource-recommender

In this project, I built a tool that produces a list of recommended blog posts from a full text input. While extensions are needed to make this tool more valuable to data scientists and students (in progress!), the idea behind this naive implementation is that we are performing a similarity comparison between a full text input and a large corpus of blog posts and other resources.  The goal is to find resources that are complementary to one's current studies, either to provide an alternative perspective or give an idea of what to study next.

You can follow my process by viewing the Main_Notebook.ipynb file. In addition to this, you will find the files used to compile my database of blog posts, as well as a file that walks through the building of the actual tool, in the form of a Flask app.

In the main notebook, there is also a nifty bonus section where we make happy little word clouds to show some nice clustering in our corpus.


## Tools used
+ Scikit-learn (TF-IDF and KMeans)
+ NLTK
+ WordCloud
+ Flask
+ PyMongo
+ readability
+ feedparser
+ listparser
+ html2text


## Some Results

** Random Search for Hyper-Parameter Optimization (paper) **

<img src="https://github.com/Mattymar/ds-resource-recommender/blob/master/grid_search_rec.png" width=512>

-----

** Deep Learning Book Ch. 9 - Convolutional Neural Networks **

<img src="https://github.com/Mattymar/ds-resource-recommender/blob/master/cnn_rec.png" width=512>

-----

** Sample word cloud from "AI" cluster **

<img src="https://github.com/Mattymar/ds-resource-recommender/blob/master/robot_cloud_gray.png" width=256>