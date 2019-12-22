#include<vector>
#include<iostream>
#include <stdlib.h> // srand, rand
#include <time.h>  // time

using namespace std;


void print_vect(vector<double>& vect_nums);

void swap(vector<double>& vect_nums, int i, int j);

void quick_sort(vector<double>& vect_nums, int begin_i, int end_i);


int main()
{
	vector<double> vect_nums = {42.4, 1, 4.523, 0, -1.2141, 50.5, 10, 1000, -523}; // test array
	print_vect(vect_nums);
	srand(time(NULL)); // insure a different seed for the rand number
	quick_sort(vect_nums, 0, vect_nums.size()-1);
	print_vect(vect_nums);
}


void print_vect(vector<double>& vect_nums)
{
	for (int i=0; i< vect_nums.size(); ++i)
	{
		cout << vect_nums[i] << " ";
	}
	cout << endl;
}

void swap(vector<double>& vect_nums, int i, int j)
{
	// swap 2 values in the vect
	double temp = vect_nums[i];
	vect_nums[i] = vect_nums[j];
	vect_nums[j] = temp;
}


void quick_sort(vector<double>& vect_nums, int begin_i, int end_i)
{
	int forward_i=begin_i;  // init starting index to be iterated forward
	int backward_i=end_i;   // init ending index to be iterated backward

	if ((end_i - begin_i) > 0) // check that there are at least 2 numbers to be sorted
	{
		int pivot_i = rand() % (end_i - begin_i + 1) + begin_i;
		double pivot_val=vect_nums[pivot_i]; // chose a pivot randomly

		while(forward_i < backward_i) // iterate from both ends until inds meet
		{
			if (vect_nums[forward_i] <= pivot_val)
			{
				if (vect_nums[backward_i] > pivot_val)
				{
					backward_i-=1; // iterate backward_i if the value is already
					  	  	  	   //to the right of pivot is > than pivot
				}
				forward_i+=1; // iterate forward_i if the value is already
							  //to the left of pivot is < than pivot
			}

			else
			{
				if (vect_nums[backward_i] <= pivot_val)
				{
					swap(vect_nums, forward_i, backward_i); // swap to insure the val to the left of
															// pivot is < than pivot and val to the right is >
					if (vect_nums[forward_i] == pivot_val) // check if the resulting swapped index is a pivot
					{
						pivot_i = forward_i;
					}
					forward_i+=1; // iterate forward_i as it's value is now < than pivot
				}
				backward_i-=1; // iterate backward_i as it's value is > than pivot
			}
		}

		if (vect_nums[forward_i] > pivot_val)
		{
			forward_i-=1; // correct i to be the index of the last val that is <= pivot
		}
		swap(vect_nums, forward_i, pivot_i); // place pivot in the correct spot
		pivot_i = forward_i; // correct the index of the pivot

		quick_sort(vect_nums, begin_i, pivot_i - 1);
		quick_sort(vect_nums, pivot_i + 1, end_i);
	}
}




