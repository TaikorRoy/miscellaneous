#include <stdio.h>

int main ()
{
   FILE *fp;

   fp = fopen("file.txt","w+");
   fputs("This is tutorialspoint.com", fp);

   fseek( fp, -1, SEEK_END );
   fputs("@", fp);
   fclose(fp);

   return(0);
}
