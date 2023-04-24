// hw0205.c
#include <stdio.h>
#include "ContributionCalculate.h"
int main(void){
    searchCommitInformationByHashVal("1cdbc6ec");
    searchCommitInformationByHashVal("20421a42");
    searchCommitInformationByHashVal("1a712217");
    searchCommitInformationByHashVal("5f579554");
    searchCommitInformationByHashVal("cfe22e1c");
    searchCommitInformationByHashVal("5bc1f331");
    searchMonthlyContribution("Oct");
    searchMonthlyContribution("Nov");
    searchMonthlyContribution("Dec");
    return 0;
}