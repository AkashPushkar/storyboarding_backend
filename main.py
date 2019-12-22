import imageAveraging


# Initialization and parameters to the imageAveraging file
dataDir='/home/apushkar/home/datasets/coco'
dataType='train2017'
annFile='{}/annotations/instances_{}.json'.format(dataDir, dataType)


catNms = ['giraffe', 'elephant', 'zebra', 'dog', 'teddy', 'cat', 'horse', 'sheep', ]
outputDir="/home/apushkar/home/datasets/AOI/objImages"
imgAvrg = imageAveraging.imageAveraging(dataDir, dataType, annFile)

print("imgAvrg.objectImageCreator started")
imgAvrg.objectImageCreator(catNms=catNms ,outputDir = outputDir)

print("ImgAvrg.globalFeature started")

imgAvrg.globalFeature(catNms=catNms, inputDir='/home/apushkar/home/datasets/AOI/objImages', outputDir = '/home/apushkar/home/datasets/AOI/deepFeatures')

print("ImgAvrg.clustering started")
imgAvrg.clustering(catNms=catNms, featureDir='/home/apushkar/home/datasets/AOI/deepFeatures', clusterResultDir='/home/apushkar/home/datasets/AOI/clusterResults')

print("ImgAvrg.averagingImage  started")
imgAvrg.averagingImage(catNms = catNms,objImageDir='/home/apushkar/home/datasets/AOI/objImages', clusterResultDir='/home/apushkar/home/datasets/AOI/clusterResults')

