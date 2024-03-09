# WindowsActivator

This is a simple CLI program made in Python that can activate Microsoft Windows for free. I have tested it on Windows 11, however I assume it should work same on Windows 7 and higher.

> This program is only for educational purposes.

To use it, first install the packages from requirements `pip3 install -r requirements.txt` and then run the main.py under activator folder.

### Modes

I made it to 2 modes. When you run main.py, you recieve like:

```bash
Usage: main.py [OPTIONS] COMMAND [ARGS]...
Try 'main.py --help' for help.
Error - Missing command.
```

Run with `--help` and you will see 2 commands: `automatic` and `manual`.

- Use the automatic command if you want to simply activate your Windows.
- The manual command will let you choose the edition to activate, however it functions the same.

### Supported Editions

Below is the list of all supported editions to be activated:

- Home
- Pro
- Professional
- Education
- Enterprise

> I wanted to make a cool CLI program so I just made this. Be sure to report any bugs and contributing is welcome!
