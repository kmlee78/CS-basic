#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct student
{
    int number;
    char name[10];
    double grade;
};

struct point
{
    int x;
    int y;
};

int main(void)
{
    // 구조체 변수를 선언하는 방법
    struct student s;
    s.number = 20150001;
    strcpy(s.name, "홍길동");
    s.grade = 4.5;
    printf("학번: %d\n이름: %s\n학점: %.1f\n", s.number, s.name, s.grade); // 학번: 20150001 이름: 홍길동 학점: 4.5

    // 두 점 사이의 거리를 구하는 프로그램
    struct point p1, p2;
    int xDiff, yDiff;
    double distance;
    scanf("%d %d", &p1.x, &p1.y);
    scanf("%d %d", &p2.x, &p2.y);
    xDiff = p1.x - p2.x;
    yDiff = p1.y - p2.y;
    distance = sqrt(xDiff * xDiff + yDiff * yDiff);
    printf("%f", distance);

    return 0;
}