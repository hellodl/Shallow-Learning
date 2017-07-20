import os, subprocess, glob
import numpy as np
from shutil import copyfile

class DataBuilder():
    def __init__(self):
        self.DATA_HOME_DIR = os.getcwd()
        self.valid_size = 2000

    def createDirs(self):
        subprocess.call(["mkdir", "vailid"])
        subprocess.call(["mkdir", "results"])
        subprocess.call(["mkdir", "-p", "test/unknown"])
        subprocess.call(["mkdir", "-p", "sample/train"])
        subprocess.call(["mkdir", "-p", "sample/test"])
        subprocess.call(["mkdir", "-p", "sample/valid"])
        subprocess.call(["mkdir", "-p", "sample/results"])

    def importSampleData(self):
        print("Import data to the SAMPLE directories as SAMPLES...")
        # codes here
        print("Importing data is done.")

    def importData(self):
        print("Import data to the related directories...")
        # codes here
        # subprocess.call("cd train_redux", shell=True)
        g = glob.glob('./train_redux/*.jpg')
        # g0 = [os.path.split(x)[-1] for x in g]
        print('%d images are found in the train directory.' % len(g))
        shuf = np.random.permutation(g)

        # move a mount of images into valid directory
        for i in range(self.valid_size):
            os.rename(shuf[i], self.DATA_HOME_DIR+'/valid_redux/'+os.path.split(shuf[i])[-1])


        print("Importing data is done.")

def main():
    DB_dogscats = DataBuilder()
    DB_dogscats.createDirs()
    DB_dogscats.importData()

if __name__ == '__main__':
    main()
