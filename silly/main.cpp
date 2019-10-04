//g++ -std=c++14 -g -o oct3 main.cpp -l gtest -l pthread
#define gtest 0

#if gtest
#include <gtest/gtest.h>
#endif

#include <iostream>
#include <iomanip>
#include <vector>
#include <stdint.h>
#include <cmath>

using namespace std;

template<class internal_int = uint64_t, class arg_int = uint32_t>
class online_normal_dist_estimator {
  internal_int sum_y2 = 0;
  internal_int sum_y = 0;
  internal_int N = 0;
public:
  void update(arg_int y) {
    ++N;
    sum_y += y;
    internal_int iy = y;
    sum_y2 += iy * iy;
  }
  void get_estimators( double& mean, double& var) {
    mean = (double)sum_y / N;
    var = (double)sum_y2/(N-1) -  mean * mean * N / (N-1);
  }
};

void stdin_main() {
  double m, s2;
  online_normal_dist_estimator<> onde;
  uint32_t N, tmp;
  cin >> N;
  for (unsigned i = 0; i < N; ++i) {
    cin >> tmp;
    onde.update(tmp);
  }
  onde.get_estimators(m, s2);
  cout << setprecision(9) << m << endl;
  cout << setprecision(9) << s2 << endl;
}

bool double_equal(double lhs, double rhs, double eps) {
  if (lhs == rhs) return true;
  double numer = fabs(lhs - rhs);
  double denom = (fabs(lhs) + fabs(rhs))*.5;
  return (numer / denom) < eps;
}

#if gtest
TEST(simple, one) {
  vector<uint32_t> tdata{ 1, 2, 3, 4};
  online_normal_dist_estimator<> onde;

  for (unsigned i = 0; i < tdata.size(); ++i) {
    onde.update(tdata.at(i));
  }
  double m, s2;
  onde.get_estimators(m, s2);

  EXPECT_TRUE(double_equal(m, 2.5, .0001));
  EXPECT_TRUE(double_equal(s2, 1.666667, .001));
}
#endif

int main(int argc, char **argv) {
#if gtest
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
#else
  stdin_main();
  return 0;
#endif
}
