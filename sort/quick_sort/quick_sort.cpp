#include<vector>
#include<iostream>
#include <chrono>
#include <math.h>

//#include <stdlib.h>     /* srand, rand */
//#include <time.h>       /* time */

using namespace std;

void switch_vals(vector<double>& v, int i, int j)
{
	double buffer_temp;
	buffer_temp = v[i];
	v[i] = v[j];
	v[j] = buffer_temp;
}

vector<double> rand_vect(int size_vector, int max_val, int min_val)
{
	vector<double> rand_v = {};
	double rand_val;
	for (int i=0; i < size_vector; ++i)
	{
		rand_val = rand() % (max_val - min_val + 1) + min_val;
		rand_v.push_back(rand_val);
	}

//	for (int i=0; i < size_vector; ++i) // print out the vector after the quicksort
//	{
//		cout << rand_v[i] << ' ';
//	}

	return rand_v;
}


void quicksort(vector<double>& to_be_sort, int begin_ind, int end_ind)
	{
	int i=begin_ind;
	int j=end_ind;

	if ((end_ind - begin_ind) > 0)
	{
		int pivot_ind = rand() % (end_ind - begin_ind + 1) + begin_ind;  //begin_ind
//		cout << pivot_ind << endl;
		int pivot_val=to_be_sort[pivot_ind];
		while(i < j)
		{
			if (to_be_sort[i] <= pivot_val) // down down , down up
			{
				if (to_be_sort[j] > pivot_val)
				{
					j-=1;
				}
				i+=1;
			}

			else							//  up up , up down
			{
				if (to_be_sort[j] <= pivot_val)
				{
					switch_vals(to_be_sort, i, j);
					if (to_be_sort[i] == pivot_val) // check if the resulting index is a pivot
					{
						pivot_ind = i;
					}
					i+=1;
				}
				j-=1;
			}
		}

		if (to_be_sort[i] > pivot_val)
		{
			i-=1; // correct i to be the index of the last val that is <= pivot
		}
		switch_vals(to_be_sort, i, pivot_ind); // place pivot in the correct spot
		pivot_ind = i; // correct the index of the pivot

		quicksort(to_be_sort, begin_ind, pivot_ind - 1);
		quicksort(to_be_sort, pivot_ind + 1, end_ind);
	}
}


vector<double> test_speed(int number_trials, int size_vector, int max_val, int min_val)
{
	srand(time(NULL)); // insure a different seed for the rand number
	vector<double> results = {};
	for (int i=0; i<number_trials; ++i)
	{
		vector<double> rand_v = rand_vect(size_vector, max_val, min_val);
	    auto t0 = chrono::high_resolution_clock::now(); // timing
	    quicksort(rand_v, 0, size_vector-1);
		auto t1 = chrono::high_resolution_clock::now();
//	    cout<< endl << chrono::duration_cast<chrono::milliseconds>(t1-t0).count()<< " milliseconds\n";
		results.push_back(chrono::duration_cast<chrono::milliseconds>(t1-t0).count());
	    rand_v.erase(rand_v.begin(),rand_v.end());
	}
	return results;
}

int main()
{
	// test the speed of the algorithm via n tests with random numbers
	int number_trials = pow(10,1);
	int size_vector = pow(10,6);
	double max_val = pow(10,6);
	double min_val = -max_val;

	vector<double> results = test_speed(number_trials, size_vector, max_val, min_val);
//	for (int i=0; i < number_trials; ++i)
//	{
//		cout << results[i] << ' ';
//	}

	// print the average number of millisecs
	double average = 0;
	for (int i=0; i < number_trials; ++i)
	{
		average += results[i];
	}
	average = average/number_trials;
	cout << "Size of the vector: " << size_vector << ". With nums in range :" << min_val << " to " << max_val << endl;
	cout << "Average time for " << number_trials << " trials is " << average << " millisecs";
}



