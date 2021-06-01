#!/usr/bin/env python3
from custom_node import HostConnectedNode
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.node import Host


def setup_net():
    # net_local = Mininet(host=Host)
    # net_local = Mininet(host=HostConnectedNode, ipBase='66.0.0.0/24')
    net_local = Mininet(host=HostConnectedNode)
    h1 = net_local.addHost('h1', inNamespace=True)
    h2 = net_local.addHost('h2', inNamespace=True)
    s1 = net_local.addController('c1', inNamespace=False)
    s1 = net_local.addSwitch('s1', inNamespace=False)
    net_local.addLink(h1, s1)
    net_local.addLink(h2, s1)
    return net_local


if __name__ == '__main__':
    setLogLevel('info')

    net = setup_net()
    net.start()
    net.pingAll(0.5)
    CLI(net)
    net.stop()
