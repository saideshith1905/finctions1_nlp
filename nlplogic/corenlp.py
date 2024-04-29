from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Searching wikipedia"""
    
    print(f"searcing for name:{name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """summarizing wikipedia"""
    print(f"finding wikipedia summary for name:{name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Getting text blob"""

    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """finding wikipedia name and return back phrases"""

    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases


ub_text = wikipedia.summary("university at buffalo")
