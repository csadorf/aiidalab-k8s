import os
import requests


class JupyterHub:

    def __init__(self, baseurl, token):
        self.baseurl = baseurl
        self.url = f'{baseurl}/hub/api'
        self.token = token

    @property
    def _headers(self):
        return {'Authorization': f'token {self.token}'} if self.token else {}

    def users(self, username=''):
        r = requests.get(f'{self.url}/users' + (f'/{username}' if username else ''), headers=self._headers)
        r.raise_for_status()
        return r.json()

    def delete_user(self, username):
        r = requests.delete(f'{self.url}/users/{username}', headers=self._headers)
        r.raise_for_status()

    def start_server(self, username):
        r = requests.post(f'{self.url}/users/{username}/server', headers=self._headers)
        r.raise_for_status()

    def stop_server(self, username):
        r = requests.delete(f'{self.url}/users/{username}/server', headers=self._headers)
        r.raise_for_status()


if __name__ == '__main__':
    from pprint import pprint
    host = os.environ.get('AIIDALAB_HOST', 'http://localhost:8000')
    token = os.environ.get('JUPYTERHUB_API_TOKEN', '')
    hub = JupyterHub(host, token)
    pprint(hub.users())
