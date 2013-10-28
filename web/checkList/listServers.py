from novaclient.v1_1 import client

from web import settings

class List():

    def __init__(self):
        self.nova = client.Client(settings.USERNAME, settings.PASSWORD,
                                  project_id=settings.PROJECT_ID,
                                  auth_url=settings.AUTH_URL)

    def buildList(self):
        result = [{'name': 'Name Server',
                   'status': 'Status Server',
                   'ip': 'Adresses',
                   }]
        for server in self.nova.servers.list():
            result.append({
                'name': server.name,
                'status': server.status,
                'ip': ''.join(server.addresses['private'][0]['addr'])
            })
        return result





