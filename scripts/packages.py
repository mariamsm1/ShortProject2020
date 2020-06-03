#MARIAM MIARI
#
#2020-2021
#
#PACKAGES USED IN THIS SHORT PROJECT.
#
#---------------------------------
#to untar downloaded databases
import tarfile

#to download databases
import wget

#to gunzip downloaded databases
import gzip

#to unzip downloaded databases
import zipfile
from zipfile import ZipFile

#to read and write csv files
import csv
import pandas as pd #also used for reading htmls

#for webscraping
import bs4
from bs4 import BeautifulSoup

#for reading .owl format databases
from owlready2 import *

#for downloading .obo formats
import goatools
from goatools.obo_parser import GODag
