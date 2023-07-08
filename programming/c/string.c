#include <stdio.h>
#include <string.h> // 문자열을 다루는 함수들이 선언된 헤더 파일

int main(void)
{
    // 문자열을 입력받아서 문자열의 길이를 출력하는 프로그램
    char input[1001]; // 1000자 이하의 문자열을 저장할 배열
    gets(input);      // 문자열을 입력받을 수 있는 gets 함수
    // scanf("%s", input);로도 문자열을 입력받을 수 있지만, 공백을 포함한 문자열을 입력받을 수 없다.
    // 이때는 input은 문자열의 시작 주소를 가리키는 포인터 변수이기도 하므로 &를 붙이지 않는다.
    int count = 0;
    while (input[count] != "\0") // 문자열의 끝을 만날 때까지 반복. \0은 null을 의미
    {
        count++;
    }
    printf("문자열의 길이는 %d입니다.\n", count);
    printf("%s", input); // %s는 문자열을 출력하는 서식 문자

    char str[5] = "abcd";
    char str2[5] = "efgh";
    // strlen 함수는 문자열의 길이를 구하는 함수
    printf("%d", strlen(str));
    // strcmp 함수는 두 문자열을 비교하는 함수
    printf("%d", strcmp(str, str2)); // str이 str2보다 사전적으로 앞에 있으면 -1이 출력, str2가 앞에 있으면 1이 출력, 같으면 0이 출력
    // strcpy 함수는 문자열을 복사하는 함수
    strcpy(str, str2); // str2를 str에 복사
    printf("%s", str); // efgh
    return 0;
}