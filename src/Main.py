from subprocess import Popen, PIPE
import re
import sys


def startInstance(server):
    '''Check instance status, and try to start it, if it is currently down'''
    if server != "":
        p = Popen(['/root/yandex-cloud/bin/yc', 'compute', 'instance', 'get', server], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        rc = p.returncode

        if(rc == 0):
            result = re.search(r"(status: )(\w*)\n", output.decode("utf-8"))

            status = result.group(2)


            if(status == 'STOPPED'):
                print("Current status of {0}: {1}, staring server".format(server, status))
                #print("Current status: " + status +  "\nStarting server " + server)
                p = Popen(['/root/yandex-cloud/bin/yc', 'compute', 'instance', 'start', server], stdin=PIPE, stdout=PIPE, stderr=PIPE)
                output, err = p.communicate(b"input data that is passed to subprocess' stdin")
                rc = p.returncode
                if(rc == 0):
                    print("Instance {0} started successfully".format(server))
                else:
                    print("Error while starting instance {0}, error code {1}".format(server, rc))
                
            else:
                print("Current status of {0}: {1}, do nothing...".format(server, status))
        else:
            print("Error while accessing instance {0}, error code {1}".format(server, rc))


#Script 
if(__name__=='__main__'):

    
    if(len(sys.argv) > 1):
        for server in sys.argv[1:]:
            startInstance(server)    
    else:
        print("Please specify server in Yandex Cloud")