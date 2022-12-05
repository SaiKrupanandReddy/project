


# Reading the file

# read the dile
with open("PassagesFromMoonwalkingWithEinstein.txt", "r+") as r:
    data = r.read().strip().split("\n")
    final_data = []
    #remocve the numbering as it is the first two charactes
    for dat in data:
        #remove empty lines
        if len(dat)>0:
            final_data.append(dat[2:])
    r.close()

len(final_data)



for dat in final_data:
    print(dat, "\n")


# POS tagging using nltk

## QUESTION 2.

# Nltk will be used

import nltk
from IPython.display import display
from nltk.tree import Tree

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
from nltk import word_tokenize


for sent in final_data:
    tags = nltk.pos_tag(word_tokenize(sent), tagset = "universal")
    print(f"Sentence {sent} tags are :\n\t", tags, "\n\n")




# ### Dependency and Consistency Parsing.
# - A research done showed stanza from stanfold university as best for getting consistency parsing.  For dependency, spacy remained the best.
# 
# - All these are going to be done inline.
# - Below is a function that will take a sentence and output the dependency and contigency parsings of the sentence

# In[5]:


# install stanza
get_ipython().system('pip install stanza')


# In[6]:


# create stanza model for english words
import stanza
doc_model_nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency', download=None)


# In[7]:


# first import spacy and get spacy model into working
import spacy
nlp = spacy.load("en_core_web_sm")

def dependency_parser(sentence):
    """
    Create Dependency parsers using spacy module.
    It uses displacy module of spacy to print the results on a graph.

    :params :
        sentence which is a string to be analysed
    Model returns None
    """
    parsed_obj = spacy.displacy.render(nlp(sentence), style = "dep", jupyter=True)
    #display parsed object
    display(parsed_obj)
    return None


# - Create a Function for consitituency parsing.
# - The function accepts a string and uses stanza to parse it to its consituents.
# - Stanza module is used here as suggested above

# In[8]:


get_ipython().system('pip install svgling -q')


# In[9]:


# function for consistituency parsing
def constituency_parser(sentence):
    """
    Create constituency parsers using spacy module.
    It uses stanza module parse the sentence and create tree then nltk is used to draw a graph.

    :params :
        sentence which is a string to be analysed
    Model returns None
    """
    parsed_cons_tree = doc_model_nlp(sentence).sentences[0].constituency
    #convert it to a tree object and display
    display(Tree.fromstring(parsed_cons_tree.pretty_print()))
    return None


# In[9]:





# - We then Iterate through the above 5 sentences while passing each sentence to above 2 functions to display these mappings
# 
# 

# In[10]:


for each_data in final_data:
    print(f"**********{each_data}************")

    print("Consisitituency Parsing Visualization")
    #consistency parsing
    constituency_parser(each_data)
    #dependency parsing
    print("Dependency Parsing Visualization")
    dependency_parser(each_data)
    print("\n\n")


# In[10]:





# In[10]:




