import os


if __name__ == '__main__':
    IMAGE_SIZE_PIXELS = 512
    BATCH_SIZE = 16
    EPOCHS = 150
    DATASET_PATH = 'asl-alphabet-2'
    print('WARNING: Verify that test/train/val paths in data.yaml are in the form ../../YOUR_DATASET/test/images')
    os.system(
        f'python yolov5/train.py --img {IMAGE_SIZE_PIXELS} --batch {BATCH_SIZE} --epochs {EPOCHS} --weights yolov5s.pt '
        f'--data {DATASET_PATH}/data.yaml --cache'
    )

    print("INFO: To watch results in TensorBoard run 'tensorboard --logdir yolov5/runs'")
