#include <studio.h>

int main(void)
{
    // 문자열을 입력받아서 문자열의 길이를 출력하는 프로그램
    char input[1001]; // 1000자 이하의 문자열을 저장할 배열
    gets(input);      // 문자열을 입력받을 수 있는 gets 함수
    int count = 0;
    while (input[count] != "\0") // 문자열의 끝을 만날 때까지 반복. \0은 null을 의미
    {
        count++;
    }
    printf("문자열의 길이는 %d입니다.\n", count);
    printf("%s", input); // %s는 문자열을 출력하는 서식 문자
    return 0;
}