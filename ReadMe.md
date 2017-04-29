# Favorite Movies Page


What this does is it takes you're favorite movies and compilies them into a webpage. When the movie is clicked the trailer will begin to play. 

  - Requires you to insert you're favorite movies using the format in media.py
  - entertainmentcenter.py contains the arrays and movie information you provide
  - fresh_tomatoes.py provides the compiling tool for displaying the information on a webpage.

# Adding your Movies

  - Open entertainmentcenter.py using python editor
  - Change the objects accordingly: 
 ```
                        OBJECT_TITLE_HERE = media.Movie("MOVIE TITLE HERE",
                        "MOVIE DESCRIPTION HERE",
                        "MOVIE POSTER IMAGE URL HERE",
                        "YOUTUBE TRAILER LINK HERE")
```
- Next add the object title to the array:
 ```
           movies = [add Object Title Here]
```
- Then Run Your Code

### Output

It should then open your Web Browser and begin creating the list of Movies. 

### Requirements

Python Editor and a Webbrowser

### Last Date Edited

4/29/2017

### Directory Structure
- entertainmentcenter.py (file containing the editable arrays)
- freshtomatoes.py (file containing the compiler and design of the webpage)
- media.py (file containing the structure for the class Movie and show_trailer)
- this readme.md
