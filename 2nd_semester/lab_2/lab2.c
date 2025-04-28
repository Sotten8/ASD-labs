#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct Node
{
    int info;
    struct Node *next;
} Node;

Node *init(int element)
{
    Node *new_node = malloc(sizeof(Node));
    if (!new_node)
    {
        printf("Unable to allocate memory.\n");
        exit(1);
    }
    new_node->info = element;
    new_node->next = NULL;
    return new_node;
}

void add_element(Node **head, int value)
{
    Node *new_node = init(value);
    if (*head == NULL)
    {
        *head = new_node;
    }
    else
    {
        Node *current = *head;
        while (current->next != NULL)
        {
            current = current->next;
        }
        current->next = new_node;
    }
}

void print_list(Node *head)
{
    while (head != NULL)
    {
        printf("%d ", head->info);
        head = head->next;
    }
    printf("\n");
}

void free_list(Node *head)
{
    while (head != NULL)
    {
        Node *temp = head;
        head = head->next;
        free(temp);
    }
}

void move_elements(Node *head)
{
    while (head != NULL)
    {
        Node *group = head;

        Node *current = group;
        for (int count = 10; count > 0 && current != NULL; current = current->next)
        {
            if (current->info >= 0)
            {
                Node *search = current->next;
                while (search != NULL && search->info >= 0)
                    search = search->next;

                if (search)
                {
                    int temp = current->info;
                    current->info = search->info;
                    search->info = temp;
                    count--;
                }
            }
            else
            {
                count--;
            }
        }

        for (int i = 0; i < 20 && head != NULL; i++)
        {
            head = head->next;
        }
    }
}

void manual_input(Node **head, int n)
{
    int count = 0, num;
    int toggle = 0;

    while (count < n)
    {
        printf("Enter %s number %d: ", toggle ? "positive" : "negative", count + 1);
        scanf("%d", &num);

        if ((toggle == 0 && num < 0) || (toggle == 1 && num > 0))
        {
            add_element(head, num);
            if (++count % 5 == 0)
                toggle = !toggle;
        }
        else
        {
            printf("Number must be %s.\n", toggle ? "positive" : "negative");
        }
    }
}

void auto_generate(Node **head, int n)
{
    int count = 0;
    int toggle = 0;

    while (count < n)
    {
        int num = (rand() % 50 + 1) * (toggle ? 1 : -1);
        add_element(head, num);
        count++;
        if (count % 5 == 0)
            toggle = !toggle;
    }
}

int main()
{
    Node *head = NULL;
    int n, mode;

    srand(time(NULL));

    printf("Enter n of elements (must be positive and multiple of 20): ");
    scanf("%d", &n);

    if (n <= 0 || n % 20 != 0)
    {
        printf("Number must be positive and multiple of 20!\n");
        return 1;
    }

    printf("Choose input mode: (1 - Manual, 2 - Auto): ");
    scanf("%d", &mode);

    if (mode == 1)
    {
        manual_input(&head, n);
    }
    else if (mode == 2)
    {
        auto_generate(&head, n);
    }
    else
    {
        printf("Invalid mode.\n");
        return 1;
    }

    printf("\nInitial list:\n");
    print_list(head);

    move_elements(head);

    printf("\nList after changes:\n");
    print_list(head);

    free_list(head);
    return 0;
}
