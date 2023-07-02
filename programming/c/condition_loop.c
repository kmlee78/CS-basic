#include <studio.h>

int main(void)
{
    int score = 90;
    if (score >= 90)
    {
        printf("A");
    }
    else if (score >= 80)
    {
        printf("B");
    }
    else
    {
        printf("F");
    } // A 출력

    int i = 1, sum = 0;
    while (i <= 10)
    {
        sum += i;
        i++;
    } // sum에 1부터 10까지의 합인 55가 저장됨

    int j;
    int n = 10;
    int result = 0;
    for (j = 1; j <= n; j++) // c언어는 for문 안에서 int j = 1;처럼 초기화할 수 없음
    {
        result += j;
    } // result에 1부터 10까지의 합인 55가 저장됨

    return 0;
}