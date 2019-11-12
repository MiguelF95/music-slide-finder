# Powerpoint Slide Finder

Simple Python script that takes powerpoint slide titles as input and returns them as a list with their corresponding slide number.

>**Notes:**
> - The first PowerPoint file found in the same directory as this script is parsed through. Ensure only the desires .pptx file is in the same folder
> - Only and exact match with the slide title is returned (case-sensitive and delimiter-sensitive)

>**Dependencies:**
> - python-pptx (https://github.com/scanny/python-pptx)
> - glob