from . import imageAveraging


# Initialization and parameters to the imageAveraging file
dataDir='..'
dataType='val2017'
annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)




imgAvrg = imageAveraging.imageAveraging()
imgAvrg.objectImageCreator(catNms=['bear'], outputDir="~//home/datasets/AOI")