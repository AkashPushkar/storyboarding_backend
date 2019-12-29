import open3d as o3d
import numpy as np
import cv2
import os



points = np.ones((1,3))
colors = np.ones((1,3))

depthBwLayers = 100

for i in range(1,5):
    img = cv2.imread(os.path.join('./data', 'p'+str(i)+'.png'))

    xy = np.where((img[:,:,0]!=255) & (img[:,:,0]!=255) & (img[:,:,0]!=255))
    points = np.concatenate((points, np.concatenate((np.reshape(xy[0],(-1,1)), np.reshape(xy[1],(-1,1)), depthBwLayers * i * np.ones((len(xy[0]),1))), axis=1)), axis=0)

    colors = np.concatenate((colors, img[xy]), axis=0)


pcl = o3d.geometry.PointCloud()

pcl.points = o3d.utility.Vector3dVector(points)
pcl.colors = o3d.utility.Vector3dVector(colors/255)

# o3d.visualization.draw_geometries([pcl])
o3d.io.write_point_cloud("a.pcd", pcl, write_ascii=True, print_progress=True)


# point cloud to mesh
# pcl.estimate_normals()

# # estimate radius of the rolling ball
# distance = pcl.compute_nearest_neighbor_distance()
# avg_dist = np.mean(distance)
# radius = 1.5* avg_dist

# mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcl, o3d.utility.DoubleVector([radius, radius * 2]))

# o3d.io.write_triangle_mesh("mesh.gltf", mesh)