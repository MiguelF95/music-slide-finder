# Powerpoint Slide Finder

Simple Python script that takes powerpoint slide titles as input and returns them as a list with their corresponding slide number.

**Notes:**
 - The first PowerPoint file found in the same directory as this script is parsed through. Ensure only the desired .pptx file is in the same folder
 - Only word-for-word match with the slide title is returned (there must be no missing words or spelling mistakes)
 - Titles are not longer case or punctuation sensitive 

**Dependencies:**
 - python-pptx (https://github.com/scanny/python-pptx)
 - glob
 - string

**TODO:**
 ~~- Relax slide title match constraints to allow case and delimiter mistakes~~
 ~~- Return list of slide titles not found~~
 ~~- Allow user to input all slide titles at once, separated by either newline or comma~~ (Only supports separation by new line)
 - Relax slide title match constraints to allow for spelling mistakes
 - Allow user to choose a specific .pptx file
