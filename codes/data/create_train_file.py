import os

def create_file():
    cwd = os.getcwd()
    gt_path = 'CrackForestDatasetPruned\groundTruthPng'
    real_path = 'CrackForestDatasetPruned\image'
    split = 0.5    # percentage train / val ratio (%)

    # define paths
    gt_total_path = os.path.join(cwd, gt_path)
    real_total_path = os.path.join(cwd, real_path)

    # define splits for train and val
    gt_imgs = os.listdir(gt_total_path)
    train_split = gt_imgs[:int(split*len(gt_imgs))]
    val_split = gt_imgs[int(split*len(gt_imgs)):]

    with open('train.txt', 'w') as f:
        for gt_file in train_split:
            for real_file in os.listdir(real_total_path):
                if gt_file.split('.')[0] in real_file:
                    f.write("{} {}\n".format(os.path.join(real_total_path, real_file), os.path.join(gt_total_path, gt_file)))

    with open('val.txt', 'w') as f:
        for gt_file in val_split:
            for real_file in os.listdir(real_total_path):
                if gt_file.split('.')[0] in real_file:
                    f.write("{} {}\n".format(os.path.join(real_total_path, real_file), os.path.join(gt_total_path, gt_file)))


if __name__ == '__main__':
    create_file()
