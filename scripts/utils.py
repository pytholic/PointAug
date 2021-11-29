'''
Augmentation functiosn for point cloud data
'''

import os
import glob
import open3d as o3d
import numpy as np


DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(os.path.dirname(DIR), 'resources/data')

# for item in glob.glob(DATA_DIR + '/*'):
# 	print(item)
# 	mesh = trimesh.load(item)
# 	mesh.show()
# 	break

# mesh = o3d.io.read_triangle_mesh(os.path.join(DATA_DIR, '1.obj'), enable_post_processing=True)
# xyz = np.asarray(mesh.vertices, dtype=np.float32) # Getting vertices
#print(xyz.dtype)
# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(xyz)
# # print(len(pcd.points))
# pcd.paint_uniform_color([0.5, 0.5, 0.5])
# o3d.visualization.draw_geometries([pcd])


class RotatePointCloud:
	def __init__(self, data):
		self.data = data

	def rotate_point_cloud_angle(self, axis: str, angle: int=90):

		''' 
	    
	    Randomly rotate the point clouds to augument the dataset
	    Rotation axis can be choosen.
	    Input:
	    	Nx3 array, original point cloud
	    Return:
	    	Nx3 array, rotated point cloud
	    
	    '''

		rotation_angle = angle * (np.pi / 180) # Convert degrees to radians

		cos_theta = np.cos(rotation_angle)
		sin_theta = np.sin(rotation_angle)

		#Rotation around X axis
		Rx = np.array([
			[1, 0, 0],
			[0, cos_theta, -sin_theta],
			[0, sin_theta, cos_theta]])
		
		#Rotation around Y axis
		Ry = np.array([
			[cos_theta, 0, sin_theta],
			[0, 1, 0],
			[-sin_theta, 0, cos_theta]])
		
		#Rotation around Z axis
		Rz = np.array([
			[cos_theta, sin_theta, 0],
			[-sin_theta, cos_theta, 0],
			[0, 0, 1]])

		if axis == 'X':
			rotated_data = np.dot(self.data.reshape((-1, 3)), Rx)
		elif axis == 'Y':
			rotated_data = np.dot(self.data.reshape((-1, 3)), Ry)
		elif axis == 'Z':
			rotated_data = np.dot(self.data.reshape((-1, 3)), Rz)
		elif axis == 'XY':
			R = np.dot(Ry, Rx)
			rotated_data = np.dot(self.data.reshape((-1, 3)), R)
		elif axis == 'XZ':
			R = np.dot(Ry, Rx)
			rotated_data = np.dot(self.data.reshape((-1, 3)), R)
		elif axis == 'YZ':
			R = np.dot(Ry, Rx)
			rotated_data = np.dot(self.data.reshape((-1, 3)), R)
		else:
			R = np.dot(Rz, np.dot(Ry, Rx))
			rotated_data = np.dot(self.data.reshape((-1, 3)), R)
		return rotated_data


	def rotate_point_cloud_random(self, axis: str):

		''' 
	    
	    Randomly rotate the point clouds to augument the dataset
	    Rotation axis can be choosen.
	    Input:
	    	Nx3 array, original point cloud
	    Return:
	    	Nx3 array, rotated point cloud
	    
	    '''

		rotation_angle = np.random.uniform() * 2 * np.pi

		cos_theta = np.cos(rotation_angle)
		sin_theta = np.sin(rotation_angle)

		#Rotation around X axis
		Rx = np.array([
			[1, 0, 0],
			[0, cos_theta, -sin_theta],
			[0, sin_theta, cos_theta]])
		
		#Rotation around Y axis
		Ry = np.array([
			[cos_theta, 0, sin_theta],
			[0, 1, 0],
			[-sin_theta, 0, cos_theta]])
		
		#Rotation around Z axis
		Rz = np.array([
			[cos_theta, sin_theta, 0],
			[-sin_theta, cos_theta, 0],
			[0, 0, 1]])

		if axis == 'X':
			rotated_data = np.dot(self.data.reshape((-1, 3)), Rx)
		elif axis == 'Y':
			rotated_data = np.dot(self.data.reshape((-1, 3)), Ry)
		elif axis == 'Z':
			rotated_data = np.dot(self.data.reshape((-1, 3)), Rz)
		elif axis == 'XY':
			R = np.dot(Ry, Rx)
			rotated_data = np.dot(self.data.reshape((-1, 3)), R)
		elif axis == 'XZ':
			R = np.dot(Ry, Rx)
			rotated_data = np.dot(self.data.reshape((-1, 3)), R)
		elif axis == 'YZ':
			R = np.dot(Ry, Rx)
			rotated_data = np.dot(self.data.reshape((-1, 3)), R)
		else:
			R = np.dot(Rz, np.dot(Ry, Rx))
			rotated_data = np.dot(self.data.reshape((-1, 3)), R)
		return rotated_data



def jitter_point_cloud(data, sigma=0.01, clip=0.05):
    
    ''' 
    Randomly jitter points. jittering is per point.
    Input:
    	Nx3 array, original point clouds
    Return:
    	Nx3 array, jittered point clouds
    '''

    N, C = data.shape
    assert(clip > 0)
    jittered_data = np.clip(sigma * np.random.randn(N, C), -1*clip, clip)
    jittered_data += data
    return jittered_data


def load_mesh(path):
	mesh = o3d.io.read_triangle_mesh(path, enable_post_processing=True)
	
	return mesh


def mesh_to_array(data):

	'''
	Input:
		Object file
	Ouput:
		Nx3 array
	'''

	xyz = np.asarray(data.vertices, dtype=np.float32)
	return xyz


def array_to_pcd(data):
	
	'''
	Input:
		Nx3 array
	'''

	pcd = o3d.geometry.PointCloud()
	pcd.points = o3d.utility.Vector3dVector(data)

	return pcd


def plot_3d(data):
	
	'''
	Input:
		list of point clouds
	
	'''

	for pcd in data:
		pcd.paint_uniform_color(np.random.uniform(low=0.01, high=1, size=(3,)))
	
	o3d.visualization.draw_geometries(data)


# Utility functions for the main app

def rotation_augmentation_angle(path, axis='Y', angle=180):

	mesh = load_mesh(path)
	xyz = mesh_to_array(mesh)
	pcd = array_to_pcd(xyz)
	
	rotate = RotatePointCloud(xyz)

	xyz_rot_angle = rotate.rotate_point_cloud_angle(axis=axis, angle=angle)
	pcd_rot_angle = array_to_pcd(xyz_rot_angle)

	plot_3d([pcd, pcd_rot_angle])


def rotation_augmentation_random(path, axis='Y'):

	mesh = load_mesh(path)
	xyz = mesh_to_array(mesh)
	pcd = array_to_pcd(xyz)
	
	rotate = RotatePointCloud(xyz)

	xyz_rot_angle = rotate.rotate_point_cloud_random(axis=axis)
	pcd_rot_angle = array_to_pcd(xyz_rot_angle)

	plot_3d([pcd, pcd_rot_angle])


def jitter_augmentation(path, sigma=0.01, clip=0.05):

	mesh = load_mesh(path)
	xyz = mesh_to_array(mesh)
	pcd = array_to_pcd(xyz)

	xyz_jitter = jitter_point_cloud(xyz, sigma=sigma, clip=clip)
	pcd_jitter= array_to_pcd(xyz_jitter)

	plot_3d([pcd, pcd_jitter])

#def translate_point_cloud(data):

	''' 
	Randomly translate point cloud.
	Input:
		Nx3 array, original point clouds
	Return:
		Nx3 array, jittered point clouds
	'''


if __name__ == '__main__':


	#tmp = np.random.uniform(low=0.01, high=1, size=(3,))
	#print(tmp)

	path = os.path.join(DATA_DIR, '1.obj')
	
	mesh = load_mesh(path)
	xyz = mesh_to_array(mesh)
	pcd = array_to_pcd(xyz)
	
	rotate = RotatePointCloud(xyz)

	xyz_rot_angle = rotate.rotate_point_cloud_angle(axis='Y', angle=180)
	xyz_rot_random = rotate.rotate_point_cloud_random(axis='XYZ')
	xyz_jittered_data = jitter_point_cloud(xyz)

	pcd_rot_angle = o3d.geometry.PointCloud()
	pcd_rot_angle.points = o3d.utility.Vector3dVector(xyz_rot_angle)
	pcd_rot_random = o3d.geometry.PointCloud()
	pcd_rot_random.points = o3d.utility.Vector3dVector(xyz_rot_random)
	pcd_jittered = o3d.geometry.PointCloud()
	pcd_jittered.points = o3d.utility.Vector3dVector(xyz_jittered_data)

	plot_3d([pcd, pcd_rot_angle, pcd_rot_random, pcd_jittered])

