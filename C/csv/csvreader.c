#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define BSIZE 1024
#define NDATA 17000
struct table
{
	int rank;
	char* name;
	char* platform;
	int year;
	char* genre;
	char * publisher;
	float NA_Sales;
	float EU_Sales;
	float JP_Sales;
	float Other_Sales;
	float Global_Sales;
};


int main()
{
	char filename[] = "vgsales.csv";
	char buffer[BSIZE];
	FILE *f;
	char *field;
	int Rank;
	struct table data[NDATA];
	int counter = 0;

	/* open the CSV file */
	f = fopen(filename,"r");
	if( f == NULL)
	{
		printf("Unable to open file '%s'\n",filename);
		exit(1);
	}

	/* process the data */
	/* the file contains 11 fields in a specific order:
	   Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,
	   EU_Sales,JP_Sales,Other_Sales,Global_Sales
	   separated by commas */
	while(fgets(buffer,BSIZE,f))
	{
		field=strtok(buffer,",");
		data[counter].rank = atoi(field);
		field=strtok(NULL,",");
		data[counter].name = field;
		field=strtok(NULL,",");
		data[counter].platform = field;
		field=strtok(NULL,",");
		data[counter].year=atoi(field);
		field=strtok(NULL,",");
		data[counter].genre = field;
		field=strtok(NULL,",");
		data[counter].publisher = field;
		field=strtok(NULL,",");
		data[counter].NA_Sales = atof(field);
		field=strtok(NULL,",");
		data[counter].EU_Sales = atof(field);
		field=strtok(NULL,",");
		data[counter].JP_Sales = atof(field);
		field=strtok(NULL,",");
		data[counter].Other_Sales = atof(field);
		field=strtok(NULL,",");
		data[counter].Global_Sales = atof(field);
		if (counter % 1000==0){
				printf("RECORD--->%d, %s, %s, %d, %s, %s, %f, %f, %f, %f, %f\n",
				data[counter].rank,data[counter].name,
				data[counter].platform,data[counter].year,data[counter].genre,
				data[counter].publisher,data[counter].NA_Sales,data[counter].EU_Sales,
				data[counter].JP_Sales,data[counter].Other_Sales,data[counter].Global_Sales);
				
		}
		counter++;
	}

	/* close file */
	fclose(f);
	printf("Record letti: %d\n",counter);

	return(0);
}

