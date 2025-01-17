import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

from util.dataloader import DataLoader
from util.metrics import Results
from config import Config

config = Config()

if __name__ == '__main__':

    test_loader = DataLoader()

    scores = 0
    sumRI = 0
    sumVI = 0

    # record error metrics
    results = Results()
    results.initialization()

    for idx, (raw_img, raw_gt, mean_gt, raw_pred, mean_pred) in enumerate(test_loader):

        print('Image ', idx)

        gt = raw_gt
        pred = raw_pred[0]
        print(gt.shape, pred.shape)

        # make them comparable cd 
        gt = gt[0:pred.shape[0], 0:pred.shape[1]]
        print("new shape:")
        print(gt.shape, pred.shape)

        # visualization
        if config.metrics_visualisation_flag:
            plt.figure(figsize=(20, 4))
            grid_spec = gridspec.GridSpec(1, 3, width_ratios=[3, 3, 3])

            plt.subplot(grid_spec[0])
            plt.axis('off')
            plt.title('RGB image')
            plt.imshow(raw_img)

            plt.subplot(grid_spec[1])
            plt.axis('off')
            plt.title('prediction')
            plt.imshow(pred)

            plt.subplot(grid_spec[2])
            plt.axis('off')
            plt.title('ground Truth')
            plt.imshow(gt)

            plt.show()

        ri, vi, R = results.update(pred, gt)

        print('SC is: ', R)
        print('RI is: ', ri)
        print('VI is: ', vi)

    meanSC, meanPRI, meanVI = results.get_results()

    if config.metrics_print_flag:
        print("==================================")
        print('mean SC is: ', meanSC)
        print('mean PRI is: ', meanPRI)
        print('mean VI is: ', meanVI)
