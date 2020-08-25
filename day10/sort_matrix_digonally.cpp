/*
****************Auther - Anand Keshari***************
problem link - https://leetcode.com/problems/sort-the-matrix-diagonally/
*/
class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int i=mat.size()-1,j=mat[0].size()-1;
        while(i>=0)
        {
            sort_a_digonal(mat,i,0);
            i--;
        }
        while(j--)
        {
            sort_a_digonal(mat,0,j);
        }
        return mat;
    }
    void sort_a_digonal(vector<vector<int>>& mat, int i, int j)
    {
        vector<int> copy;
        while(i<mat.size() && j<mat[0].size())
        {
            copy.push_back(mat[i][j]);
            i++;
            j++;
        }
        sort(copy.begin(),copy.end());
        i--;
        j--;
        while(copy.size())
        {
            
            mat[i][j]=copy[copy.size()-1];
            copy.pop_back();
            i--;
            j--;
        }
    }
};
