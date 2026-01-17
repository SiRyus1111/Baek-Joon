#include <stdio.h>
#include <unistd.h>
#include <sys/types.h> 

int main()
{
    printf("Parent process (Original) PID: %d\n", getpid());

    pid_t pid = fork();

    if (pid < 0) {
        fprintf(stderr, "Fork failed");
        return 1;
    } 
    else if (pid == 0) {
        printf("Child process PID: %d, Parent PID: %d\n", getpid(), getppid());
    } 
    else {
        sleep(1); 
        printf("Parent process again PID: %d\n", getpid());
    }

    return 0;
}