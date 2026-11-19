"""Minimal web app example using Flask."""
import argparse
import os
import sys
from flask import Flask, request

app = Flask(__name__)
server_password = None


@app.route('/')
def hello():
    """Main route that checks password if required."""
    if server_password is not None:
        # Check if password parameter matches
        client_password = request.args.get('password', '')
        if client_password != server_password:
            return '<h1>Not authorized</h1>', 401

    return '<h1>Hello World</h1>'


def daemonize(logfile=None):
    """Fork the process to run as a daemon in the background."""
    # First fork
    try:
        pid = os.fork()
        if pid > 0:
            # Parent process, exit
            sys.exit(0)
    except OSError as e:
        sys.stderr.write(f"Fork #1 failed: {e}\n")
        sys.exit(1)

    # Decouple from parent environment
    os.chdir('/')
    os.setsid()
    os.umask(0)

    # Second fork
    try:
        pid = os.fork()
        if pid > 0:
            # Second parent, exit
            sys.exit(0)
    except OSError as e:
        sys.stderr.write(f"Fork #2 failed: {e}\n")
        sys.exit(1)

    # Redirect standard file descriptors
    sys.stdout.flush()
    sys.stderr.flush()

    if logfile:
        # Open log file
        log_fd = os.open(logfile, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
        # Redirect stdout and stderr to log file
        os.dup2(log_fd, sys.stdout.fileno())
        os.dup2(log_fd, sys.stderr.fileno())
        os.close(log_fd)
    else:
        # Redirect to /dev/null
        devnull = os.open(os.devnull, os.O_RDWR)
        os.dup2(devnull, sys.stdin.fileno())
        os.dup2(devnull, sys.stdout.fileno())
        os.dup2(devnull, sys.stderr.fileno())
        os.close(devnull)


def main():
    """Entry point for the web app."""
    global server_password

    parser = argparse.ArgumentParser(description='Run the Hello World web app')
    parser.add_argument('--port', type=int, default=8080,
                        help='Port to run the server on (default: 8080)')
    parser.add_argument('--password', type=str, default=None,
                        help='Password for authorization (default: no password)')
    parser.add_argument('--daemon', action='store_true',
                        help='Run as a background daemon')
    parser.add_argument('--logfile', type=str, default=None,
                        help='Log file path when running as daemon (default: no logging)')

    args = parser.parse_args()
    server_password = args.password

    # Print startup message before daemonizing
    startup_msg = f'Starting web server on http://localhost:{args.port}'
    if server_password:
        startup_msg += f'\nPassword protection enabled. Access with: http://localhost:{args.port}/?password={server_password}'

    if args.daemon:
        print(f'{startup_msg}\nRunning in daemon mode...')
        if args.logfile:
            print(f'Logging to: {args.logfile}')
        daemonize(args.logfile)
    else:
        print(startup_msg)

    app.run(host='0.0.0.0', port=args.port, debug=False)


if __name__ == '__main__':
    main()
