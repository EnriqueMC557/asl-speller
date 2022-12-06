import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-type', type=str, default='image', help='image/webcam')
    args = parser.parse_args()
    args = vars(args)

    if args['test_type'] == 'webcam':
        os.system('python yolov5/detect.py --weights yolov5/runs/train/exp/weights/best.pt --source 0')
    else:
        os.system('python yolov5/detect.py --weights yolov5/runs/train/exp/weights/best.pt --img 512 --source images_test_speller')
