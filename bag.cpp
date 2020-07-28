//
//  bag.cpp
//  DataStructuresHW1
//
//  Created by kimberly scirotto on 2/4/20.
//  Copyright © 2020 kimberly scirotto. All rights reserved.
//

#include "bag.h"
#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

Bag::Bag()
{
    head = NULL;
    current = NULL;
    temp = NULL;
    
}
Bag::~Bag()
{
    while(head != NULL)
    {
        temp = head;
        head = head->next;
        delete temp;
    }
    delete head;
}
void Bag::insertNode(int insrtBag)
{
    //creates new node to be inserted
    node *p = new node;
    p->data = insrtBag;
    p->next = NULL;
    //checks if this is the first item in the bag
    if(head != NULL)
    {
        current = head;
        while(current->next != NULL)
        {
            current = current->next;
        }
         current->next = p;
    }
    //works if more one item in bag
      else
      {
          head = p;
          current = head;
      }
}
int Bag::removeNode()
{
    int count = 0;
    //checks if bag is empty. returns -1 if it is
    if(head == NULL){
        cout << "Bag is empty" << endl;
        return -1;
    }
    //checks if item to remove is last in bag. If so removes it and returns value removed
    if(head->next==NULL){
        cout << head->data << " was removed." << endl;
        while(head != NULL)
        {
            temp = head;
            head = head->next;
        }
        delete head;
        return temp->data;
    }
    current = head;
    //loop to count how many items in Bag
    while(current -> next != NULL) {
        current = current->next;
        count++;
    }
    //gets random number for item to be removed
    int random = rand() % count;
    current = head;
    //Cycles through bag until random item is found. returns and removes that item
    for(int i = 0;i < count;i++){
        if(i == random){
            cout << current->data << " was removed." << endl;
            current->data = current->next->data;
            temp = current->next->next;
            delete current->next;
            current->next = temp;
            return current->data;
        }
        current = current->next;
    }
    
    return 0;
}
void Bag::display(){
    if(head == NULL){
        cout << "Bag empty" << endl;
    }
    current = head;
    while(current != NULL ) {
        for(int x = 0; x < 5; x++){
            while(current != NULL){
                cout << left << setw(5) << current->data << "  ";
                current = current->next;
            }
        }
        cout << endl;
    }
}
ostream &operator<<(ostream &output, const Bag &value){
    output << value.current->data;
    return output;
}
 
