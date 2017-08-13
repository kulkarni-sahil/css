#include <stdio.h>
#include <string.h>
void main(){
    char a[50] , crypt[50] , decrypt[50];
    int n , k=3 ,i=0 , key ;
    printf("Enter a string:");
    scanf("%[0-9a-zA-Z ]", a);
    i=strlen(a);
    printf("%d\n",i);
    for(n=0 ; n<i ; n++){
        if(a[n] == ' ' )
            crypt[n] = ' ';
        else{
			if (a[n] >= 'A' && a[n] <= 'Z')
	             crypt[n] = (char)((((a[n]-65)+k)%26)+65);
			else if (a[n] >= 'a' && a[n] <= 'z')
				 crypt[n] = (char)((((a[n]-97)+k)%26)+97);
         }
    }
    crypt[n] = '\0';
    printf("Encrypted:");
    for(n=0; n<i ; n++){
        printf("%c",crypt[n]);
    }
   
    printf("\nDE:");
    for(n=0 ; n<i ; n++){
        if(crypt[n] == ' ' )
            decrypt[n] = ' ';
        else{
        	if (a[n] >= 'A' && a[n] <= 'Z')
	            key = (((crypt[n]-65)-k)%26);
	        else if (a[n] >= 'a' && a[n] <= 'z')
	        	key = (((crypt[n]-97)-k)%26);
            if(key < 0){
                key = 26 + key;
            }
           	if (a[n] >= 'A' && a[n] <= 'Z')
            	decrypt[n] = (char)((key+65));
            else if (a[n] >= 'a' && a[n] <= 'z')
            	decrypt[n] = (char)((key+97));
         }
    }
   
   
    for(n=0; n<i ; n++){
        printf("%c",decrypt[n]);
    }
    printf("\n");
}
