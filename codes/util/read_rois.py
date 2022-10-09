import re
from skimage.draw import ellipse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec


def read_roi(file_name):
	with open(file_name) as f:
		lines = f.readlines()
		lines_el = lines[1:-1]
		print("Read lines:", len(lines_el))

		arr = []
		for line in lines_el:
			obj = {}
			if re.search(r"^ELLIPSE", line):
				obj["type"] = "ELLIPSE"
				ellipse_data = re.sub(r"^ELLIPSE",'',line)[1:-2]
				coordinates = ellipse_data.split(',')
				r_radius = round(int(coordinates[3])/2)
				c_radius = round(int(coordinates[2])/2)
				obj["r"] = int(coordinates[1]) + r_radius
				obj["c"] = int(coordinates[0]) + c_radius
				obj["r_radius"] = r_radius
				obj["c_radius"] = c_radius
				# arr.append(obj)

				img = np.zeros((256, 256), dtype=np.uint8)
				rr, cc = ellipse(obj["r"], obj["c"], obj["r_radius"], obj["c_radius"])
				img[rr, cc] = 1

				arr.append(img)

			else:
				print("not an ELLIPSE !?!?!?")
		
		#merge single cell masks
		reduced = np.maximum.reduce(arr)

		# plt.figure(figsize=(20, 4))
		# grid_spec = gridspec.GridSpec(1, 3, width_ratios=[3, 3, 3])
		# plt.subplot(grid_spec[0])
		# plt.axis('off')
		# plt.title('Ground truth')
		# plt.imshow(reduced)

		# plt.show()


		return reduced






# read_roi("single_roi.rois.rois")