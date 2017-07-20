import os, subprocess

class DataBuilder():
    def __init__(self):
        pass

    def createDirs(self):
        subprocess.call(["mkdir", "vailid"])
        subprocess.call(["mkdir", "results"])
        subprocess.call(["mkdir", "-p", "test/unknown"])
        subprocess.call(["mkdir", "-p", "sample/train"])
        subprocess.call(["mkdir", "-p", "sample/test"])
        subprocess.call(["mkdir", "-p", "sample/valid"])
        subprocess.call(["mkdir", "-p", "sample/results"])


def main():
    DB_dogscats = DataBuilder()
    DB_dogscats.createDirs()

if __name__ == '__main__':
    main()
