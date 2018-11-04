#include <stdio.h>
#include <stdlib.h>

FILE *outputfile;
int main() {
  outputfile = fopen("result.txt", "w");

  /* スタート */


  /* フィニッシュ */

  fclose(outputfile);
}

void JanPonKen(int times, int myH,int oppH,int myHH[],int oppHH[],int mP,int oP,char s[]) {
  if(times == 9) {

  }
}

int JanKen()

int saveToFile(str s) {      // 出力ストリーム

    // ファイルを書き込み用にオープン(開く)
  if (outputfile == NULL) {          // オープンに失敗した場合
    printf("cannot open\n");         // エラーメッセージを出して
    exit(1);                         // 異常終了
  }

  fprintf(outputfile, s); // ファイルに書く


}
