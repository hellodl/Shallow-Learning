import os, subprocess, glob
import numpy as np
from shutil import copyfile

class DataBuilder():
    def __init__(self):
        self.DATA_HOME_DIR = os.getcwd()
        self.valid_size = 2000
        self.sample_train_size = 200
        self.sample_valid_size = 200
        self.sample_test_size = 200
        self.createDirs()

    def createDirs(self):
        subprocess.call(["mkdir", "valid_redux"])
        subprocess.call(["mkdir", "results"])
        subprocess.call(["mkdir", "-p", "test/unknown"])
        subprocess.call(["mkdir", "-p", "sample/train"])
        subprocess.call(["mkdir", "-p", "sample/test"])
        subprocess.call(["mkdir", "-p", "sample/valid"])
        subprocess.call(["mkdir", "-p", "sample/results"])

        self.train_dir = 'train_redux'
        self.test_dir = 'test_redux'
        self.valid_dir = 'valid_redux'
        self.results_dir = 'results'
        self.sample_train_dir = 'sample/train'
        self.sample_test_dir = 'sample/test'
        self.sample_valid_dir = 'sample/valid'
        self.sample_results_dir = 'sample/results'


    def importSampleData(self):
        print("Import data to the SAMPLE directories as SAMPLES...")
        # codes here
        g = glob.glob('./train_redux/*.jpg')
        print("%d images are found in the train directory." % len(g))
        shuf = np.random.permutation(g)
        for i in range(self.sample_train_size):
            copyfile(shuf[i], self.DATA_HOME_DIR+'/sample/train/'+os.path.split(shuf[i])[-1])
        print("Importing data is done.")

    def importData(self):
        print("Import data to the related directories...")
        # codes here
        self.dataTransfer(self.valid_size, valid_dir=self.valid_dir, train_dir=self.train_dir)
        print("Importing data is done.")

    def dataTransfer(self, valid_size, train_dir, valid_dir):
        t = glob.glob(self.DATA_HOME_DIR+'/'+train_dir+'/'+'*.jpg')
        v = glob.glob(self.DATA_HOME_DIR+'/'+valid_dir+'/'+'*.jpg')

        nb_t = len(t)
        nb_v = len(v)
        print('%d train imgs are found.' %nb_t)
        print('%d valid imgs are found.' %nb_v)

        if valid_size <= 0:
            raise Exception("Valid size must be positive number.")

        num_trans = valid_size - nb_v
        if num_trans == 0:
            print("The size of valid imgs meets requirement.")
        elif num_trans < 0:
            print("%d imgs are moved from valid set to train set." %(-num_trans))
            shuf_v = np.random.permutation(v)
            for i in range(-num_trans):
                os.rename(shuf_v[i], self.DATA_HOME_DIR+'/'+train_dir+'/'+os.path.split(shuf_v[i])[-1])
        elif num_trans >0 and num_trans <= nb_t:
            print("%d imgs are moved from train set to valid set." %num_trans)
            shuf_t = np.random.permutation(t)
            for i in range(num_trans):
                os.rename(shuf_t[i], self.DATA_HOME_DIR+'/'+valid_dir+'/'+os.path.split(shuf_t[i])[-1])
        else:
            raise Exception("Not enough imgs to move from train set to valid set.")


def main():
    DB_dogscats = DataBuilder()
    DB_dogscats.importData()

if __name__ == '__main__':
    main()
