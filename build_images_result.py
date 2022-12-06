import cv2
import matplotlib.pyplot as plt


if __name__ == '__main__':
    EXP_PATH = 'yolov5/runs/detect/exp6'

    images = []
    titles = ['H', 'O', 'L', 'A', 'M', 'U', 'N', 'D', 'O']
    for img in range(9):
        img = cv2.imread(f'{EXP_PATH}/{img}.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        images.append(img)

    fig, axes = plt.subplots(1, 9)
    fig.set_size_inches((25, 5))
    for idx, ax in enumerate(axes):
        ax.imshow(images[idx])
        ax.set_title(titles[idx], fontsize=20, weight='bold')
        ax.set_xticks([])
        ax.set_yticks([])
    plt.savefig('figs/images_speller_result.png', bbox_inches='tight')
    plt.show()
