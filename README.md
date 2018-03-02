# Hidden Console Start ⚙️

[![PyPI](https://img.shields.io/pypi/v/hcs.svg)](https://pypi.python.org/pypi/hcs)
[![PyPI](https://img.shields.io/pypi/pyversions/hcs.svg)](https://pypi.python.org/pypi/hcs)
[![PyPI](https://img.shields.io/pypi/l/hcs.svg)](https://github.com/RDCH106/hidden_console_start/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/RDCH106/hidden_console_start.svg?branch=master)](https://travis-ci.org/RDCH106/hidden_console_start)

Hide console and execute applications in background.
HCS (Hidden Console Start) is a good alternative to simulate background process (process &) as in GNU/Linux systems.

##### GNU/Linux 

```
$ ping 127.0.0.1 > log.txt &
```

##### Windows

```
$ hcs -e "ping 127.0.0.1 > log.txt"
```

<br>

### What can I do with HCS?

- Launch applications in background
- Launch all the processes that you want with one call to HCS (one subprocess in one thread for each application)

### Installation

You can install or upgrade HCS with:

`$ pip install hcs --upgrade`

Or you can install from source with:

```bash
$ git clone https://github.com/RDCH106/hidden_console_start.git --recursive
$ cd hidden_console_start
$ pip install .
```

### Quick example

```bash
$ hcs -e "ping 127.0.0.1 > log.txt" "mspaint"
```

The example executes ping to `127.0.0.1` redirecting the result to `log.txt` file and launch Microsoft Paint at the same time.
