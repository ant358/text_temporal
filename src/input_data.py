# %%
import wikipedia
import logging

wikipedia.set_lang("en")


def get_wiki_summary(name="Monty Python", sentences=10) -> str:
    """A wikipedia fetcher function

    Args:
        name (str, optional): The name of the page to fetch.
            Defaults to "Monty Python".
        sentences (int, optional): The number of sentences to fetch.
            Defaults to the first 10
            can be no greater than 10.

    Returns:
        str: The fetched summary of the wikipedia page
    """
    return wikipedia.summary(name, sentences=sentences)


def get_random_wiki_page(pages=2) -> list[str]:
    """Fetch a random wikipedia page title. Defaults to 2 pages
    If a single page is returnd it is a string, if multiple pages
    are returned it is a list of strings. So we always return a
    list with 2.

    Args:
        pages (int, optional): The number of pages titles.
        Defaults to 2.

        Returns:
            list[str]: The titles of the random pages
    """
    return wikipedia.random(pages=pages)


def get_wiki_page(
    title="Monty Python",
) -> str:
    """Fetch a specific wikipedia page content

    Args:
        title (str): The title of the page

    Returns:
        str: The page content
    """
    try:
        page = wikipedia.page(title).content
    except wikipedia.exceptions.DisambiguationError as e:
        page = wikipedia.page(e.options[0]).content
        logging.exception(f"DisambiguationError: {e.options}, using {e.options[0]}")
    except wikipedia.exceptions.PageError as e:
        logging.exception(f"PageError: {e}")
        page = f"{title} not found"

    return page


if __name__ == "__main__":
    print(get_wiki_summary())

# %%
