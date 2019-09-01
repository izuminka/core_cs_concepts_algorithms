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
        // Node(double item, Node* prev_node, Node* next_node);
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

int main(int argc, char const *argv[])
{
    // TEST constructor 1
    Node* n1 = new Node(3.212);
    cout << n1->item << endl;
    
    return 0;
}
