from nlplogic.corenlp import get_phrases

def test_get_phrase():
    assert "state university" in  get_phrases("university at buffalo")
