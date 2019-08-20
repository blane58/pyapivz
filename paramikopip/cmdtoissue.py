def cmdtoissue(dog, command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = dog.exec_command(command_to_issue)
    return ssh_stdout.read().decode('UTF-8')
