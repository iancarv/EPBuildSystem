import os
import zipfile
import settings
from testes.tester import Tester


def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

if __name__ == "__main__":
    tester = Tester()
    if tester.test():
	    zip_name = zipfile.ZipFile(settings.dest, 'w')
	    zipdir(settings.dir, zip_name)
