import open3d as o3d
import numpy as np
import cv2
import os

points = np.ones((1,3))
colors = np.ones((1,3))

depthBwLayers = 100

for i in range(1,5):
    img = cv2.imread(os.path.join('./data', 'p'+str(i)+'.png'))
#    for row in range(np.shape(img)[0]):
#        for col in range(np.shape(img)[1]):
#            if img[row, col,:].all() != 255:
#                colors = np.concatenate((colors, np.reshape(img[row,col,:], (1,3))),axis=0)
#                points = np.concatenate((points, np.reshape([row, col, i],(1,3) )), axis=0)
#        print(row, end=" ", flush=True)

    xy = np.where((img[:,:,0]!=255) & (img[:,:,0]!=255) & (img[:,:,0]!=255))
    points = np.concatenate((points, np.concatenate((np.reshape(xy[0],(-1,1)), np.reshape(xy[1],(-1,1)), depthBwLayers * i * np.ones((len(xy[0]),1))), axis=1)), axis=0)

    colors = np.concatenate((colors, img[xy]), axis=0)
#    print(np.shape(points), np.shape(colors))


pcl = o3d.geometry.PointCloud()
#xyz = np.concatenate((np.random.randn(100,2),np.ones((100,1))), axis=1)
#col = np.concatenate((np.zeros((100,2)), np.ones((100,1))), axis=1)
#
pcl.points = o3d.utility.Vector3dVector(points)
pcl.colors = o3d.utility.Vector3dVector(colors/255)

o3d.visualization.draw_geometries([pcl])
o3d.io.write_point_cloud("a.pcd", pcl)
