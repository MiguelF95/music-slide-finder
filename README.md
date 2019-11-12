# Powerpoint Slide Finder

Simple Python script that takes powerpoint slide titles as input and returns them as a list with their corresponding slide number.

**Notes:**
 - The first PowerPoint file found in the same directory as this script is parsed through. Ensure only the desired .pptx file is in the same folder
 - Only an exact match with the slide title is returned (case-sensitive and delimiter-sensitive)

**Dependencies:**
 - python-pptx (https://github.com/scanny/python-pptx)
 - glob

**TODO:**
 - Allow user to choose a specific .pptx file
 - Relax slide title match constraints to allow case and delimiter mistakes
 - Relax slide title match constraints to allow for spelling mistakes
 - Return list of slide titles not found
 - Allow user to input all slide titles at once, separated by either newline or comma