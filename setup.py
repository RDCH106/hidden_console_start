from setuptools import setup
from hiddenconsolestart.metadata import Metadata

metadata = Metadata()


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

long_description = """"

Hidden Console Start ⚙️
-----------------------

Hide console and execute applications in background. HCS (Hidden Console
Start) is a good alternative to simulate background process (process &)
as in GNU/Linux systems.

**GNU/Linux**

::

    $ ping 127.0.0.1 > log.txt &

**Windows**

::

    $ hcs -e "ping 127.0.0.1 > log.txt"

What can I do with HCS?
~~~~~~~~~~~~~~~~~~~~~~~

-  Launch applications in background
-  Launch all the processes that you want with one call to HCS (one
   subprocess in one thread for each application)

Installation
~~~~~~~~~~~~

You can install or upgrade HCS with:

``$ pip install hcs --upgrade``

Or you can install from source with:

.. code:: bash

    $ git clone https://github.com/RDCH106/hidden_console_start.git --recursive
    $ cd hidden_console_start
    $ pip install .

Quick example
~~~~~~~~~~~~~

.. code:: bash

    $ hcs -e "ping 127.0.0.1 > log.txt" "mspaint"

The example executes ping to ``127.0.0.1`` redirecting the result to
``log.txt`` file and launch Microsoft Paint at the same time.
    """


setup(
    name = 'hcs',
    packages = ['hiddenconsolestart'],
    install_requires = requirements(),
    version = metadata.get_version(),
    license = 'MIT',
    description = 'Hide console and execute applications in background',
    long_description= long_description,
    author = metadata.get_author(),
    author_email = 'contact@rdch106.hol.es',
    url = 'https://github.com/RDCH106/hidden_console_start',
    download_url = 'https://github.com/RDCH106/hidden_console_start/archive/v'+metadata.get_version()+'.tar.gz',
    entry_points={
        'gui_scripts': ['hcs=hiddenconsolestart.main:main'],
    },
    keywords = 'background console windows gnu-linux',
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)