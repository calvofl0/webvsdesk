"""Minimal web app example using Flask."""
import argparse
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


def main():
    """Entry point for the web app."""
    global server_password

    parser = argparse.ArgumentParser(description='Run the Hello World web app')
    parser.add_argument('--port', type=int, default=8080,
                        help='Port to run the server on (default: 8080)')
    parser.add_argument('--password', type=str, default=None,
                        help='Password for authorization (default: no password)')

    args = parser.parse_args()
    server_password = args.password

    print(f'Starting web server on http://localhost:{args.port}')
    if server_password:
        print(f'Password protection enabled. Access with: http://localhost:{args.port}/?password={server_password}')

    app.run(host='0.0.0.0', port=args.port, debug=False)


if __name__ == '__main__':
    main()
