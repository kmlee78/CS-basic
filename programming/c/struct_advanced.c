#include <stdio.h>
#include <math.h>

struct point
{
    int x;
    int y;
};

struct rect
{
    struct point p1;
    struct point p2;
};

// 두 점을 입력받아서 사각형의 넓이와 둘레를 출력하는 프로그램
int main(void)
{
    struct rect r;
    printf("왼쪽 상단 모서리 x, y 좌표를 입력하세요: ");
    scanf("%d %d", &r.p1.x, &r.p1.y);
    printf("오른쪽 하단 모서리 x, y 좌표를 입력하세요: ");
    scanf("%d %d", &r.p2.x, &r.p2.y);
    int width = abs(r.p2.x - r.p1.x);
    int height = abs(r.p2.y - r.p1.y);
    int area = width * height;
    int perimeter = 2 * (width + height);
    printf("넓이: %d\n둘레: %d\n", area, perimeter);

    return 0;
}