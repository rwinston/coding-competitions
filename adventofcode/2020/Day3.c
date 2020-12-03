#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int trees(int* matrix[],  int rows, int cols, int down, int right) {
	int x = 0, y = 0, trees = 0;	
	while (y < rows) {
		trees += matrix[y][(x%cols)];
		x+=right; y+=down;
	}
	return trees;
}

int main(int argc, char* argv[]) {
	FILE* fp = fopen("p3", "r");
	char line[256];
	int rows = 0;
	int cols = 0;

	while (fgets(line, 256, (FILE*)fp) != NULL) {
		rows++;
		line[strcspn(line, "\r\n")] = 0;
		cols = strlen(line);
	}

	int** matrix = (int**)malloc(rows * sizeof(int*));
	rewind(fp);

	int i = 0;
	while (fgets(line, 256, (FILE*)fp) != NULL) {
		line[strcspn(line, "\r\n")] = 0;
		int* row = malloc(cols * sizeof(int));
		matrix[i] = row;
		char* c = line;
		for (int j = 0; j < cols; j++) {
			row[j] = (*c)=='#' ? 1 : 0;
			c++;
		}	
		i++;		
	}


	
	printf("Part 1: %d\n", trees(matrix, rows, cols, 1, 3));
	printf("Part 2: %d\n", 
			trees(matrix, rows, cols, 1, 1) * 
			trees(matrix, rows, cols, 1, 3) * 
			trees(matrix, rows, cols, 1, 5) * 
			trees(matrix, rows, cols, 1, 7) * 
			trees(matrix, rows, cols, 2, 1)); 


	fclose(fp);
	for (int i = 0; i < rows; ++i) { free(matrix[i]); }
	free(matrix);
	return 0;
}

