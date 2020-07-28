//
//  main.cpp
//  DataStructuresHW1
//
//  Created by kimberly scirotto on 2/4/20.
//  Copyright © 2020 kimberly scirotto. All rights reserved.
//

#include <iostream>
#include "bag.h"
#include <cstdlib>


int main()
{
    Bag bag;
    int choice = 0;
    int data = 0;
    //Main menu for program
    cout << "1. Insert " << endl;
    cout << "2. Remove" << endl;
    cout << "3. Display All Values " << endl;
    cout << "4. Quit" << endl;
    cin >> choice;
    //will run until 4 is entered
    while(choice != 4)
    {
        //make sure number is valid
        while(choice <= 0 || choice >= 5){
            cout << "Invalid Choice. Enter 1-4: ";
            cin >> choice;
        }
        if(choice == 1){
            cout << "Enter what you want in bag: ";
            cin >> data;
            bag.insertNode(data);
            
        }
        if(choice == 2){
            bag.removeNode(); 
        }
        if(choice == 3){ 
            bag.display();
        }
        cout << "1. Insert " << endl;
           cout << "2. Remove" << endl;
           cout << "3. Display All Values " << endl;
           cout << "4. Quit" << endl;
           cin >> choice;
    }
}
