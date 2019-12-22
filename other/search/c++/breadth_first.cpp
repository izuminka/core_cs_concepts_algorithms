#include<iostream>
#include <vector>
using namespace std;

void print_mat(vector<vector<int>>& matrix)
{ // print out elements of the matrix
	for(int i=0; i<matrix.size(); ++i)
	{
		for (int j=0; j<matrix[i].size(); ++j)
		{
			cout<<matrix[i][j]<<" ";
		}
		cout<<endl;
	}
}

bool val_in_vect(vector<int>& vect, int value)
{ // check if the value is in the vector
	bool valIn=false;
	for(int i=0; i<vect.size(); ++i)
	{
		if (vect[i] == value)
		{
			valIn = true;
			break;
		}
	}
	return valIn;
}

int main()
{	// test for a graph
	vector<vector<int>> matrix =
			//                   TO
	{//  0   ,00  ,01  ,02  ,000 ,001 ,010 ,012 ,020 ,021 ,0010,0120
		{0   ,1   ,1   ,1   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   }, // 0
		{0   ,0   ,1   ,0   ,1   ,1   ,0   ,0   ,0   ,0   ,0   ,0   }, // 00
		{1   ,0   ,0   ,1   ,0   ,1   ,1   ,1   ,0   ,0   ,0   ,0   }, // 01
		{1   ,0   ,1   ,0   ,0   ,0   ,0   ,0   ,1   ,1   ,0   ,0   }, // 02
		{0   ,1   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   }, // 000
		{0   ,1   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   }, // 001    FROM
		{0   ,0   ,1   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,1   ,0   }, // 010
		{0   ,0   ,1   ,0   ,0   ,0   ,0   ,0   ,1   ,0   ,1   ,1   }, // 012
		{0   ,0   ,0   ,1   ,0   ,0   ,0   ,1   ,0   ,0   ,0   ,0   }, // 020
		{0   ,0   ,0   ,1   ,0   ,0   ,0   ,1   ,0   ,0   ,0   ,1   }, // 021
		{0   ,0   ,0   ,0   ,0   ,0   ,1   ,0   ,0   ,0   ,0   ,0   }, // 0010
		{0   ,0   ,0   ,1   ,0   ,0   ,0   ,1   ,0   ,0   ,0   ,0   }, // 0120
	};
	int init = 0; // inital node
	int final = 7; // destination node

	int que_count = 0;
	vector<int> que = {init};
	vector<int> visited = {init};
	bool stopBool=true;
	while(stopBool==true)	// iterate untill the node is found
	{
		for (int j=0; j<matrix[que_count].size(); ++j) // go through all connections of the node
		{
			if (matrix[que_count][j]==1) // index corresponds to the node, value corresponds to connection. 1 if connected
			{
				if (j == final)  // if that's the node that we are looking for then break
				{
					stopBool = false;
					break;
				}
				else
				{
					if (not val_in_vect(visited, j)) // if it's a new unvisited node
					{
						visited.push_back(j); // remember the visit
						for (int k=0; k<matrix[j].size(); ++k) // add the children of the node to the que
						{
							if (matrix[j][k]==1) // find the actual connections to children
							{
								if (not val_in_vect(visited, k)) // check if not visited
								{
									que.push_back(k);
								}

							}
						}

					}

				}
			}
		}
		que_count+=1; // move the the next node in the que
	}
}


