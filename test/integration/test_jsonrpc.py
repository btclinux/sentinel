import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

# from dashd import DashDaemon
# from dash_config import DashConfig
from anond import AnonDaemon
from anon_config import AnonConfig


# def test_dashd():
def test_anond():
    # config_text = DashConfig.slurp_config_file(config.dash_conf)
    config_text = AnonConfig.slurp_config_file(config.anon_conf)
    print(config_text)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'0642bbe1cadd962f090093b14cd5cc6c4d7e4c1efcce82bf3c0ac7f2fce12806'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'01064a94d893deab5198592c9a950be8fdbb9ca7e9d512803a4872e176e116fb'
            # 0x0575f78ee8dc057deee78ef691876e3be29833aaee5e189bb0459c087451305a
    # creds = DashConfig.get_rpc_creds(config_text, network)
    # dashd = DashDaemon(**creds)
    # assert dashd.rpc_command is not None
    creds = AnonConfig.get_rpc_creds(config_text, network)
    anond = AnonDaemon(**creds)
    assert anond.rpc_command is not None
    
    assert hasattr(anond, 'rpc_connection')

    # Anon testnet block 0 hash == 00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c
    # test commands without arguments
    # info = dashd.rpc_command('getinfo')
    info = anond.rpc_command('getinfo')
    info_keys = [
        'version',
        'protocolversion',
        'walletversion',
        'balance',
        'blocks',
        'timeoffset',
        'connections',
        'proxy',
        'difficulty',
        'testnet',
        'keypoololdest',
        'keypoolsize',
        'paytxfee',
        'relayfee',
        'errors',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    # assert dashd.rpc_command('getblockhash', 0) == genesis_hash
    assert anond.rpc_command('getblockhash', 0) == genesis_hash
