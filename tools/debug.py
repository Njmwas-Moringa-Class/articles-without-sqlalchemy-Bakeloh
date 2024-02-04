#!/usr/bin/env python3



import os
import sys
sys.path.append('../lib') # Assuming 'lib' is one level above 'tools'
print(os.getcwd())
print(sys.path)
print(os.listdir())

import ipdb

from Author import Author
from Magazine import Magazine
from Article import Article

# import sys
# sys.path.append('modules')  # Adjust the path to the correct location

# from Author import Author
# from Magazine import Magazine
# from Article import Article

if __name__ == '__main__':
    #  WRITE YOUR TEST CODE HERE ###
    

    author1 = Author("50 Cent")
    author2 = Author("Ngugi wa Thiongo")
    
    ipdb.set_trace()
    
    magazine1 = Magazine("Times", "Kenyan Times")
    magazine2 = Magazine("Sacco Review", "SASRA")

    # Insert a breakpoint here to interact with the terminal
    ipdb.set_trace()

    article1 = author1.add_article(magazine1, "Financial Times")
    article2 = author2.add_article(magazine1, "How Not to Save")
    article3 = author1.add_article(magazine2, "Unemployment Impact on Saccos")

    # Test code
    print("Authors:")
    for author in Author.all():
        print(author.name())

    print("\nMagazines:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} - {magazine.category()}")

    print("\nArticles:")
    for article in Article.all():
        print(f"{article.title()} by {article.author().name()} in {article.magazine().name()}")

# DO NOT REMOVE THIS
    ipdb.set_trace()
