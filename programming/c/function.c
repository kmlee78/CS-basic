#include <stdio.h>

int hour; // 전역 변수
int minute;
int minuteAdd;

void counter()
{
    minute += minuteAdd;
    hour += minute / 60;
    minute %= 60;
    hour %= 24;
}

int getDays(int month, int day)
{
    int i, sum = 0;
    for (i = 1; i < month; i++)
    {
        if (i == 2)
        {
            sum += 28;
        }
        else if (i % 2 == 1)
        {
            sum += 31;
        }
        else
        {
            sum += 30;
        }
    }
    sum += day;
    return sum;
}

int combination(int n, int r)
{
    if (n == r || r == 0)
    {
        return 1;
    }
    else
    {
        return combination(n - 1, r - 1) + combination(n - 1, r);
    }
}

int main(void)
{
    // 현재 시각에 분을 더하는 프로그램
    printf("시간, 분, 더할 분을 입력하세요: ");
    scanf("%d %d %d", &hour, &minute, &minuteAdd);
    counter();
    printf("더해진 시간은 %d시 %d분입니다.\n", hour, minute);

    // 월과 일을 입력받아서 1월 1일부터 몇일째인지 계산하는 프로그램
    int month, day;
    printf("월과 일을 입력하세요: ");
    scanf("%d %d", &month, &day);
    printf("1월 1일부터 %d월 %d일까지는 %d일째 되는 날입니다.\n", month, day, getDays(month, day));

    // 재귀함수를 이용하여 조합을 계산하는 프로그램
    int n, r;
    printf("n을 r을 입력하세요: ");
    scanf("%d %d", &n, &r);
    printf("%dC%d = %d\n", n, r, combination(n, r));

    return 0;
}