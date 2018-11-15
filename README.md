# Introduction
This propgram is a simple web API using flask. We aim for collecting data by this API.

# Installation Guide

This program works with Python3.5.

First, please clone this repository and  get Miniconda3 installer with command below:

```sh
$ git clone https://github.com/TaikiYamamoto/M1presentation_training_A5B1.git
$ cd M1presentation_training_A5B1
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Then extract files, and installing Miniconda3:

```sh
$ sh Miniconda3-latest-Linux-x86_64.sh
```

(If you do not use Linux OS, please download and install for the other OS from [here](https://conda.io/miniconda.html).)

Please answer "yes" to question "Do you wish the installer to prepend the Miniconda3 install location

to PATH in your /usrhome/ISM18/c50~~~~~~~/.bashrc ?".

If you answer to question "no", you add the Miniconda3 path on your computer.

```sh
$ echo 'export PATH=/usrhome/ISM18/c50~~~~~~~/miniconda3/bin:$PATH' >> ~/.bashrc
$ source ~/.bashrc
```

Finally, construct the environment using environment.yml, and activate its environment:

```sh
$ conda env create -n python3.5 -f environment.yml
$ source activate python3.5
```

This Completed installation.

# How to use

Running flask API program:

```sh
(python3.5)$ python myapp.py
```

Now, that HTTP server is up on your computer, please access in localhost:5000/ (default) with web browser.

However, you can not see your page, because you do not implement server's operating.

Please implement it with reference to handouts and presentations.

If you completed implementation, let's draw and send!
