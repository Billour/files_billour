# Naming rules
Python style
Follow the PEP 8 Python style guide, except TensorFlow uses 2 spaces instead of 4. Please conform to the Google Python Style Guide, and use pylint to check your Python changes.
PEP 8 link: https://peps.python.org/pep-0008/

pylint
To install pylint:


$ pip install pylint
To check a file with pylint from the TensorFlow source code root directory:


$ pylint --rcfile=tensorflow/tools/ci_build/pylintrc tensorflow/python/keras/losses.py
Supported Python versions
For supported Python versions, see the TensorFlow installation guide.

See the TensorFlow continuous build status for official and community supported builds.

C++ coding style
Changes to TensorFlow C++ code should conform to the Google C++ Style Guide and TensorFlow specific style details. Use clang-format to check your C/C++ changes.

To install on Ubuntu 16+, do:


$ apt-get install -y clang-format
You can check the format of a C/C++ file with the following:


$ clang-format <my_cc_file> --style=google > /tmp/my_cc_file.cc
$ diff <my_cc_file> /tmp/my_cc_file.cc


Version:2024042501
# files_billour
This is a an easy-to-use files system, I hope it could help people easy to use and for operating systems like Windows, Linux,  but not for macOS.
