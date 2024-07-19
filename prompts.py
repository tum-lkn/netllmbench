TASK_1 = ('Network Topology: You have two switches (S1 and S2) and one router (R1). '
          'Host H1 is to connect to S1 via interface eth0. '
          'Task: Generate a command to configure the IP address 192.168.1.10/24 on Host H1\'s eth0 interface. '
          'Give your answer in JSON format. The keys are "machine" and "command". '
          'Do not include any other text in your answer.')

TASK_2 = ('Network Topology: Host H2 is to connect to Switch S1 via interface eth0. '
          'Task: Generate a command to configure the IP address 192.168.1.20/24 on Host H2\'s eth0 interface. '
          'Give your answer in JSON format. The keys are "machine" and "command". '
          'Do not include any other text in your answer.')

TASK_3 = ('Network Topology: Host H3 is to connect to Switch S2 via interface eth0. '
          'Task: Generate a command to configure the IP address 192.168.2.10/24 on Host H3\'s eth0 interface. '
          'Give your answer in JSON format. The keys are "machine" and "command". '
          'Do not include any other text in your answer.')

TASK_4 = ('Network Topology: Switch S1 is connected to Router R1 via interface eth0 on R1. '
          'Task: Generate a command to configure the IP address 192.168.1.1/24 on Router R1\'s eth0 interface.'
          'Give your answer in JSON format. The keys are "machine" and "command". '
          'Do not include any other text in your answer.')

TASK_5 = ('Network Topology: Switch S2 is connected to Router R1 via interface eth1 on R1. '
          'Task: Generate a command to configure the IP address 192.168.2.1/24 on Router R1\'s eth1 interface.'
          'Give your answer in JSON format. The keys are "machine" and "command". '
          'Do not include any other text in your answer.')

TASK_6 = ('Task: Generate a command for Host H1 to assign a default gateway pointing to the router\'s IP address on their respective subnet.'
          'Give your answer in JSON format. The keys are "machine" and "command". '
          'Do not include any other text in your answer.')

TASK_7 = ('Task: Generate a command for Host H2 to assign a default gateway pointing to the router\'s IP address on their respective subnet.'
          'Give your answer in JSON format. The keys are "machine" and "command". '
          'Do not include any other text in your answer.')

TASK_8 = ('Task: Generate a command for Host H3 to assign a default gateway pointing to the router\'s IP address on their respective subnet.'
          'Give your answer in JSON format. The keys are "machine" and "command". '
          'Do not include any other text in your answer.')

TASK_9 = ('Network Topology: Following Task 4, static routes have been configured on Router R1, facilitating communication between Subnet 1 (hosts H1 and H2) and Subnet 2 (host H3). '
          'Task: Generate a command for Host H3 to ping Host H2 for only 3 times. '
          'Give your answer in JSON format. The keys are "machine" and "command". '
          'Do not include any other text in your answer.')
