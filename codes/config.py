class Config():
    def __init__(self):
        # ------------------------------ Train Phase -----------------------------#
        self.debug = True
        self.input_size = 128  # Side length of square image patch
        # self.input_size = 256  # Side length of square image patch
        self.batch_size = 10
        self.val_batch_size = 4
        self.test_batch_size = 1

        self.k = 64  # Number of classes
        self.num_epochs = 36  # 36 for real
        self.data_dir = "../mag/transformed_images/base/"  # Directory of images
        # self.data_dir = "../../mag/transformed_images_single/"  # average only
        # self.data_dir = "../datasets/basic_images/" # base images

        self.showdata = False  # Debug the data augmentation by showing the data we're training on.

        self.useInstanceNorm = False  # Instance Normalization
        self.useBatchNorm = True  # Only use one of either instance or batch norm
        self.useDropout = True
        self.drop = 0.65

        # Each item in the following list specifies a module.
        # Each item is the number of input channels to the module.
        # The number of output channels is 2x in the encoder, x/2 in the decoder.
        self.encoderLayerSizes = [64, 128, 256, 512]
        self.decoderLayerSizes = [1024, 512, 256]

        self.showSegmentationProgress = True
        self.segmentationProgressDir = '../results/latent_images/'

        self.variationalTranslation = 0  # Pixels, 0 for off. 1 works fine

        self.loss_csvfile_destination = '../results/training_losses/'
        self.saveModel = True

        # ------------------------------Predict & Test Phase -----------------------------#
        # Flag for predicting & Metric Evaluation using BSD500
        self.USE_BSD500 = False  # <<<<============= Dataset Selection
        self.metrics_visualisation_flag = True
        self.metrics_print_flag = True

        # Model Name
        self.model_name = "2022-06-18_17_58_55_369662" # učenje na transformiranih slikah
        # model_name = "2022-07-02_03_26_16_673979" # učenje na navadnih slikah
        # model_name = "2022-07-05_21_45_51_271601" # učenje na navadnih slikah
        # model_name = "2022-07-03_14_45_03_778345" # učenje na average slikah
        # model_name = "2022-07-05_18_30_56_480984" # učenje 256px
        # model_name = "2022-07-07_05_33_30_317885" # učenje 256px

        # Directory from where to load the model
        self.loaded_model = "./results/saved_models/" + self.model_name

        # Converting the BSD500 gt frrom ".mat" files to ".npy" matrices required for predictions
        # Only need to be done once after conversion to .npy files are being loaded from converted_segmentations folder
        self.BSD500_preprocessing = False  # True

        # Path where both BSD500 and BSD300 are located
        self.test_path = "../mag/transformed_images/base"
        # self.test_path = "./datasets/basic_images"
        # self.test_path = "../mag/transformed_images_single"

        # Directory where to save the predictions made using the loaded model
        self.predictions_destination = "../results/test_set_predictions/"
        self.predictions_destination2 = "out_22_10_04_test_mat"
        # self.predictions_destination2 = "out_256px"

        self.test_set_image_dir = ''

        # if self.USE_BSD500:
        #     # Directory to load the Images of BSD 500
        #     self.test_set_image_dir = 'BSR/BSDS500/data/images/'
        #     self.test_set_gt_dir = '/BSR/BSDS500/data/groundTruth/'
        #     self.predictions_destination = "../results/test_set_predictions/BSD500/"
        # else:
        #     # Directory to load the images of BSD300
        #     self.test_set_image_dir = "BSDS300/images/"
        #     self.test_set_gt_dir = 'BSDS300/groundTruth/'
        #     self.predictions_destination = "../results/test_set_predictions/BSD300/"
