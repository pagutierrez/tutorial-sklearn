import os
import zipfile

try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

import tarfile


IMDB_URL = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
IMDB_ARCHIVE_NAME = "aclImdb_v1.tar.gz"
TITANIC_ARCHIVE_NAME = "titanic3.csv"
TITANIC_URL = "https://raw.githubusercontent.com/amueller/scipy-2017-sklearn/master/notebooks/datasets/titanic3.csv"
SPAM_ARCHIVE_NAME = "SMSSpamCollection"
SPAM_URL = "https://raw.githubusercontent.com/amueller/scipy-2017-sklearn/master/notebooks/datasets/smsspam/SMSSpamCollection"


def get_datasets_folder():
    here = os.path.dirname(__file__)
    notebooks = os.path.join(here, 'notebooks-spanish')
    datasets_folder = os.path.abspath(os.path.join(notebooks, 'datasets'))
    datasets_archive = os.path.abspath(os.path.join(notebooks, 'datasets.zip'))

    if not os.path.exists(datasets_folder):
        if os.path.exists(datasets_archive):
            print("Extracting " + datasets_archive)
            zf = zipfile.ZipFile(datasets_archive)
            zf.extractall('.')
            assert os.path.exists(datasets_folder)
        else:
            print("Creating datasets folder: " + datasets_folder)
            os.makedirs(datasets_folder)
    else:
        print("Using existing dataset folder:" + datasets_folder)
    return datasets_folder


def check_imdb(datasets_folder):
    print("\nComprobando la disponibilidad del dataset IMDb")
    archive_path = os.path.join(datasets_folder, IMDB_ARCHIVE_NAME)
    imdb_path = os.path.join(datasets_folder, 'IMDb')

    train_path = os.path.join(imdb_path, 'aclImdb', 'train')
    test_path = os.path.join(imdb_path, 'aclImdb', 'test')

    if not os.path.exists(imdb_path):
        if not os.path.exists(archive_path):
            print("Descargando el dataset de %s (84.1MB)" % IMDB_URL)
            opener = urlopen(IMDB_URL)
            open(archive_path, 'wb').write(opener.read())
        else:
            print("Archivo encontrado: " + archive_path)

        print("Extrayendo %s a %s" % (archive_path, imdb_path))

        tar = tarfile.open(archive_path, "r:gz")
        tar.extractall(path=imdb_path)
        tar.close()
        os.remove(archive_path)

    print("Comprobando que los directorios train y test del dataset IMDb existen...")
    assert os.path.exists(train_path)
    assert os.path.exists(test_path)
    print("=> Conseguido!")

def check_titanic(datasets_folder):
    print("\nComprobando la disponibilidad del dataset titanic")
    archive_path = os.path.join(datasets_folder, TITANIC_ARCHIVE_NAME)

    if not os.path.exists(archive_path):
        print("Descargando el dataset de %s (104KB)" % TITANIC_URL)
        opener = urlopen(TITANIC_URL)
        open(archive_path, 'wb').write(opener.read())
    else:
        print("Archivo ya existe: " + archive_path)

    print("=> Conseguido!")

def check_sms(datasets_folder):
    print("\nComprobando la disponibilidad del dataset SMS_SPAM")
    directory_path = os.path.join(datasets_folder,'smsspam')
    archive_path = os.path.join(directory_path, SPAM_ARCHIVE_NAME)

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        if not os.path.exists(archive_path):
            print("Descargando el dataset de %s (466KB)" % SPAM_URL)
            opener = urlopen(SPAM_URL)
            open(archive_path, 'wb').write(opener.read())
        else:
            print("Archivo ya existe: " + archive_path)
    else:
        print("Carpeta ya existe: " + directory_path)

    print("=> Conseguido!")

if __name__ == "__main__":
    datasets_folder = get_datasets_folder()
    check_imdb(datasets_folder)
    check_titanic(datasets_folder)
    check_sms(datasets_folder)

    #print("\n Cargando Labeled Faces Data (~200MB)")
    #from sklearn.datasets import fetch_lfw_people
    #fetch_lfw_people(min_faces_per_person=70, resize=0.4,
    #                 data_home=datasets_folder)
    #print("=> Conseguido!")

