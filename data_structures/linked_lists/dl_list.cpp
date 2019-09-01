#include<iostream>
using namespace std;


class Node
{ // doubly linked node for the list
    public:
        double item; // item to be stored in the node
        Node* prev_node; // pointer to previous node in the list
        Node* next_node; // pointer to next node in the list
        //Constructors
        Node(double item); // init prev_node and next_node to NULL
        Node(double item, Node* prev_node, Node* next_node);
        // Destructors
        ~Node();
};

// Member functions definitions including constructor
Node::Node(double item)
{// initiate only the item, set the neighboring nodes to NULL
    this->item = item;
    this->prev_node = NULL;
    this->next_node = NULL;
};

Node::Node(double item, Node* prev_node, Node* next_node)
{// initiate the item, set the neighboring nodes pointers
    this->item = item;
    this->prev_node = prev_node;
    this->next_node = next_node;
};

Node::~Node()
{};

class DLList
{
    private:
        //TODO make size, head, tail private after testing
        int size; // size of the list 
        Node* head; // head node of the list
        Node* tail; // tail of the list

    public:
        DLList();   // constructor
        ~DLList();  // destructor
        void FrontInsert(double item); // insert a node with an item in front of the list
        void Print(); // print the items of the list
        int GetSize(); // get the size of the list
        Node* GetNode(int index); // return the node of the provided index, start from 0
        void RemoveNode(int index); // remove the node from the list at a given index, start from 0
};

DLList::DLList()
{   // initialize an empty list
    this->size = 0; 
    this->head = NULL;
    this->tail = NULL;
};

DLList::~DLList()
{};

void DLList::FrontInsert(double item)
{ // insert a node with an item in front of the list
    //TODO	this->head = new Node(item, NULL, this->head);
	Node* new_head_node = new Node(item, NULL, this->head);
	if (size != 0) // if the list is not empty
	{
		this->head->prev_node = new_head_node; // update the previous node of the head
	}
	else // if the list is empty
	{
		this->tail = new_head_node; // initialize a tail
	}
	this->head = new_head_node; // update the headnode
	size+=1; // increase the size of the array by 1
};

void DLList::Print()
{ // print out the items of the list. Go until the tail node or in case of the error until non NULL node
    Node* n = this->head;
    while(n != NULL) // the tail's next node is NULL
    {
        cout << n->item << " "; // print out the item
        n = n->next_node; // move to the next node
    }
    cout << endl;
};

int DLList::GetSize()
{// return the size of the array
	return size;
};

Node* DLList::GetNode(int index)
{ // search for the node given the index in the array, starting from i = 0
    //TODO write raise value error
    if ((index < 0) || (index >= size)) // if the index is outside the bounds of the list
    {
        return NULL;
    }
    else
    {
        Node* current_node = this->head;
        int current_i = 0;
        while(current_i != index)
        {
			current_node = current_node->next_node;
			current_i += 1;
        };
        return current_node;
    }
};

void DLList::RemoveNode(int index)
{// remove the node from the list at a given index, start from 0
	Node* node_to_remove = GetNode(index);

	if (node_to_remove != NULL) // insure that node at the index exists (index provided is not out of bounds)
	{
		if (index == 0) // special case when node is the head
		{
			this->head = node_to_remove->next_node; // reset the head
			this->head->prev_node = NULL; // set the previous point of the next node to NULL
		}
		else if (index == size-1) //special case when the node is the tail
		{
			this->tail = node_to_remove->prev_node; //reset the tail
			this->tail->next_node = NULL; // set the next pointer of the previous node to NULL
		}
		else
		{
			node_to_remove->next_node->prev_node = node_to_remove->prev_node;
			node_to_remove->prev_node->next_node = node_to_remove->next_node;
		}

		delete node_to_remove;
        size -= 1;
	}
	else
	{
		cout << "Index is out of bounds" << endl;
	}
}



int main(int argc, char const *argv[])
{


    // // TEST RemoveNode(int index)
    // DLList* new_ls = new DLList(); // initialize the list
    // new_ls->FrontInsert(3);
    // new_ls->FrontInsert(2.213);
    // new_ls->FrontInsert(1);

    // int ind = 2; // 1, 2 works, 
    // cout << "Before del" << endl;
    // new_ls->Print();
    // cout << new_ls->GetSize() << endl;
    // cout << "After del" << endl;
    // new_ls->RemoveNode(ind);
    // new_ls->Print();
    // cout << new_ls->GetSize() << endl;


    return 0;
}

    // ALL TESTS

    // // TEST Node(double item)
    // Node* n1 = new Node(3.212);
    // cout << n1->item << endl;

    // // TEST Node(double item, Node* prev_node, Node* next_node)
    // Node* n1 = new Node(1, new Node(0), new Node(2));
    // cout << n1->prev_node->item << " ";
    // cout << n1->item << " ";
    // cout << n1->next_node->item << " ";

    // // TEST ~Node()
    // Node* n1 = new Node(1, new Node(0), new Node(2));
    // cout << n1->prev_node->item << " ";
    // cout << n1->item << " ";
    // cout << n1->next_node->item << " "<< endl;
    //
    // delete n1->next_node;
    // cout << n1->prev_node->item << " ";
    // cout << n1->item << " ";
    // cout << n1->next_node->item << " "<< endl;

    // TEST DLList(), FrontInsert(double item)
    // // TEST 1 node
    // DLList* new_ls = new DLList(); // initialize the list
    // new_ls->FrontInsert(1.24141);
    // cout << new_ls->head->item << " ";
    // cout << new_ls->tail->item << " ";
    // cout << new_ls->size << endl;

    // // TEST 3 nodes
    // DLList* new_ls = new DLList(); // initialize the list
    // new_ls->FrontInsert(3);
    // new_ls->FrontInsert(2.213);
    // new_ls->FrontInsert(1);
    // cout << new_ls->head->item << " "; //head test
    // cout << new_ls->head->next_node->item << " "; // next node test
    // cout << new_ls->tail->prev_node->item << " "; // prev node test
    // cout << new_ls->tail->item << " "; // tail test
    // cout << new_ls->size << endl;

    // // TEST Print()
    // DLList* new_ls = new DLList(); // initialize the list
    // new_ls->FrontInsert(3);
    // new_ls->FrontInsert(2.213);
    // new_ls->FrontInsert(1);
    // new_ls->Print();

    // // // TEST GetNode(int index)
    // DLList* new_ls = new DLList(); // initialize the list
    // new_ls->FrontInsert(3);
    // new_ls->FrontInsert(2.213);
    // new_ls->FrontInsert(1);
    // cout << new_ls->GetNode(1)->item << endl;
    // cout << new_ls->GetNode(-10)->item << endl;
    // cout << new_ls->GetNode(10)->item << endl;

    // // TEST GetSize()
    // DLList* new_ls = new DLList(); // initialize the list
    // new_ls->FrontInsert(3);
    // new_ls->FrontInsert(2.213);
    // new_ls->FrontInsert(1);
    // cout << new_ls->GetSize();