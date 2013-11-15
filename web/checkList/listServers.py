from novaclient.v1_1 import client


class List:

    def __init__(self, user, password, project_id, auth_url):
            self.nova = client.Client(user, password,
                                      project_id=project_id,
                                      auth_url=auth_url)

    def buildList(self):
        #result = [{'name': 'Name Server',
        #           'status': 'Status Server',
        #           'ip': 'Adresses',
        #           }]
        result = []

        try:
            listServer = self.nova.servers.list()
        except:
            return result

        for server in listServer:
            result.append({
                'name': server.name,
                'status': server.status,
                'ip': ''.join(server.addresses['private'][0]['addr'])
            })
        return result
