#include <stdio.h>
#include <unistd.h>
#include <sys/types.h> // pid_t 타입을 위해 추가하는 것이 좋습니다.

int main()
{
    // 1. 부모 프로세스의 PID 출력
    printf("Parent process (Original) PID: %d\n", getpid());

    // 2. fork() 호출
    pid_t pid = fork();

    if (pid < 0) {
        // fork 실패 시 처리
        fprintf(stderr, "Fork failed");
        return 1;
    } 
    else if (pid == 0) {
        // 3. 자식 프로세스 영역
        printf("Child process PID: %d, Parent PID: %d\n", getpid(), getppid());
    } 
    else {
        // 4. 부모 프로세스 영역 (pid > 0)
        // 자식이 종료될 때까지 잠시 기다려주는 것이 좋습니다.
        sleep(1); 
        printf("Parent process again PID: %d\n", getpid());
    }

    return 0;
}