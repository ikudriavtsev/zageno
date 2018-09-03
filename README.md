# Finding the shortest distance (number of words) in a given text file

The core implementation is done in `challenge.py`. The solution is __not__ case insensitive. Also, it doesn't solve for
*big* files, although the function in `challenge.py` can be used to operate on a chunk of text from such a file. The
problem of resulting words appear in different chunks is actual in this case and can be traded off by increasing the
size of each chunk.

## Running

tbd

## Tests

Run the following command from within the repo root:

`python -m unittest discover`
