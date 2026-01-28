#include <iostream>
#include <stack>

struct Node{
    char name;
    Node *left = nullptr;
    Node *right = nullptr;
};

void preorder(Node *root){

    std::stack<Node*> st;
    st.push(root);

    while (!st.empty()){
        Node* cur = st.top();
        st.pop();

        std::cout << cur->name;
        if (cur->right){
            st.push(cur->right);
        }
        if (cur->left){
            st.push(cur->left);
        }
    }
}

void inorder(Node *root){
    
    std::stack<Node*> st;
    Node* cur = root;

    while (cur != nullptr || !st.empty()){
        while (cur != nullptr){
            st.push(cur);
            cur = cur->left;
        }
        cur = st.top();
        st.pop();
        
        std::cout << cur->name;

        cur = cur->right;
    }
} 

void postorder(Node *root){
    std::stack<Node*> st;
    std::stack<char> res;
    st.push(root);
    Node* cur = root;

    while (!st.empty()){
        cur = st.top();
        st.pop();

        res.push(cur->name);

        if (cur->left){
            st.push(cur->left);
        }
        if (cur->right){
            st.push(cur->right);
        }
    }

    while (!res.empty()){
        std::cout << res.top();
        res.pop();
    }
}

int main(){
    int n;
    std::cin >> n;
    std::cin.ignore();

    Node tree[26];
    
    for(int i = 0; i < 26; i++) {
        tree[i].left = nullptr;
        tree[i].right = nullptr;
    }

    for (int i = 0; i < n; i++){
        char nodeName, left, right;
        std::cin >> nodeName >> left >> right;
        
        int index = nodeName - 'A';
        tree[index].name = nodeName;

        if (left != '.'){
            tree[index].left = &tree[left - 'A'];
        }
        if (right != '.'){
            tree[index].right = &tree[right - 'A'];
        }
    }
    Node *rootnode = &tree[0];
    preorder(rootnode);
    std::cout << '\n';
    inorder(rootnode);
    std::cout << '\n';
    postorder(rootnode);
}