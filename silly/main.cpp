//g++ -std=c++14 -g -o stub stub.cpp -l gtest -l pthread
#include <algorithm>
#include <assert.h>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <gtest/gtest.h>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdint.h>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

#include <cmath>
#include <gtest/gtest.h>

typedef bool (*get_uint_t)(uint32_t*);

void calc_sample_mean_smpl_var( get_uint_t get_uint, double& mean, double& smpl_var)
{
  uint32_t y, n;
  uint64_t smy2=0, smy=0;
  if (!get_uint(&n)) {
    cerr << "can't read n" << endl;
    exit(1);
  }
  for (uint32_t i = 0; i < n; ++i) {
    if (!get_uint(&y)) {
      cerr << "can't read y" << endl;
      exit(1);
    }
    smy += y;
    smy2 += y*y;
  }
  mean = (double)smy / n;
  smpl_var = (double)smy2/(n-1) -  mean * mean * n / (n-1);
//  cerr << smpl_var << endl;
}

vector<uint32_t> data;
int data_offset = -1;

bool get_stdin(uint32_t* dat) {
  uint32_t tmp;
  cin >> tmp;
  *dat = tmp;
  return true;
}

void stdin_main() {
  double m, s2;
  calc_sample_mean_smpl_var(get_stdin, m, s2);
}

bool get_data(uint32_t* y) {
  if (data_offset < 0) {
    data_offset = 0;
    *y = data.size();
    return true;
  }
  if (data_offset >= data.size()) {
    return false;
  }
  *y = data.at(data_offset);
  ++data_offset;
  return true;
}

bool double_equal(double lhs, double rhs, double eps) {
  if (lhs == rhs) return true;
  double numer = fabs(lhs - rhs);
  double denom = (fabs(lhs) + fabs(rhs))*.5;
  return (numer / denom) < eps;
}

TEST(simple, one) {
  vector<uint32_t> tdata{ 1, 2, 3, 4};
  data.swap(tdata);
  double m, s2;
  calc_sample_mean_smpl_var(get_data, m, s2);
  EXPECT_TRUE(double_equal(m, 2.5, .0001));
  EXPECT_TRUE(double_equal(s2, 1.666667, .001));
}


int main(int argc, char **argv) {
  //testing::InitGoogleTest(&argc, argv);
  //return RUN_ALL_TESTS();
  stdin_main();
  return 0;
}
