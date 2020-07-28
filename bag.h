//
//  Header.h
//  DataStructuresHW1
//
//  Created by kimberly scirotto on 2/4/20.
//  Copyright © 2020 kimberly scirotto. All rights reserved.
//


#include <iostream>
#ifndef Header_h
#define Header_h

using namespace std;
struct node{
    int data;
   struct node *next;
};

class Bag
{
public:
    //constructor
    Bag();
    //destructor
    ~Bag();
    //function to insert a new node into bag
    void insertNode(int insrtBag);
    //function to remove random node from bag
    int removeNode();
    //fuction to display contents of bag 5 per line
    void display();
    //overload << to work with Bags
    friend ostream &operator<<(ostream &output, const Bag &value);
    
private:

    node *head;
    node *current;
    node *temp;
    
};


#endif /* Header_h */
