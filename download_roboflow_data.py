import os


if __name__ == '__main__':
    os.system('pip install roboflow')

    import env
    from roboflow import Roboflow

    rf = Roboflow(api_key=env.ROBOFLOW_API_KEY)
    project = rf.workspace().project(env.PROJECT_NAME)
    dataset = project.version(env.PROJECT_VERSION).download('yolov5')
