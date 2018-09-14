import pytest
import os
import sys
import re
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
os.environ['SENTINEL_ENV'] = 'test'
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), '../../lib')))
import config
# from dash_config import DashConfig
from anon_config import AnonConfig


@pytest.fixture
# def dash_conf(**kwargs):
def anon_conf(**kwargs):
    defaults = {
        # 'rpcuser': 'dashrpc',
        'rpcuser': 'anonrpc',
        'rpcpassword': 'EwJeV3fZTyTVozdECF627BkBMnNDwQaVLakG3A4wXYyk',
        'rpcport': 29241,
    }

    # merge kwargs into defaults
    for (key, value) in kwargs.items():
        defaults[key] = value

    conf = """# basic settings
testnet=1 # TESTNET
server=1
rpcuser={rpcuser}
rpcpassword={rpcpassword}
rpcallowip=127.0.0.1
rpcport={rpcport}
""".format(**defaults)

    return conf


def test_get_rpc_creds():
    # dash_config = dash_conf()
    anon_config = anon_conf()
    # creds = DashConfig.get_rpc_creds(dash_config, 'testnet')
    creds = AnonConfig.get_rpc_creds(anon_config, 'testnet')

    for key in ('user', 'password', 'port'):
        assert key in creds
    assert creds.get('user') == 'anonrpc'
    assert creds.get('password') == 'EwJeV3fZTyTVozdECF627BkBMnNDwQaVLakG3A4wXYyk'
    assert creds.get('port') == 29241

    # dash_config = dash_conf(rpcpassword='s00pers33kr1t', rpcport=8000)
    anon_config = anon_conf(rpcpassword='s00pers33kr1t', rpcport=12345)
    # creds = DashConfig.get_rpc_creds(dash_config, 'testnet')
    creds = AnonConfig.get_rpc_creds(anon_config, 'testnet')

    for key in ('user', 'password', 'port'):
        assert key in creds
    assert creds.get('user') == 'anonrpc'
    assert creds.get('password') == 's00pers33kr1t'
    assert creds.get('port') == 12345

    no_port_specified = re.sub('\nrpcport=.*?\n', '\n', anon_conf(), re.M)
    # creds = DashConfig.get_rpc_creds(no_port_specified, 'testnet')
    creds = AnonConfig.get_rpc_creds(no_port_specified, 'testnet')

    for key in ('user', 'password', 'port'):
        assert key in creds
    assert creds.get('user') == 'anonrpc'
    assert creds.get('password') == 'EwJeV3fZTyTVozdECF627BkBMnNDwQaVLakG3A4wXYyk'
    assert creds.get('port') == 3127


# ensure anon network (mainnet, testnet) matches that specified in config
# requires running anond on whatever port specified...
#
# This is more of a anond/jsonrpc test than a config test...
