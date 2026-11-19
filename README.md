# Web vs Desktop: Didactic Python Example

A minimal example demonstrating the difference between a web application and a desktop application in Python.

## What's Included

- **Desktop App**: A simple window displaying "Hello World" using Tkinter
- **Web App**: A Flask server displaying "Hello World" with optional password protection

## Installation

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```

2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

3. Install the package:
   ```bash
   pip install .
   ```

## Running the Desktop App

Simply run:
```bash
deskapp
```

A window will appear with "Hello World" displayed.

## Running the Web App

### Basic Usage (No Password)

Start the server:
```bash
webapp
```

Then open your browser and visit:
```
http://localhost:8080
```

### With Custom Port

```bash
webapp --port 3000
```

Then visit: `http://localhost:3000`

### With Password Protection

Start the server with a password:
```bash
webapp --password mypass
```

Then visit with the password parameter:
```
http://localhost:8080/?password=mypass
```

If you visit without the password or with the wrong password, you'll see "Not authorized".

## Key Differences

- **Desktop App**: Runs locally, creates a window, interacts with the user through GUI
- **Web App**: Runs as a server, accessed through a browser, communicates over HTTP
