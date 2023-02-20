import sys
import os
import subprocess
import cv2

#usage: python3 evaluate.py
#or python evaluate.py
#depending on installation of python

#array of characters to test against, uses the first character of the file to determine what character it is
#loops through the array, if you want add or subtract characters to test against, do so here
test=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def isImage(filepath) -> bool:
    '''
    checks if file is an image
    '''

    lowercasePath = filepath.lower()

    # you can add more formats here
    cases = [
        lowercasePath.endswith('jpg'),
        lowercasePath.endswith('png'),
        lowercasePath.endswith('jpeg'),
    ]

    return any(cases)



def getPaths(imgdir, condition=lambda x: True):
    '''
    given path to image folder will return you a list of full paths
    to files which this folder contain

    :param condition: is a function that will filter only those files
    that satisfy condition
    '''

    files = map(lambda x: os.path.join(imgdir, x).strip(),
        os.listdir(imgdir))

    filtered = filter(condition, files)

    return list(filtered)

def frequencyNumber(arr,size):
    # Creating a HashMap containing integer
        # as a key and occurrences as a value
        freqMap = {}
  
        for i in range(size):
            if (arr[i] in freqMap):
  
                # If number is present in freqMap,
                # incrementing it's count by 1
                freqMap[arr[i]] = freqMap[arr[i]] + 1
            else:
  
                # If integer is not present in freqMap,
                # putting this integer to freqMap with 1 as it's value
                freqMap[arr[i]] = 1
  
        # Printing the freqMap
        for key, value in freqMap.items():
            print(f"{key} {value}")



def labelingProcess(imgdir):
    print("Welcome to the evaluation tool")
    for loop in range(0, len(test)):
        count=0
        comparison = test[loop]
        results=[]
        print("Testing on character {}".format(comparison))
        count=0



        pathsToImages = getPaths(imgdir, isImage)

        if not len(pathsToImages):
            print("couldn't find any images")
            return


        for pathtoimage in pathsToImages:
            imageName = os.path.basename(pathtoimage)

        # read image
            image = cv2.imread(pathtoimage)
            if image is None:
                print("couldn't open the image")
                continue

            #uses the first letter of the label to check what character is being compared 
            label = imageName[0]

            if not len(label):
                continue
        
            if label==comparison:
                letter=subprocess.run([
                'tesseract',
                '{}/{}'.format(imgdir,imageName),
                'stdout',
                '--tessdata-dir',
                '/home/leoliang/tesstrain/data',
                '--psm',
                '13',
                '-l',
                '{}'.format(model),
                '--loglevel',
                'ALL'
                ],capture_output=True, text=True)
                results.append(letter.stdout)
                count=count+1

        frequencyNumber(results,count)


if __name__ == '__main__':
    #change imgdir to directory where images to test against are
    #imgdir = 'SourceSans'
    imgdir = 'tesstrain/data/test-ground-truth (old font)'
    #change model name to whatever model you are testing against
    #you must also change the location of where the model is located in the subproccess to run
    #to where your model is located
    #change to '/home/leoliang/tesstrain/data', to the folder location where your model is located
    #you can also change the PSM above to whatever PSM you want to use for tesseract, in our case I found 
    #PSM 13 to work the best
    model = 'UHDT'
    labelingProcess(imgdir)