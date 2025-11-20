#include<iostream>
using namespace std;

int main(){

    int life = 4;

    int card = 40;
    int my_card = card;

    int *p = &card;
    int *myp = &my_card;

    int my = *myp;

    printf("Life: %d\n", life);
    printf("Card: %d\n", card);
    printf("Address of card: %p\n",&card);
    printf("My Card: %d\n", my_card);


    printf("Pointer to Card: %d\n", *p);
    printf("pointer P: %p\n",p);
    printf("Address of p: %p\n",&p);


    printf("Pointer to My Card: %d\n", *myp);
    printf("Value of My: %d\n", my);

    // printf("my = %p" my)
    return 0;
}