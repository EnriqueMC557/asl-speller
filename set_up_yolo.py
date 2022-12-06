import os
import sys


if __name__ == '__main__':
    os.system('git clone https://github.com/ultralytics/yolov5')
    os.system('pip install -r yolov5/requirements.txt')

    sys.path.append('yolov5')

    import torch
    import utils

    display = utils.notebook_init()
    print("WARNING: If 'fatal: detected dubious ownership in repository at YOLOV5_REPO_PATH' was thrown "
          "run the respective command (git config --global --add safe.directory YOLOV5_REPO_PATH)")
