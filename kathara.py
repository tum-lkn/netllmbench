from Kathara.manager.Kathara import Kathara
from Kathara.model.Lab import Lab
import logging


def unpack_generator(gen):
    return [(a, b) for a, b in gen]


class KatharaEmulator:
    def __init__(self):
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)
        self.lab = Lab("netllmbench")

        self.logger.info("Creating netllmbench topology...")

        self.init_machine(self.lab, "router1", ["A", "B"])
        self.init_machine(self.lab, "switch1", ["A", "C", "D"])
        self.init_machine(self.lab, "switch2", ["B", "E"])
        self.init_machine(self.lab, "host1", ["C"])
        self.init_machine(self.lab, "host2", ["D"])
        self.init_machine(self.lab, "host3", ["E"])

        self.lab.create_file_from_list(
            [
                "ip link add name br0 type bridge",
                "ip link set br0 up",
                "ip link set eth0 master br0",
                "ip link set eth1 master br0",
                "ip link set eth2 master br0",
            ],
            "switch1.startup"
        )

        self.lab.create_file_from_list(
            [
                "ip link add name br0 type bridge",
                "ip link set br0 up",
                "ip link set eth0 master br0",
                "ip link set eth1 master br0",
            ],
            "switch2.startup"
        )

    def init_machine(self, lab, name, links):
        self.logger.info(f"Creating machine {name}.")

        # initialize the images
        lab.new_machine(name, **{"image": "kathara/base"})

        for link in links:
            lab.connect_machine_to_link(name, link)

    def deploy_lab(self):
        self.logger.info("Deploying lab...")
        Kathara.get_instance().deploy_lab(self.lab)

    def undeploy_lab(self):
        self.logger.info("Undeploying lab...")
        Kathara.get_instance().undeploy_lab(lab=self.lab)

    def run_command(self, host, command):
        self.logger.info(f"Running command: {command}")
        out = unpack_generator(Kathara.get_instance().exec(machine_name=host, command=command, lab=self.lab))

        return out

    def exec_command(self, host, command):
        if isinstance(command, str):
            self.logger.info(f"Executing command: {command}")
            cmd_out = self.run_command(host, command)
            return cmd_out

        elif isinstance(command, list) and len(command) > 0:

            for item in command:
                self.logger.info(f"Executing command: {item}")
                self.run_command(host, item)

