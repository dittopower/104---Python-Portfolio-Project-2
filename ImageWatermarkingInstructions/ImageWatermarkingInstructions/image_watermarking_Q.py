#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task the signatories below agree that it
#  represents our own work and that we both contributed to it.  We
#  are aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  First student's no: n8857954
#  First student's name: Damon Jones
#  Portfolio contribution: 80%
#
#  Second student's no: PUT 2ND STUDENT'S NUMBER HERE
#  Second student's name: PUT 2ND STUDENT'S NAME HERE
#  Portfolio contribution: PUT 2ND STUDENT'S PERCENTAGE CONTRIBUTION HERE
#
#  Contribution percentages refer to the whole portfolio, not just this
#  task.  Percentage contributions should sum to 100%.  A 50/50 split is
#  NOT necessarily expected.  The percentages will not affect your marks
#  except in EXTREME cases.
#
#--------------------------------------------------------------------#


#-----Task Description-----------------------------------------------#
#
#  IMAGE WATERMARKING
#
#  In this task you develop two functions for hiding and revealing
#  secret images as invisible watermarks within other images.  You
#  need to develop two functions:
#
#  1. add_watermark - Take an image and a greyscale "watermark"
#     and embed the watermark invisibly in the image.
#
#  2. reveal_watermark - Given an image file with a secret watermark,
#     process the file so that the watermark is revealed.
#
#  To do this you will need to make use of the functions provided
#  by the Python Imaging Library (PIL).  See the task's instructions
#  for further detail.
#--------------------------------------------------------------------#


#-----Automatic Tests------------------------------------------------#
#
#  This section contains unit tests that are used to run your
#  program.  Note that "passing" these tests does NOT mean that you
#  have satisfied the requirements for the task, because these tests
#  merely call the functions, but do not check that the image files
#  produced are correct.

"""
The first group of tests are for your "reveal_watermark" function.
They aim to retrieve the watermarks that have already been added to
two separate images.  Note that Tests 2 and 3 remove old copies of
the target files, if they exist.


Test 1.  Special case - Watermarked file does not exist, so
         your function should just return False and not change
         any files.
>>> reveal_watermark('Mystery_X.bmp')
False


Test 2.  Normal case - Watermarked file contains a secret image.
         Your code should produce the watermark in new file
         "BryceCanyon_X_O.bmp".  Hint: US pioneer Ebenezer Bryce
         famously described the canyon that now bears his name as
         "a hell of a place to lose a cow"!
>>> try:
...     remove('BryceCanyon_X_O.bmp')
... except:
...     pass
>>> reveal_watermark('BryceCanyon_X.bmp')
True


Test 3.  Normal case - Watermarked file contains a secret image.
         Your code should produce the watermark in new file
         "Beach_X_O.bmp".  Hint: Cluck, cluck, cluck!
>>> try:
...     remove('Beach_X_O.bmp')
... except:
...     pass
>>> reveal_watermark('Beach_X.bmp')
True


The next group of tests are for your "add_watermark" function.
They require that your "reveal_watermark" function works correctly,
because they will use it to check that the watermark has indeed been
added to the target file.  Therefore, you must have a working
"reveal_watermark" function before you can attempt to pass these
tests.  Apart from the first two, each test (1) removes old files, if
any, (2) calls the "add_watermark" function to add a watermark, and
(3) calls the "reveal_watermark" function to retrieve the watermark.


Test 4.  Special case - Image file does not exist, so
         your function should just return False and not change
         any files.
>>> add_watermark('Mystery_X.bmp', 'dog_watermark.bmp')
False


Test 5.  Special case - Watermark file does not exist, so
         your function should just return False and not change
         any files.
>>> add_watermark('Flowers_X.bmp', 'donkey_watermark.bmp')
False


Test 6.  Normal case - Image can be watermarked successfully.
         In this test you add the laboratory watermark to the image of
         QUT's Science and Engineering Centre, creating file
         "ScienceAndEngineeringCentre_X.bmp".
         Then this file is processed to reveal the watermark,
         creating file "ScienceAndEngineeringCentre_X_O.bmp".
         NB: In this case the main image and the watermark are exactly
         the same size.
>>> try:
...     remove('ScienceAndEngineeringCentre_X.bmp')
... except:
...     pass
>>> try:
...     remove('ScienceAndEngineeringCentre_X_O.bmp')
... except:
...     pass
>>> add_watermark('ScienceAndEngineeringCentre.bmp', 'laboratory_watermark.bmp')
True
>>> reveal_watermark('ScienceAndEngineeringCentre_X.bmp')
True


Test 7.  Normal case - Image can be watermarked successfully.
         In this test you add the dog watermark to the image of
         a field of flowers, creating file "Flowers_X.bmp".
         Then this file is processed to reveal the watermark,
         creating file "Flowers_X_O.bmp".  In this case the
         watermark is smaller than the main image so should be
         centred in the middle of the main image.
>>> try:
...     remove('Flowers_X.bmp')
... except:
...     pass
>>> try:
...     remove('Flowers_X_O.bmp')
... except:
...     pass
>>> add_watermark('Flowers.bmp', 'dog_watermark.bmp')
True
>>> reveal_watermark('Flowers_X.bmp')
True

"""
# 
#--------------------------------------------------------------------#



#-----Students' Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.

from PIL import Image

##### PUT YOUR SOLUTION HERE

def add_watermark(image, mark):
    try:
        pic = Image.open(image)
        grey = Image.open(mark)
        w,h=0,1
        startw=(pic.size[w]-grey.size[w])/2
        starth=(pic.size[h]-grey.size[h])/2
    ## IF watermark too large
        if startw < 0:
            grey = grey.crop(abs(startw),0,grey.size[w]+startw,grey.size[h])
            startw=0
        if starth < 0:
            grey = grey.crop(0,abs(starth),pic.size[w],grey.size[h]+starth)
            starth=0
         
        greypixels = list(grey.getdata())
        picregion = pic.transform(grey.size,1,(startw,starth,startw+grey.size[w],starth+grey.size[h]))
        picpixels = list(picregion.getdata())
        newpx= []
        for num in range(len(picpixels)):
            data = []
            data.append((picpixels[num][0]/10)*10 + greypixels[num]/100)
            data.append((picpixels[num][1]/10)*10 + (greypixels[num]%100)/10)
            data.append((picpixels[num][2]/10)*10 + greypixels[num]%10)
            newpx.append(tuple(data))
        
        test = Image.new("RGB",grey.size)
        test.putdata(tuple(newpx))
        test.copy()
        pic.paste(test,(startw,starth,startw+grey.size[w],starth+grey.size[h]))
        pic.save(image[:len(image)-4]+'_X.bmp')
    except Exception:
        return False
    return True




def reveal_watermark(image):
    try:
        mark =  Image.open(image)
        pixels = list(mark.getdata())
        revealed = []
        for pix in pixels:
            if isinstance(pix, int):
                return False
            else:
                data = ''
                for px in pix:
                    data = data + str(px)[len(str(px))-1:]
                if int(data) > 255:
                    data = 255
                revealed.append(int(data))
            #    print data
        pic=Image.new("L", mark.size)
        pic.putdata(revealed)
        pic.save(image[:len(image)-4]+'_O.bmp')
    except Exception:
        return False
    return True
        


#
#--------------------------------------------------------------------#



#-----Testing--------------------------------------------------------#
#
# The following code (when uncommented) will run your functions on
# the supplied images.  You should comment it out while developing
# your functions, but leave it uncommented when you submit your
# solution for marking.
#
if __name__ == '__main__':
    from os import remove
    from doctest import testmod
    testmod(verbose=True)
#
#--------------------------------------------------------------------#
