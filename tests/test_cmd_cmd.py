
if __name__ == '__main__':
    cmd = Cmd()
    #print(cmd.raw_os('ls /home/david', True, True))
    #cmd.shell(["ls /home/david | echo '1'"], verbose=True)
    #cmd.raw(["ls", "/home/david"], verbose=True)
    #cmd1 = Cmd(["ls","-a", "/home/david"])
    #cmd1.raw(verbose=True)
    cmd.raw_line("ls -a /home/david | echo '1'", verbose=True)
