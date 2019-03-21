"""
Understanding the customer requirement is very important thing in building 
efficient software for Machine Learning/Deep Learning/RL

Generally Non technical users expect everything to be in chronological/alphabetical
order - They expect the file system to be user-friendly and efficient and certainly bug-free

So it is important to learn the behaviour of customers by comsuming and ingesting their 
feedback/survey/opinions data from the web/desktop application which has NLP engine
tethered to its end which keeps learning from the continuous stream of text and 
actually produce better results for sorting and searching their audio/video/Images/.doc etc
with decreasing latency.

"""
import re
from datetime import datetime
Images = ['mallika_1.jpg','dog005.jpg','grandson_2018_01_01.png',
          'dog008.jpg','mallika_6.jpg','grandson_2018_5_23.png',
          'dog01.png','mallika_11.jpg','mallika2.jpg','grandson_2018_02_5.png',
          'grandson_2019_08_23.jpg','dog9.jpg','mallika05.jpg']

def sortFiles(filesList):
    jpg_files = [f for f in Images if f.strip().split('.')[1] == 'jpg']
    png_files = [f for f in Images if f.strip().split('.')[1] == 'png']
    jpg_files = sorted(jpg_files)
    png_files = sorted(png_files)
    
    def fileExtension(files):
        regex_dog = re.compile(r'dog\d+')
        dog_filter = list(filter(regex_dog.match,files))
        dog_filter = sorted(dog_filter,key=lambda x: int(''.join(re.findall(r'\d+',x))))
        
        regex_mallika = re.compile(r'mallika')
        mallika_filt = list(filter(regex_mallika.match,files))
        sorted_mallika = sorted(mallika_filt,key=lambda x: int(''.join(re.findall(r'\d+',x))))

        regex_gs = re.compile(r'grandson')
        grandS = list(filter(regex_gs.match,files))
        grandS = sorted(grandS,key=lambda x: datetime.strptime(''.join(re.findall(r'\d+',x)),"%Y%m%d"))
        return (dog_filter + grandS + sorted_mallika)
    
    jpg_sorted = fileExtension(jpg_files)
    png_sorted = fileExtension(png_files)
    return (jpg_sorted,png_sorted)

jpgS, pngS = sortFiles(Images)

if __name__ == '__main__':
    searchQ = input()
    if searchQ.startswith('dog'):
        X = re.compile(r'dog')
        result = list(filter(X.match,jpgS)) + list(filter(X.match,pngS))
    if searchQ.startswith('grandson'):
        Y = re.compile(r'grandson')
        result = list(filter(Y.match,jpgS)) + list(filter(Y.match,pngS))
    if searchQ.startswith('mallika'):
        Z = re.compile(r'mallika')
        result = list(filter(Z.match,jpgS)) + list(filter(Z.match,pngS))
        
    print (result)