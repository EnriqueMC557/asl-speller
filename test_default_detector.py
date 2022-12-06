import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-type', type=str, default='image', help='image/webcam')
    args = parser.parse_args()
    args = vars(args)

    if args['test_type'] == 'webcam':
        os.system('python yolov5/detect.py --weights yolov5s.pt --conf 0.25 --source 0')
    else:
        os.system('python yolov5/detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source yolov5/data/images')
