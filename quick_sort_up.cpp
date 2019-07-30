#include<vector>
#include<iostream>
#include <chrono>
#include <math.h>

using namespace std;

void switch_inds(vector<double>& v, int i, int j)
{
	// switch inds in the vector
	double buffer_temp;
	buffer_temp = v[i];
	v[i] = v[j];
	v[j] = buffer_temp;
}

vector<double> rand_vect(int size_vector, int max_val, int min_val)
{
	// create a random vector
	vector<double> rand_v = {};
	double rand_val;
	for (int i=0; i < size_vector; ++i)
	{
		rand_val = rand() % (max_val - min_val + 1) + min_val;
		rand_v.push_back(rand_val);
	}
	return rand_v;
}

void quicksort(vector<double>& to_be_sort, int begin_ind, int end_ind)
{
	// perform quicksort with in place replacement in the vector
	// Inputs: vector passed by the reference, initial sorting index, final sorting index

	vector<double> tmp_left_pivot = {};
	vector<double> tmp_right_pivot = {};

	int pivot_index=end_ind; // pivot is always chosen as the end member of the vector

	if ((end_ind - begin_ind) > 0) // check if there are numbers within the limits
	{
		for (int i = begin_ind; i <= end_ind; ++i) // iterate up to the pivot
			{
				if (i != pivot_index)
				{
					if (to_be_sort[i] <= to_be_sort[pivot_index])
					{
						tmp_left_pivot.push_back(to_be_sort[i]);
					}

					else
					{
						tmp_right_pivot.push_back(to_be_sort[i]);
					}
				}
			}

		tmp_left_pivot.push_back(to_be_sort[pivot_index]);
		pivot_index = begin_ind + tmp_left_pivot.size() - 1;

		for (int i = 0; i < tmp_left_pivot.size(); ++i) // iterate up to the pivot
			{
				to_be_sort[begin_ind+i] = tmp_left_pivot[i];
			}
		for (int i = 0; i < tmp_right_pivot.size(); ++i) // iterate up to the pivot
			{
				to_be_sort[begin_ind+i+tmp_left_pivot.size()] = tmp_right_pivot[i];
			}

		// erase the elements of vectors
		tmp_left_pivot.erase(tmp_left_pivot.begin(), tmp_left_pivot.end());
		tmp_right_pivot.erase(tmp_right_pivot.begin(), tmp_right_pivot.end());

		quicksort(to_be_sort, begin_ind, pivot_index-1);
		quicksort(to_be_sort, pivot_index+1, end_ind);
	}
}

vector<double> test_speed(int number_trials, int size_vector, int max_val, int min_val)
{
	// test the speed of the algorithm with several trials

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
	int size_vector = pow(10,5);
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



