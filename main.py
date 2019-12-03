import imageAveraging


# Initialization and parameters to the imageAveraging file
dataDir='/home/apushkar/home/datasets/coco'
dataType='train2017'
annFile='{}/annotations/instances_{}.json'.format(dataDir, dataType)



outputDir="/home/apushkar/home/datasets/AOI/objImages"
imgAvrg = imageAveraging.imageAveraging(dataDir, dataType, annFile)

imgAvrg.objectImageCreator(catNms=['bear'],outputDir = outputDir )
