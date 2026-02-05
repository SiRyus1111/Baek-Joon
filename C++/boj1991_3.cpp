#include <iostream>
#include <stack>

struct Node{
    char name;
    Node *pleft = nullptr;
    Node *pright = nullptr;
};

void preorder(Node* root){
    std::stack<Node*> st;
    st.push(root);

    while (!st.empty()){    
        Node* cur = st.top();
        st.pop();    
        
        std::cout << cur->name;    
        
        if (cur->pright) st.push(cur->pright);    
        
        if (cur->pleft) st.push(cur->pleft);    
    }

}

void inorder(Node* root){
    std::stack<Node*> st;
    Node* cur = root;

    while (cur != nullptr || !st.empty()){    
        while (cur != nullptr){    
            st.push(cur);    
            cur = cur->pleft;    
        }    
        
        cur = st.top();    
        st.pop();    
        
        std::cout << cur->name;    

        cur = cur->pright;    
}

}

void postorder(Node* root){
    std::stack<Node*> st;
    std::stack<char> result;
    st.push(root);

    while (!st.empty()){    
        Node* cur = st.top();    
        st.pop();    
        
        result.push(cur->name);    
        
        if (cur->pleft) st.push(cur->pleft);    
        
        if (cur->pright) st.push(cur->pright);    
    }    
    
    while(!result.empty()){    
        std::cout << result.top();    
        result.pop();    
    }

    }
int main()
{
    int n;
    std::cin >> n;
    std::cin.ignore();

    Node tree[26];    
    
    for (int i = 0; i < n; i++){    
        tree[i].pleft = nullptr;    
        tree[i].pright = nullptr;    
    }    
    
    for (int i = 0; i < n; i++){    
        char node, l, r;    
        std::cin >> node >> l >> r;    
        
        int index = node - 'A';    
        tree[index].name = node;    
        
        if (l != '.') tree[index].pleft = &tree[l - 'A'];    
        
        if (r != '.') tree[index].pright = &tree[r - 'A'];    
    }    
    
    preorder(&tree[0]);    
    std::cout << std::endl;    
    inorder(&tree[0]);    
    std::cout << std::endl;    
    postorder(&tree[0]);

}