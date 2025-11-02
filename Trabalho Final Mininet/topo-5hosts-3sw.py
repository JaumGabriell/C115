from mininet.topo import Topo

class MyTopo( Topo ):
    "2 switch 2 host custom topology"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost1 = self.addHost( 'h1' )
        rightHost1 = self.addHost( 'h2' )
        centerHost = self.addHost( 'h3' )
        leftHost2 = self.addHost( 'h4' )
        rightHost2 = self.addHost( 'h5' )
        leftSwitch = self.addSwitch( 's1' )
        centerSwitch = self.addSwitch( 's2' )
        rightSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( leftHost1, leftSwitch )
        self.addLink( rightHost1, leftSwitch )
        self.addLink( leftSwitch, centerSwitch )
        self.addLink( centerHost, centerSwitch)
        self.addLink( centerSwitch, rightSwitch )
        self.addLink( leftHost2 , rightSwitch )
        self.addLink( rightHost2, rightSwitch )

topos = { 'mytopo': ( lambda: MyTopo() ) }
