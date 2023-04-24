// hw0205.c
#include <string.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <stdbool.h>
#include <signal.h>  
#include <setjmp.h>
#include "ContributionCalculate.h"
sigjmp_buf env; 
void recvSignal(int sig) {  
    // printf("received signal %d !!!\n",sig);  
    siglongjmp(env,1);  
}
void handle_alarm(int signal) {
    // printf("signal = %d\n", signal);
    siglongjmp(env,2);
}
int main(void){
    int r;
    r = sigsetjmp(env, 1);
    if(r == 0){
        signal(SIGSEGV, recvSignal);
        signal(SIGALRM, handle_alarm);
        alarm(1);
        searchCommitInformationByHashVal("1cdbc6ec");
        alarm(0);
    }
    else if(r == 1){
        printf("You segmentation fault. Go back to checkpoint!\n");
    } 
    else{
        printf("You died. Go back to checkpoint!\n");
    }
    
    r = sigsetjmp(env, 1);
    if(r == 0){
        signal(SIGSEGV, recvSignal);
        signal(SIGALRM, handle_alarm);
        alarm(1);
        searchCommitInformationByHashVal("20421a42");
        alarm(0);
    }
    else if(r == 1){
        printf("You segmentation fault. Go back to checkpoint!\n");
    } 
    else{
        printf("You died. Go back to checkpoint!\n");
    }
    
    
    r = sigsetjmp(env, 1);
    if(r == 0){
        signal(SIGSEGV, recvSignal);
        signal(SIGALRM, handle_alarm);
        alarm(1);
        searchCommitInformationByHashVal("1a712217");
        alarm(0);
    }
    else if(r == 1){
        printf("You segmentation fault. Go back to checkpoint!\n");
    } 
    else{
        printf("You died. Go back to checkpoint!\n");
    }
    
    r = sigsetjmp(env, 1);
    if(r == 0){
        signal(SIGSEGV, recvSignal);
        signal(SIGALRM, handle_alarm);
        alarm(1);
        searchCommitInformationByHashVal("5f579554");
        alarm(0);
    }
    else if(r == 1){
        printf("You segmentation fault. Go back to checkpoint!\n");
    } 
    else{
        printf("You died. Go back to checkpoint!\n");
    }
    
    r = sigsetjmp(env, 1);
    if(r == 0){
        signal(SIGSEGV, recvSignal);
        signal(SIGALRM, handle_alarm);
        alarm(1);
        searchCommitInformationByHashVal("cfe22e1c");
        alarm(0);
    }
    else if(r == 1){
        printf("You segmentation fault. Go back to checkpoint!\n");
    } 
    else{
        printf("You died. Go back to checkpoint!\n");
    }
    
    r = sigsetjmp(env, 1);
    if(r == 0){
        signal(SIGSEGV, recvSignal);
        signal(SIGALRM, handle_alarm);
        alarm(1);
        searchCommitInformationByHashVal("5bc1f331");
        alarm(0);
    }
    else if(r == 1){
        printf("You segmentation fault. Go back to checkpoint!\n");
    } 
    else{
        printf("You died. Go back to checkpoint!\n");
    }
    
    r = sigsetjmp(env, 1);
    if(r == 0){
        signal(SIGSEGV, recvSignal);
        signal(SIGALRM, handle_alarm);
        alarm(1);
        searchMonthlyContribution("Oct");
        alarm(0);
    }
    else if(r == 1){
        printf("You segmentation fault. Go back to checkpoint!\n");
    } 
    else{
        printf("You died. Go back to checkpoint!\n");
    }
    
    r = sigsetjmp(env, 1);
    if(r == 0){
        signal(SIGSEGV, recvSignal);
        signal(SIGALRM, handle_alarm);
        alarm(1);
        searchMonthlyContribution("Nov");
        alarm(0);
    }
    else if(r == 1){
        printf("You segmentation fault. Go back to checkpoint!\n");
    } 
    else{
        printf("You died. Go back to checkpoint!\n");
    }
    
    r = sigsetjmp(env, 1);
    if(r == 0){
        signal(SIGSEGV, recvSignal);
        signal(SIGALRM, handle_alarm);
        alarm(1);
        searchMonthlyContribution("Dec");
        alarm(0);
    }
    else if(r == 1){
        printf("You segmentation fault. Go back to checkpoint!\n");
    } 
    else{
        printf("You died. Go back to checkpoint!\n");
    }
    return 0;
}