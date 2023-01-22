from src.input_data import get_wiki_summary, get_random_wiki_page, get_wiki_page


def test_get_wiki():
    assert len(get_wiki_summary()) > 0


def test_get_random_wiki_page():
    assert len(get_random_wiki_page()) > 0


def test_get_wiki_page():
    assert len(get_wiki_page("Monty Python")) > 0
