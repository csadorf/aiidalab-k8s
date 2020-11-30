#!/usr/bin/env python
import os
import secrets
import string
from subprocess import run

import click


RESET_PASSWORD = """
from firstuseauthenticator import FirstUseAuthenticator as Auth
auth = Auth()
auth.reset_password('{username}', '{password}')
"""


def _generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password
    return password


def _reset_password(hub, username, password):
    run(['kubectl', 'exec', hub, '--', 'python3', '-c',
         RESET_PASSWORD.format(username=username, password=password).strip().replace('\n', ';')], check=True)


@click.command()
@click.argument('username')
@click.option('--hub', required=True, prompt=True,
              default=lambda: os.environ.get('JUPYTERHUB_POD', ''))
def cli(username, hub):
    pw = _generate_password()
    _reset_password(hub, username, pw)
    click.echo(f"Changed password for user '{username}' to: {pw}")


if __name__ == '__main__':
    cli()
