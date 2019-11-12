import glob
from pptx import Presentation

songlist = {}
inp = ""

print("\n\nThis script will take in PowerPoint Slide titles and return them with their corresponding slide numbers.\n")


#Obtain Slide titles from user input and add to a dictionary with value -1. Input requests stop when user inputs 1
while inp != '1':
    inp = (input("Input a slide title and press enter to continue adding more titles to the list.\nWhen finished, type '1' and press enter\n\n"))
    songlist[inp] = -1
    print("\n\n")


#Remove 1 from songlist
del songlist['1']


#Get Powerpoint File from current directory (same directory as this script)
pptname = glob.glob('*.pptx')
prs = Presentation(pptname[0])


#if a slide's title matches one in the songlist, update the value to the corresponding slide number
for slide in prs.slides:
    if slide.shapes.title.text in songlist:
        songlist[slide.shapes.title.text] = prs.slides.index(slide) + 1


#Print slide numbers with their corresponding titles
#Titles that were not found remain -1 in dicitonary and are not printed
print("Slide Numbers from " + pptname[0])
print("=============================================================")

for i in songlist:
    if songlist[i] != -1:
         print(  str(songlist[i]) + ' (' + i + ')'  )

print("=============================================================")