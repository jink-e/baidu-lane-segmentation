from os.path import join as pjoin
# from os.path import dirname, abspath

class Config(object):
    # model config
    OUTPUT_STRIDE = 16
    ASPP_OUTDIM = 256
    SHORTCUT_DIM = 48
    SHORTCUT_KERNEL = 1
    NUM_CLASSES = 8

    # train config
    EPOCHS = 60
    WEIGHT_DECAY = 1.0e-4
    SAVE_PATH = "logs"
    # BASE_LR = 0.0006
    BASE_LR = 0.001

    PRETRAIN = False
    PRETRAINED_WEIGHTS = pjoin(SAVE_PATH, 'laneNet1.pth.tar')
