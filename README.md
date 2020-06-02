# Short Project in Bioinformatics-Lund University
## Project scripts description

My short project entitled "Functional annotation of potential regulators of lysosomes and cell death identified in a genome-wide screen " involved scripts that carry out two major tasks.The first task primarly involves data download and analysis of genes collected from 12 databases related to autophagy,cell death,and lysosomes. However, the second task involves functional annotation of genes obtained from a genome-wide screen and microscopic images analysis of knockdown data. 
Scripts of the first task require the installation and import of various packages(see packages.py). <br>
Some databases were available for download(see datadownload.py), while others were not and therefore the htmls were downloaded (datadownload.py) and webscraping scripts were written for them(see webscraping.py).

## Dependencies

* python v3.7.4

All the scripts were run using python. No other dependency is required.

## Basic scripts
* packages.py<br>
This script involves the packages used in this short project.

* datadownload.py<br>
This script involves the codes written for downloading the databases that were available for download or the htmls of databases that were not available for download.<br>
Some codes should be run a long with the correct packages from packages.py.<br>
One file was downloaded manually and therefore it is not included in this set of codes. It is from uniprot/subcellular-lysosome section.

* webscraping.py<br>






