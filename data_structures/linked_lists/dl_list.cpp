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



int main(int argc, char const *argv[])
{
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

    // delete n1->next_node;
    // cout << n1->prev_node->item << " ";
    // cout << n1->item << " ";
    // cout << n1->next_node->item << " "<< endl;

    return 0;
}
