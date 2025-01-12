#include <iostream>
#include "Solution.hpp"
using namespace std;

struct testcase { string boxes; vector<int> output; };

class UnitTest {
private:
    vector<testcase> testcases;
    Solution obj;
public:
    UnitTest() {
        testcases = {{"110", {1,1,3}}, {"001011", {11,8,5,4,3,4}}};
    }

    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            vector<int> result = obj.minOperations(testcases[i].boxes);
            bool match = true;
            for(int j = 0; j < result.size(); ++j) {
                if(result[j] != testcases[i].output[j]) { match = false; break; }
            }
            
            cout << "TestCase " << i+1 << ": " << (match ? "passed":"failed") << endl;
        }
    }
};

int main() {
    UnitTest test;
    test.test();
}