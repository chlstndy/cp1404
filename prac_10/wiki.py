import wikipedia

while True:
    search_input = input("Enter a page title or search phrase (or press Enter to exit): ")

    if not search_input:
        break

    try:
        page = wikipedia.page(search_input, autosuggest=False)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation page found. Please provide a more specific search term.")
    except wikipedia.exceptions.PageError as e:
        print("Page not found. Please check your input.")
