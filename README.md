# Movie Trailer

This is a simple python application that creates a static webpage to
display a list of movies, movie information provided in certain format.
This webpage displays the poster pictures of the movies and its title.
Clicking on the choice of movie will then play a
trailer of that movie.

## Install instruction:

Please create a GitHub account if you don't already have one.
For detailed instuctions to create a GitHub account
please refer to [GitHub site](http://www.gihub.com)
Python installation is expected to be installed on the target machine.
For futher instructions on python installation please refer to www.python.org.

Then please clone/branch this Movie Trailer project from [GitHub](https://github.com/rajusubbanna/Movie-Trailer)
Example:
```
1. git clone https://github.com/rajusubbanna/Movie-Trailer
2. cd MovieTrailer
```

## What it contains:

There is no library that gets created for public use or API published.
This Project has 3 source files.
```
1. The file fresh_tomatoes.py, downloaded/cloned via GitHub Repository ud036_StarterCode
2. The class declaration file Movie.py.
        *This has simple constructors to creates a Movie instanec.
3. It example usage file entertainmentMedia.py.py
```

## How it works:

The example media.py code actually creates a list of movies and interface with API
published by fresh_tomatoes for creating a static webpage that gets
displayed in the default browser. Clicking on any of the poster would then play
the movies trailer.
Example:
        File entertainmentMedia.py shows how this application can be used. For every movie that needs to be added to this dynamically created webpage needs 4 information
```
        1. Movie title
        2. A Short Movie Storyline
        3. A URL link to the poster page for this movie
        4. A URL youtube link that would play its trailer
```
a real data would be
```
	1."Toy Story",
	2."A story of boy and this toys",
	3. "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	4. "https://www.youtube.com/watch?v=vwyZH85NQC4"
```

or copy lines 50 to 55 as many times, as many movies to be added and fill the
contents. The contents are shown below
```
media.Movie(
           "<A TITLE>",
            "<Storyline for this movie>",
            "<URL to poster image>",
            "<URL to youtube trailer>"
             ),
```
For Toy Story movie above it would be
<pre><code>
media.Movie(
   "Toy Story",
   "A story of boy and this toys",
   "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
   "https://www.youtube.com/watch?v=vwyZH85NQC4"
           ),
</code></pre>

## More Information:

This is developed as part of the Udacity Fullstack nanodegree course.
There are excellent courses offered at Udacity, please feel free to browse through and pick your kind.

## License:

No copyright and licensing required to run this code.
However fresh_tomatoes.py is provided by Udacity, please check with them for futher details about it. This is a public domain work. Feel free to do whatever you want with it.

## Author :
Raju Subana, except for fresh_tomatoes.py. Code provided as-is.
