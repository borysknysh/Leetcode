class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        auto&& size_nums1 = static_cast<int>(nums1.size());
        auto&& size_nums2 = static_cast<int>(nums2.size());
        auto&& size = size_nums1+size_nums2;
        
        auto&& merged = mergedArray(nums1, nums2);
        if(size%2 == 0)
        {
            return (merged[size/2]+merged[size/2-1])/2.;
        }
        return static_cast<double>(merged[(size-1)/2]);
    }
    std::vector<int> mergedArray(const vector<int>& nums1, const std::vector<int>& nums2)
    {
        vector<int> temp;
        auto&& iter_nums1 = nums1.begin();
        auto&& iter_nums2 = nums2.begin();
        while(iter_nums1 != nums1.end() && iter_nums2 != nums2.end())
        {
            if(*iter_nums1 < *iter_nums2)
            {
                temp.emplace_back(*iter_nums1);
                iter_nums1++;
            }
            else
            {
                temp.emplace_back(*iter_nums2);
                iter_nums2++;
            }
        }
        while(iter_nums1 != nums1.end())
        {
             temp.emplace_back(*iter_nums1);
                iter_nums1++;
        }
        
        while(iter_nums2 != nums2.end())
        {
            temp.emplace_back(*iter_nums2);
            iter_nums2++;
        }
        
        return temp;
    }
};
