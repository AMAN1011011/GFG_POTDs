class Solution {
  public:
    int rowWithMax1s(vector<vector<int> > &arr) {
        int maxi=0,ind=-1;
        for(int i=0;i<arr.size();i++)
        {
            int c=0;
            int j=arr[i].size()-1;
            while(arr[i][j]!=0){
                c++;
                j--;
            }
            if(maxi<c){
                maxi=c;
                ind=i;
            }
        }
        return ind;
    }
};
