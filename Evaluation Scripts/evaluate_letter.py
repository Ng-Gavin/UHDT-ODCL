import sys
import os
import subprocess
import cv2


#usage: use python3 evaluate_letter.py CHAR
#or python evaluate_letter.py CHAR
#depending on your installation 
#where CHAR is the character you want to evaluate against
#Uses first character of file to determine what the character in the file is, and compares that to the results
comparison = sys.argv[1]
results = []
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
    print("Testing on character {}".format(comparison))
    count=0



    pathsToImages = getPaths(imgdir, isImage)

    if not len(pathsToImages):
        print("couldn't find any images")
        return

    for pathtoimage in pathsToImages:
        imageName = os.path.basename(pathtoimage)

        image = cv2.imread(pathtoimage)
        if image is None:
            print("couldn't open the image")
            continue

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
    imgdir= 'tesstrain/data/test-ground-truth (old font)'
    model= 'UHDT'
    #change model name to whatever model you are testing against
    #you must also change the location of where the model is located in the subproccess to run
    #to where your model is located
    #change to '/home/leoliang/tesstrain/data', to the folder location where your model is located
    #you can also change the PSM above to whatever PSM you want to use for tesseract, in our case I found 
    #PSM 13 to work the best
    labelingProcess(imgdir)