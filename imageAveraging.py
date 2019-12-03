import os
import json
import matplot.pyplot as plt
import cv2

from pycocotools.coco import COCO

class imageAveraging:
	def __init__(self, dataDir, dataType, annFile):
		self.dataDir=dataDir
		self.dataType=dataType
		self.annFile=annFile
		self.coco=COCO(annFile)


	def objectImageCreator(self, catNms, outputDir):

		for cat in catNms:
			catIds = self.coco.getCatIds(catNms = cat)
			imgIds = self.coco.getImgIds(catIds = catIds)
			annIds = self.coco.getAnnIds(imgIds = imgIds, catIds = catIds, iscrowd=None)

			for annId in annIds:
				anns = self.coco.loadAnns(annId)
				imgId = anns[0]['image_id']
				img = cv2.imread(self.coco.loadImgs(imgId)[0])
				
				if len(np.shape(img)) != 3:
					continue
				
				mask = self.coco.annToMask(anns)

				for i in range(len(np.shape(img))):
					img[:,:,i] *= mask

				img = img[anns[0]['bbox'][0]:anns[0]['bbox'][0]+anns[0]['bbox'][3], anns[0]['bbox'][1]: anns[0]['bbox'][1]+anns[0]['bbox'][4], :]
				cv.imwrite(os.path.join(outputDir, cat), img)

				break



