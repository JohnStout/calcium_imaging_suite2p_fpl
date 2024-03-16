import tifffile as tf
import numpy as np
import os
import xmltodict
import matplotlib.pyplot as plt

# filepath to .raw file
filepath = r'/Users/js0403/2p/A04/Image_001_001.raw'

# figure root
rootpath = os.path.split(filepath)[0]

# get metadata
root_contents = os.listdir(rootpath)
metadata_file = [i for i in root_contents if '.xml' in i][0]
metadata_path = os.path.join(rootpath,metadata_file)
file = xmltodict.parse(open(metadata_path,"r").read()) # .xml file

# define frame rate based on metadata
fr = float(file['ThorImageExperiment']['LSM']['@frameRate'])

# define .raw file fname
raw_files = [os.path.join(rootpath,i) for i in root_contents if '.raw' in i]

# get dimensions of recorded data
x=int(file['ThorImageExperiment']['LSM']['@pixelX'])
y=int(file['ThorImageExperiment']['LSM']['@pixelY'])
t=int(file['ThorImageExperiment']['Streaming']['@frames'])
z=int(file['ThorImageExperiment']['ZStage']['@steps']) # check this variable
dims=(z,t,y,x)

dimsize = 1
for i in dims:
    dimsize=dimsize*i
    #print(dimsize)

# now checkout whether dims = size of memory mapped file
filesize = np.memmap(filepath, dtype='int16', mode='r').size
#print(filesize)
print(filesize-dimsize)

#filesize.flush()


# create a memory mappable file
im = memmap(
    fname,
    shape=(num_files,image_shape[0],image_shape[1]),
    dtype=np.uint16,
    append=True
)

# now we will append to memory mapped file
print("Please wait while data is mapped to:",fname)
counter = 0
for i in pathnames:
    if downsample_factor is None:
        im[counter] = imread(i)
    else:
        im[counter] = imread(i)[::downsample_factor,::downsample_factor]
    im.flush()
    print("Finished with image",counter+1,"/",len(pathnames))  
    counter += 1