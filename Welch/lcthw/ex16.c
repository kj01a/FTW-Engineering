#include<stdio.h>
#include<assert.h>
#include<stdlib.h>
#include<string.h>

struct Person{
    char *name;
    int age;
    int height;
    int weight;
};

struct Person *Person_create(char *name, int age, int height, int weight){
    struct Person *who = malloc(sizeof(struct Person));
    assert(who != NULL);
    
    who->name = strdup(name);
    who->age = age;
    who->height = height;
    who->weight = weight;
    
    return who;
}

void Person_destroy(struct Person *who){
    assert(who != NULL);
    free(who->name);
    free(who);
}

void Person_print(struct Person *who){
    printf("Name: %s\n", who->name);
    printf("\tAge: %d\n", who->age);
    printf("\tHeight: %d\n", who->height);
    printf("\tWeight: %d\n\n", who->weight);
}

int main(int argc, char *argv[]){
    //create two people structs
    struct Person *kj = Person_create("KJ", 26, 75, 270);
    struct Person *curt = Person_create("Curt", 4, 6, 900);
    
    //print people and their memory address
    printf("KJ is at address: %p\n", kj);
    Person_print(kj);
    
    printf("Curt is at address: %p\n", curt);
    Person_print(curt);
    
    //age + 20, print again
    kj->age += 20;
    kj->height -= 60;
    kj->weight += 5000;
    Person_print(kj);
    
    curt->age += 20;
    Person_print(curt);
    
    //destory people, clean up
    Person_destroy(kj);
    Person_destroy(curt);
    
    return 0;
}
