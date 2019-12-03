import os
import json
import matplotlib.pyplot as plt
import cv2
import numpy as np
import skimage.io as io
import math

from pycocotools.coco import COCO
import pdb

import torchvision.models as models

from sklearn.cluster import KMeans


class imageAveraging:
	def __init__(self, dataDir, dataType, annFile):
		self.dataDir=dataDir
		self.dataType=dataType
		self.annFile=annFile
		self.coco=COCO(annFile)


	def objectImageCreator(self, catNms, outputDir):
		i=0
		for cat in catNms:
			catIds = self.coco.getCatIds(catNms = cat)
			imgIds = self.coco.getImgIds(catIds = catIds)
			annIds = self.coco.getAnnIds(imgIds = imgIds, catIds = catIds, iscrowd=None)

			for annId in annIds:
				anns = self.coco.loadAnns(annId)
				imgId = anns[0]['image_id']
				#pdb.set_trace()
				img = self.coco.loadImgs(imgId)[0]
				#pdb.set_trace()
				url = img['coco_url']
				img = io.imread(url)
				#pdb.set_trace()
				#print(i,"sdnicjwncjd")	
				if len(img.shape) != 3:
					#pdb.set_trace()
					continue
				
				mask = self.coco.annToMask(anns[0])

				for i in range(len(img.shape)):
					img[:,:,i] *= mask

				img = img[int(anns[0]['bbox'][1]):int(anns[0]['bbox'][1]+anns[0]['bbox'][3]), int(anns[0]['bbox'][0]): int(anns[0]['bbox'][0]+anns[0]['bbox'][2]), :]
				cv2.imwrite(os.path.join(outputDir, cat, str(annId)+'.jpg'), img)
				#print(i)		
				i=i+1
				if i==10:
					break
	

	def globalFeature(self, catNms, inputDir, outputDir):
		
		
		alexnet = models.alexnet(pretrained=True).features

		
		for cat in catNms:
			data = {}
			catIds = self.coco.getCatIds(catNms = cat)
			imgIds = self.coco.getImgIds(catIds = catIds)
			annIds = self.coco.getAnnIds(imgIds = imgIds, catIds = catIds, iscrowd=None)
			
			for annId in annIds:
				img = cv2.imread(os.path.join(inputDir, str(annId)+'.jpg'))
				if (img == None):
					continue
				fv = np.array(alexnet(img)).flatten()
				
				data[annId] = fv
		
			with open(os.apth.join(outputDir, cat+'.json'), 'w+') as file:
				json.dump(data, file)	
						
	

	def clustering(self, catNms, featureDir, clusterResultDir,  n_cluster='auto'):
				
		for cat in catNms:
			
			with open(os.path.join(featureDir,cat+'.json', 'r')) as file:
				data = json.load(file)
			d = []
			annId = []
			for i in data.keys():
				d.append(data[i])
				annId.append(i)
			if n_cluster == 'auto':
				n_cluster = int(math.sqrt(len(d)))
			kmeans = KMeans(n_cluster).fit(X)
			labels = kmeans.labels_
			centroids = kmeans.cluster_centres_
			
			clusterResult = {} 
			for i in range(n_cluster):
				clusterResult[str(i)] = []

			for i in zip(annId, labels):
				clusterResult[str(labels)].append(annId)


			with open(os.path.join(clusterResultDir, cat+'.json'), 'w+') as file:
				json.dump(clusterResult, file)

		
	def averagingImage(self, catNms, clusterResultDir):
		for cat in catNms:
			with open(os.path.join(clusterResultDir, cat+'.json'), 'r') as file:
			data = json.load(file)

			for key in data:
				combinedImg = []
				#averageImg = np.zeros((256,256,3))
				for img in data[key]:
					averageImg.append(img)

				m = np.ma.masked_where(img == 0, img)
				combinedImg = np.ma.median(m, axis=0).filled(0)
			cv2.imwrite(os.path.join(clusterResultDir, cat, str(key)+.jpg), combinedImg) 



#	def visualization(self, catNms, clusterResultDir):
#
#		for cat in catNms:
#			with open(os.path.join(clusterResultDir, cat+'.json'), 'r') as file:
#				data = json.load(file)
#
#
#			
#			for key 
			




		


				



				
