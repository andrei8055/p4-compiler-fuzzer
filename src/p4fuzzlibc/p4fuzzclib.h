#include <string>
#include <vector>
#include <sstream>
#include <cmath>

int common_tokens_distance(std::string s1, std::string s2);
std::vector< std::vector<int> > calc_distance_matrix(std::vector<std::string> data);
std::vector<int> calc_max_distance_cluster(std::vector< std::vector<int> > dist, std::vector<int> cluster);
