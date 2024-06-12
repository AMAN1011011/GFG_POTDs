//Driver Code start

//Creating a class named solution
class Solution {
  public:

  //takes a single integer parameter n and returns an integer
  //This function is defined within the Solution class and is intended to count how many numbers from 0 to n contain the digit '4'.
  int countNumberswith4(int n) {
        // code here
        //This line declares and initializes an integer variable count to 0
        int count = 0;
        //This line starts a for loop that will iterate from 0 to n, inclusive.
        for (int i = 0; i <= n; i++) {

            //checks if the current number i contains the digit '4'.
            if (to_string(i).find("4") != std::string::npos) {

                //If the if condition is true, this line increments the count variable by 1.
                count++;
            }
        }
        return count;
    }
};


//Driver Code Ends