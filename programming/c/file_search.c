#include <stdio.h>
#include <string.h>

// 특정 파일에서 특정 단어를 검색하는 프로그램
int main(void)
{
    FILE *fp;
    char fname[256];
    char buffer[256];
    char word[256];
    int line = 0;

    printf("파일 이름을 입력하세요: ");
    scanf("%s", fname);
    if ((fp = fopen(fname, "r")) == NULL)
    {
        printf("파일을 열 수 없습니다.\n");
        return 0;
    }

    while (fgets(buffer, 256, fp)) // 파일에서 256의 길이만큼 읽어서 buffer에 저장한다.
    {
        line++;
        if (strstr(buffer, word)) // buffer에 word가 포함되어 있는지 확인한다.
        {
            printf("라인 %d: %s", line, buffer);
        }
    }
    fclose(fp);

    return 0;
}