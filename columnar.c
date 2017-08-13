#include<stdio.h>
#include<string.h>
void main()
{
	char input[50],cipherText[50];
	char matrix[17][3],decrypt[17][3];
	int length,i=0,j=0,k=0,rows,adjustment;
	printf("Enter the plain text ");
	gets(input);
	length=strlen(input);
	rows= length/3;
	if(length%3!=0)
	{
		rows++;
	}

	while(k<length)
	{
		matrix[i][j++%3]=input[k];
		if(j%3==0)
			i++;
		k++;


	}

	if(length%3 == 1)
	{
		matrix[rows-1][1]='X';
		matrix[rows-1][2]='X';

	}
	else if(length%3 == 2)
		matrix[rows-1][2]='X';





		printf("Before Enc \n");

	for(i=0;i<rows;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%c\t",matrix[i][j] );
		}
		printf("\n");
	}

	printf("\n");

	printf("The cipher text is:\n");
	k=0;

	for(i=0;i<3;i++)
	{
		for(j=0;j<rows;j++)
		{
			cipherText[k++]=matrix[j][i];
		}
		
	}




	for(i=0;i<length;i++)
	{
		if(cipherText[i]!='X')
		printf("%c", cipherText[i]);

	}
	printf("\n");
printf("\n");

	k=0;
	i=0;
	j=0;

	if(length % 3 != 0)
	adjustment = (length + (3- (length%3) ) );
	
	else
		adjustment = length;

	while( k < adjustment )
	{
		decrypt[i++%rows][j]=cipherText[k];

		if(i%rows==0)
		{
			j++;

		}
		k++;


	}


	printf("After dec \n");


	for(i=0;i<rows;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%c\t",decrypt[i][j] );
		}
		printf("\n");
	}


	printf("\n");
	k=0;

	printf("The decrypted text is \n");
	for(i=0;i<rows;i++)
	{
		for(j=0;j<3;j++)
		{
			if(decrypt[i][j]!='X')
				printf("%c",decrypt[i][j]);
		}
	}
	

	printf("\n \n");





}