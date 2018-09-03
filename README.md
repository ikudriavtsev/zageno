# Finding the shortest distance (number of words) in a given text file

The core implementation is done in `challenge.py`. The solution is __not__ case insensitive. Also, it doesn't solve for
*big* files, although the function in `challenge.py` can be used to operate on a chunk of text from such a file. The
problem of resulting words appear in different chunks is actual in this case and can be traded off by increasing the
size of each chunk.

Word extraction from text is done in a naive way by splitting the text by whitespace and then trying to sanitize the
word with some most common grammar punctuation.

## Running

The command to run the solution compiles like the following (from within the repo root directory):
`python main.py <text file path> <word1> <word2>`

For instance:
```
$ python3 main.py ./example_provided.txt motivation development
Distance equals 2 between words `motivation` and `development` in file ./example_provided.txt
```

Or:
```
$ python3 main.py ./example_custom.txt computer system
Distance equals 1 between words `computer` and `system` in file ./example_custom.txt
```

## Tests

Run the following command from within the repo root directory:

`python -m unittest discover`
