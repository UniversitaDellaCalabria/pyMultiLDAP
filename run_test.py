import copy
import logging

from client import LdapClient
from settings import LDAP_CONNECTIONS


logger = logging.getLogger('ldap_client')
logger.setLevel(logging.DEBUG)
stdout = logging.StreamHandler()
stdout.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stdout.setFormatter(formatter)
logger.addHandler(stdout)

for i in LDAP_CONNECTIONS:
    lc = LdapClient(LDAP_CONNECTIONS[i])
    print('# Results from: {} ...'.format(lc))
    kwargs = copy.copy(lc.conf)
    r = lc.get(search="(&(sn=aie*)(givenName=isa*))")
    print(r+',') if r else ''

    # like wildcard
    r = lc.get(search="(&(sn=de marco)(schacPersonalUniqueId=*DMRGPP83*))")
    print(r+',') if r else ''

    # using search method with overload of configuration
    #kwargs['search']['search_filter'] = "(&(sn=de marco))"
    #r = lc.search(**kwargs['search'])

    r = lc.get(format='json')
    print(r+',') if r else ''

    p = "{SSHA512}JeCeGQnNfC+Cc5FuCpJmBMEYx3HELlOoxhkprKOnfS7wFI3dxhjJ2ubfKdvXIzZYE78ugo/wiwnsj9xV3MuWBps80UdeEAiP"
    search_str = "(&(userPassword={}))".format(p)
    r = lc.get(search=search_str, format='json')
    print(r+',') if r else ''

    print('# End {}'.format(i))
