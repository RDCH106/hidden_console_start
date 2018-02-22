# Hidden Console Start ⚙️

Hide console and execute applications in background.
HCS (Hidden Console Start) is a good alternative to simulate background process (process &) as in GNU/Linux systems.

##### GNU/Linux 

```
$ ping 127.0.0.1 > log.txt &
```

##### Windows

```
$ pythonw hcs.pyw -e "ping 127.0.0.1 > log.txt"
```

<br>

### What can I do with HCS?

- Launch applications in background
- Launch all the processes that you want with one call to HCS (one subprocess in one thread for each application)

### Installation

You can install from source with:

```bash
$ git clone https://github.com/RDCH106/hidden_console_start.git --recursive
$ cd hidden_console_start/hiddenconsolestart
$ python hcs.pyw   #Execution
```

### Quick example

```bash
$ pythonw hcs.pyw -e "ping 127.0.0.1 > log.txt" "mspaint"
```

The example executes ping to `127.0.0.1` saves the result in `log.txt` file and launch Microsoft Paint at the same time.
