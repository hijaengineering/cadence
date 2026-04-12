# Cadence

A lightweight GUI application that monitors and displays your typing speed in keystrokes per minute (KPM) in real-time. The goal is simple: make you aware of when you're rushing, and nudge you to slow down. The display window stays on top of other windows and changes color as your speed increases.

> [!NOTE]
> This is a development project and may not adhere to production standards. Contributions via PRs are welcome!

## Features

- Real-time keystroke monitoring
- Visual feedback with color changes:
  - White: Normal typing speed (0-300 KPM)
  - Yellow: Getting fast — consider slowing down (301-400 KPM)
  - Red: You are rushing (>400 KPM)
- Always-on-top window
- Automatic reset every 10 seconds
- Minimalist interface
- Privacy first: What you are typing is not stored & runs fully offline

## Prerequisites

- macOS (currently only tested on Mac)
- Python 3.12 or higher
- Pyenv
- Poetry (Python package manager)
- Homebrew (for installing dependencies)
- System permissions for keyboard monitoring

> [!NOTE]
> These are the tools used in this setup. Other configurations may work, but this guide is written with the above in mind.

## Installation

1. **Install Required System Packages**

   ```bash
   brew install python-tk
   ```

2. **Configure Python with Tkinter Support**
   You'll need to install Python with Tkinter support. An example when using pyenv:

   ```bash
   export LDFLAGS="-L$(brew --prefix tcl-tk)/lib"
   export CPPFLAGS="-I$(brew --prefix tcl-tk)/include"
   export PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig"
   export PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$(brew --prefix tcl-tk)/include' --with-tcltk-libs='-L$(brew --prefix tcl-tk)/lib'"
   pyenv install 3.12.8  # Replace with your desired Python version
   ```

3. **Install Python Dependencies**

   ```bash
   poetry install
   ```

4. **Verify Tkinter Installation**

   ```bash
   poetry run python -c "import tkinter; print(tkinter.Tk().call('info', 'patchlevel'))"
   ```

5. **System Permissions**
   - Open System Settings
   - Navigate to Privacy & Security → Accessibility
   - Add your terminal application (e.g., Terminal.app or iTerm) to the allowed applications list

## Running the Application

```bash
sudo poetry run python cadence
```

> [!NOTE]
> Sudo access is required for keyboard monitoring.

## Troubleshooting

If you encounter issues with Tkinter or Poetry:

1. **Reset Poetry Environment**

   ```bash
   poetry env remove python
   poetry env use $(pyenv which python)
   poetry install
   ```

2. **Complete Poetry Reset**
   If the above doesn't work, try these steps:
   ```bash
   poetry self update
   poetry env remove --all
   poetry cache clear --all .
   rm poetry.lock
   poetry update
   poetry lock && poetry sync
   ```

## Contributing

Feel free to open issues or submit pull requests for improvements. Some areas that could use enhancement:

- Make the project more standalone: Remove the need for some of the prerequisites.
- Configuration options for speed thresholds
- Cross-platform support
