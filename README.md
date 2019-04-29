## Model Assembly Service
Model assembly service is an application to compose [CellML](https://www.cellml.org/) model entities from disparate source models in order to serialize a new CellML model. To perform model composition, this application utilizes the python bindings of the [libcellML](https://github.com/cellml/libcellml) library.

## Installation
### libCellML in Linux
Our model assembly service utilizes the libCellML library to compose CellML model entities. For convenience, we have described here the installation process of libCellml in Linux environment. For Windows 10 environment, please follow a link mentioned below.

libCellML depends on other software packages, so we have to install them before installing libCellML.

```
sudo apt-get install python3-dev
sudo apt-get install python3-pip
pip3 install Sphinx
pip3 install SPARQLWrapper
pip3 install lxml
sudo apt-get install cmake-curses-gui

git clone https://github.com/cellml/libcellml.git
cd libcellml
mkdir build
cd build
ccmake .. (afterwards, press `c` until we get a `g` option and then press `g` to generate a Makefile)
make -j
make test
make coverage
make docs
```

Enter the following command to activate the libcellml library in the `PYTHONPATH` 
```
export PYTHONPATH=~/libcellml/build/src/bindings/python
```

For testing, please run a test file to make sure libcellml is working.
```
python ~/libcellml/tests/bindings/python/test_model.py
```

### libcellml in Windows 10
Please navigate to the following link to get a detailed instruction on how to install (under-development) Python bindings on Windows 10.
``` 
https://github.com/cellml/libcellml/issues/277
```

### Programming Language
- Python 3.6
- SPARQL

### Library
- libCellML (Python bindings)

### Limitations
We will implement Unit testing and Functional testing to make sure the code is functioning as expected. While the underlying tools are not specific to renal epithelial transport, the currently supported text-to-query mappings and recommender system are very specific to renal epithelial transport.

### List of contributors
- Dewan Sarwar - @dewancse
- David Nickerson - @nickerso

### Acknowledgements
This project is supported by the MedTech Centre of Research Excellence (MedTech CoRE), the Aotearoa Foundation, and the Auckland Bioengineering Institute.
