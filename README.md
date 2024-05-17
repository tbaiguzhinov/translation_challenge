# Translation Service Challenge

This is a microservice providing a JSON API, working with word definitions/translations taken from Google Translate.

## Features

### GET /api/word/<str>

Returns the definitions, synonyms, translations and examples of a provided word.
Possible query parameters:

- target ('es' by default) - target translation language

### DELETE /api/word/

Deletes a provided word from the database.

### GET /api/words/

Returns the list of words stored in the database.
Possible query parameters:

- page (1 by default) - the number of the page with results
- limit (10 by default) - the limit of words per page
- sort_ascending (True by default) - sorts the words in ascending alphabetical order
- filter_word (None by default) - a word or a combination of letters, using which a search is done in the database
- include_details (False by default) - specifies whether the result should include translations, definitions, examples and synonyms.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Docker](https://www.docker.com/) installed
- [Docker Compose](https://docs.docker.com/compose/) installed

### Installation

1. Clone the repository:

   ```
   git clone git@github.com:tbaiguzhinov/translation_challenge.git
   ```

2. Navigate to the project directory:

   ```
   cd translation_challenge
   ```

3. Build and start the Docker containers:

   ```
   docker-compose up -d
   ```

### Local developement

Here is the way to install pre-commit hooks and poetry

1. Create virtual environment

   ```
   python3 -m venv venv
   ```

2. Activate virtual environment

   ```
   source venv/bin/activate
   ```

3. Install requirements, including pre-commit hooks
   ```
   pip3 install -r requirements.txt
   ```

Now when you do `git add .` and `git commit -m "<commit-message>"`, pre-commit hooks run automatically.

### Configuration

The project uses environment variables for configuration. Edit the `.env` file and provide the necessary values, such as database connection details and API keys:

- MONGODB_URL - the url for MongoDB database
- GOOGLE_API_KEY - google API key for Google Translate
- AUTHENTICATION (optional) - if set to True, switches on authentication by Token

### Testing

Run tests with command:

```
 python3 -m pytest
```

Current coverage is 98%.

## Usage

Visit `http://0.0.0.0:8000/docs` in your browser to access the Swagger page of the application.

## Considerations

Google Dictionary API has been depricated since 2011. It is possible, however, to parse the response on https://translate.google.com/details page, using BeautifulSoup for instance. However, there is an unofficial API existing on api.dictionaryapi.dev, which I used and it does exactly this. In the event, if this API ceases to function, there is Oxford dictionary API which is reportedly used by Google, or we could eventually create our own parser.
