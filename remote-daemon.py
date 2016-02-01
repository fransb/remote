import sys
import time
import remote
from daemon import Daemon

class YourCode(object):
    def run(self):
        while True:
            
            fh = open("/tmp/remote.txt","a")
            fh.write("test1")
            fh.close()


            remote.run()
            time.sleep(1)

class MyDaemon(Daemon):
    def run(self):

        fh = open("/tmp/remote.txt","a")
        fh.write("test")
        fh.close()

        # Or simply merge your code with MyDaemon.
        your_code = YourCode()
        your_code.run()

if __name__ == "__main__":
    fh = open("/tmp/remote.txt","w")
    fh.write("Hello World")
    fh.close()
    daemon = MyDaemon('/tmp/remote-daemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
