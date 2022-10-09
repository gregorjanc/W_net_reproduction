"""BSD500 Dataset"""
import os
import sys
import numpy as np
from PIL import Image
from scipy.io import loadmat
from config import Config
from util.read_rois import read_roi

config = Config()


class DataLoader:
    def __init__(self, root=''):
        self.root = root
        self.imgs, self.gts, self.preds = _get_img_list(self.root)

    def __getitem__(self, index):
        img_path, gt_path, pred_path = self.imgs[index], self.gts[index], self.preds[index]

        raw_img = Image.open(img_path).convert('RGB')
        raw_gt, mean_gt = _loadmask(gt_path)
        raw_pred, mean_pred = _loadpred(pred_path)

        return raw_img, raw_gt, mean_gt, raw_pred, mean_pred

    def __len__(self):
        return len(self.imgs)


def _get_img_list(folder):
    img_paths = []
    gt_paths = []
    pred_paths = []

    img_directory = os.path.join(folder, config.data_dir)
    gt_directory = os.path.join(folder, config.data_dir)

    pred_folder = os.path.join(folder, config.predictions_destination2)

    segmentation_path_folders = ["test/"]
    image_path_folders = ["test/"]

    img_folder=os.path.join(img_directory,image_path_folders[0])
    gt_folder=os.path.join(gt_directory,segmentation_path_folders[0])

    for filename in os.listdir(img_folder):
        if filename.endswith(".jpg"):

            imgpath = os.path.join(img_folder, filename)

            roi_file = filename.replace('.jpg', '.rois')
            gtpath = os.path.join(gt_folder, roi_file)

            mat_prediction_file = f"mat_{config.model_name}_{filename.replace('.jpg','.mat')}"
            predpath = os.path.join(pred_folder, mat_prediction_file)

            if (os.path.isfile(imgpath) and os.path.isfile(gtpath) and os.path.isfile(predpath)):
                img_paths.append(imgpath)
                gt_paths.append(gtpath)
                pred_paths.append(predpath)
            else:
                print('cannot find the gt or image or pred:', imgpath, gtpath, predpath)

    print('Found {} images in the folder {}'.format(len(img_paths), img_directory))


    return img_paths, gt_paths, pred_paths


def _loadmask(mask_path):
    raw_masks = []
    mean_mask = None
    mask_mat = read_roi(mask_path)

    mean_mask = mask_mat / 1


    return mask_mat, mean_mask.astype(np.int)


def _loadpred(pred_path):
    raw_preds = []
    mean_pred = None

    pred_mat = loadmat(pred_path)['segs']

    idx = pred_mat.shape[1]

    for i in range(idx):
        pred = pred_mat[0, i]

        if i == 0:
            mean_pred = pred
        else:
            mean_pred = mean_pred + pred

        raw_preds.append(pred)

    mean_pred = mean_pred / idx
    raw_preds = np.array(raw_preds)

    return raw_preds, mean_pred.astype(np.int)