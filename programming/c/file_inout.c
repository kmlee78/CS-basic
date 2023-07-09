#include <stdio.h>
#include <string.h>

int main(void)
{
    // HI라는 글자를 저장하고 있는 output.txt라는 파일을 만드는 프로그램
    FILE *fp = NULL;
    fp = fopen("output.txt", "w"); // 쓰기 모드
    if (fp == NULL)                // 파일을 읽어올 수 없는 경우
    {
        printf("파일 읽기 실패");
        return 0;
    }
    fputc('H', fp); // 한글자씩 문자 입력
    fputc('I', fp);
    fclose(fp);

    // 이미 존재하는 파일에서 문자를 하나하나 읽어오는 프로그램
    int c;
    fp = fopen("input.txt", "r"); // 읽기 모드
    if (fp == NULL)
    {
        printf("파일 읽기 실패");
        return 0;
    }
    while ((c = fgetc(fp)) != EOF) // 파일의 끝(End Of File)까지 문자를 읽어온다.
    {
        putchar(c); // 읽어온 문자를 화면에 출력한다.
    }
    return 0;
}