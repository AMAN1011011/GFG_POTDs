class Solution {
  public:
    Node* deleteNode(Node* &head, int x) {
        Node * NewNode = head;
        if (x>1)    {
            for (int i=1;i<x-1;i++)   {
                NewNode=NewNode->next;
            }
        }
        else head = NewNode->next;
        NewNode->next=NewNode->next->next;
        
        return head;
    }
};
