class Solution {
public:
    vector<vector<int>> result;
    void PrintSubset(vector<int>&arr, vector<int>&ans, int i){
    //Base case
    if(i==arr.size()){
        result.push_back(ans);
        return;
    }
    //Include current element
    ans.push_back(arr[i]);
    PrintSubset(arr,ans,i+1);

    //Backtrack
    ans.pop_back();

    // Exclude current element
    PrintSubset(arr,ans,i+1);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> ans;
        PrintSubset(nums,ans,0);
        return result;
        
    }
};