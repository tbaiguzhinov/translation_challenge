# Translation Service Challenge

This is a microservice providing a JSON API, working with word definitions/translations taken from Google Translate.

## Endpoints

### GET /api/word/

Returns the definitions, synonyms, translations and examples of a provided word.
Possible query params:

-

### GET /api/words/

Returns the list of words stored in the database.

### DELETE /api/word/

Deletes a provided word from the database.

## Considerations

- Google Dictionary API has been depricated since 2011. It is possible, however, to parse the response on https://translate.google.com/details page, using BeautifulSoup for instance. However, there is an official API existing on api.dictionaryapi.dev, which I use in app.definition_utils.py, which does exactly this. In the event, this API stops working, there is Oxford dictionary API which should normally be used by Google (but the support is only for English), or we could eventually create our own parser.
