#This component takes a string of text and seperates everything out of it that is useless so that we can actually do a useful text analysis.

from nltk.stem.snowball import SnowballStemmer
import string
import re

def textParse(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        
        example:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        """

    f.seek(0)  ### file start
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        words = text_string

        ###multi spacial stemmer, don't know how to make single spaces yet, don't care.
        stemmer = SnowballStemmer("english", ignore_stopwords=True) 
        p = re.compile('\w+|\W')
        words = p.findall(text_string)
        words = [stemmer.stem(w) for w in words]
        words = "".join(words)        




    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = textParse(ff)
    print text



if __name__ == '__main__':
    main()