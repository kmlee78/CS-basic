#include <stdio.h>
#define NUMBER 5

int main(void)
{
    int i, j;
    // 5개의 정수를 입력받아서 가장 큰 수를 출력하는 프로그램
    int max, index;
    int score[NUMBER]; // 크기 5인 배열 선언
    max = 0;
    index = 0;
    for (i = 0; i < NUMBER; i++)
    {
        scanf("%d", &score[i]);
        if (max < score[i])
        {
            max = score[i];
            index = i;
        }
    }
    printf("가장 큰 수는 %d번째 수 %d입니다.\n", index + 1, max);

    // 2차원 배열을 활용하여 5명의 학생의 3과목 점수를 입력받아서 각 학생의 총점을 출력하는 프로그램
    int students[NUMBER][3];
    int total[3] = {
        0,
    }; // 총점을 저장할 배열, 모든 요소를 0으로 초기화
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 3; j++)
        {
            scanf("%d", &students[i][j]);
            total[i] += students[i][j];
        }
    }
    for (i = 0; i < 5; i++)
    {
        printf("%d번째 학생의 총점은 %d점입니다.\n", i + 1, total[i]);
    }

    return 0;
}