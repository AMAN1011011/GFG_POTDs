// User function Template for C++

class Solution {
  public:
    string doIntersect(int p1[], int p2[], int q1[], int q2[]) {
        // code here
        
        double m1=(p2[1]-p1[1])/double(p2[0]-p1[0]); 
        double m2=(q2[1]-q1[1])/double(q2[0]-q1[0]); 
        double v11=m1*(p1[0]-q1[0])-(p1[1]-q1[1]); 
        double v12=m1*(p1[0]-q2[0])-(p1[1]-q2[1]); 
        double v21=m2*(q1[0]-p1[0])-(q1[1]-p1[1]); 
        double v22=m2*(q1[0]-p2[0])-(q1[1]-p2[1]); 
        
        
        if(v11*v12>0 || v21*v22>0)return "false"; 
        return "true"; 
       
    }
};