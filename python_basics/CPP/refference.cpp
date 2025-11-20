#include <iostream>
using namespace std;

void modifyWithPointer(int *p) {
    *p = 300; // Dereferencing pointer to change value
}

void modifyWithReference(int &r) {
    r = 500; // Directly modifying the reference
}

int main() {
    int score = 100;

    int *ptr = &score;           // Pointer to score
    int &ref = score;            // Reference to score

    cout << "Initial score: " << score << endl;
    cout << "Pointer points to: " << ptr <<", having a value: "<<*ptr << endl;
    cout << "Reference refers to: " << &ref <<", holding access to: "<< ref << endl;

    modifyWithPointer(ptr);      // Changes score to 300
    cout << "\nAfter modifyWithPointer:\n";
    cout << "score: " << score <<" and address of the pointer: "<< &ptr<<", still pointing to "<<ptr << endl;

    modifyWithReference(ref);    // Changes score to 500
    cout << "\nAfter modifyWithReference:\n";
    cout << "score: " << score <<" and address of the refference: "<< &ref<<", still holding access to "<<&score << endl;

    // Reassigning pointer
    int newScore = 999;
    ptr = &newScore;             // Now ptr points to newScore
    cout << "\nPointer reassigned to newScore:\n";
    cout << "*ptr: " << *ptr << endl;
    cout << "score still: " << score << endl;

    // Trying to reassign reference (not allowed)
    // int &ref = newScore; // ❌ Error: reference already bound

    return 0;
}