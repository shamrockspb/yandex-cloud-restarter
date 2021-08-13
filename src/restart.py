# -*- coding: utf-8 -*-
"""
Example:

        $ python restart.py instance1 instance2

Todo:
    * Add function for managing instance via API

"""

from subprocess import Popen, PIPE
import re
import sys


def start_instance(server):
    """Function that checks instance status, and starts it, if it is currently down
    
    Args:
        server (str): instance name in Yandex Cloud. 
    Returns:
        None
    """
    if server != "":
        p = Popen(['/root/yandex-cloud/bin/yc', 'compute', 'instance',
                  'get', server], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        rc = p.returncode

        if(rc == 0):
            result = re.search(r"(status: )(\w*)\n", output.decode("utf-8"))

            status = result.group(2)

            if(status == 'STOPPED'):
                print("Current status of {0}: {1}, staring server".format(
                    server, status))
                p = Popen(['/root/yandex-cloud/bin/yc', 'compute', 'instance',
                          'start', server], stdin=PIPE, stdout=PIPE, stderr=PIPE)
                output, err = p.communicate()
                rc = p.returncode
                if(rc == 0):
                    print("Instance {0} started successfully".format(server))
                else:
                    print(
                        "Error while starting instance {0}, error code {1}".format(server, rc))

            else:
                print("Current status of {0}: {1}, do nothing...".format(
                    server, status))
        else:
            print(
                "Error while accessing instance {0}, error code {1}".format(server, rc))


# Main
if(__name__ == '__main__'):

    if(len(sys.argv) > 1):
        for server in sys.argv[1:]:
            start_instance(server)
    else:
        print("Please specify server in Yandex Cloud")
