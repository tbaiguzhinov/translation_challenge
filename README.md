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
