#include <iostream>
#include <vector>

using namespace std;


int left(int i);

int right(int i);

int parent(int i);

void print_vect(vector<double>& vect_nums);

void swap(vector<double>& vect_nums, int i, int j);

void max_heapify(vector<double>& vect_nums, int last_i, int i);

void build_max_heap(vector<double>& vect_nums);

void heap_sort(vector<double>& vect_nums);

int main()
{
	vector<double> vect_nums = {42.4, 1, 4.523, 0, -1.2141, 50.5, 10, 1000, -523}; // test array
	print_vect(vect_nums);
	heap_sort(vect_nums);
	print_vect(vect_nums);
}


int left(int i)
{
	// index of i's left child
	int left_child_i = i*2 + 1;
	return left_child_i;
}

int right(int i)
{
	// index of i's right child
	int right_child_i = i*2 + 2;
	return right_child_i;
}

int parent(int i)
{
	// index of i's parent
	int parent_i = (i-1)/2;
	return parent_i;
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

void max_heapify(vector<double>& vect_nums, int last_i, int i)
{
	// heapify i and i's children. If i's children are greater than i,
	//swaps i's value with child's value recursively calls on the child's index
	int left_i = left(i);
	int right_i = right(i);
	int largest_i = i;

	if ((left_i <= last_i) && (vect_nums[left_i] > vect_nums[i])) // compare i's val with left_i's val
	{
		largest_i = left_i;
	}
	if ((right_i <= last_i) && (vect_nums[right_i] > vect_nums[largest_i])) // compare i's val with right_i's val
	{
		largest_i = right_i;
	}
	if (largest_i != i) // if there are any changes, recursively calls on the child's index
	{
		swap(vect_nums, i, largest_i);
		max_heapify(vect_nums, last_i, largest_i);
	}
}

void build_max_heap(vector<double>& vect_nums)
{
	// build max heap. Use max_heapify from the parent of the last leaf to the 0th index.
	int last_i = vect_nums.size() - 1;
	int start_i = parent(last_i); // any index greater than this is a leaf
	for (int i=start_i; i>=0; --i)
	{
		 max_heapify(vect_nums, last_i, i);
	}
}

void heap_sort(vector<double>& vect_nums)
{
	// perform heap sort on the given unsorted vector
	build_max_heap(vect_nums); // build max heap out of the vector
	int last_i = vect_nums.size() - 1;
	while(last_i > 0)
	{
		swap(vect_nums, 0, last_i); // swap the 0th(largest) node with the last_i
		last_i-=1;
		max_heapify(vect_nums, last_i, 0); // max_heapify on the heap with one less node, leaving out the largest at the end
	}
}

