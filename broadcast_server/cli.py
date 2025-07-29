import click
from broadcast_server.server import start_server
from broadcast_server.client import start_client

@click.group()
def cli():
    pass

@cli.command()
@click.option('--host', default='localhost', help='Host to bind the server')
@click.option('--port', default=8765, help='Port to bind the server')
def start(host, port):
    """Start the broadcast server."""
    start_server(host, port)

@cli.command()
@click.option('--host', default='localhost', help='Server host to connect to')
@click.option('--port', default=8765, help='Server port to connect to')
def connect(host, port):
    """Connect to the broadcast server as a client."""
    start_client(host, port)

if __name__ == '__main__':
    cli()