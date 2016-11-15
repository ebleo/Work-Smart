"""

https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1#.w2d03bdnd

http://searchsoa.techtarget.com/definition/object-oriented-programming

http://stackoverflow.com/questions/4841436/what-exactly-does-do-in-python

https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/

https://www.analyticsvidhya.com/learning-paths-data-science-business-analytics-business-intelligence-big-data/learning-path-data-science-python/

"""
url = []

categories = ["Python", "AI", "Object Oriented Programming"]

def get_cat():
    for i in range(len(categories)):
        print(str(i), ". ", categories[i])


print("This is a list of different links that you've gathered")
print("They've been manually sorted based on the category")
print("here are the categories:")
get_cat()
