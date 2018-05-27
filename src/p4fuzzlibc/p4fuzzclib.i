%module p4fuzzclib

%{
#define SWIG_FILE_WITH_INIT
#include "p4fuzzclib.h"
%}

%include "std_string.i"
%include "std_vector.i"

%template(vectors) std::vector<std::string>;
%template(vectori) std::vector<int>;
%template(vectorvi) std::vector< std::vector<int> >;

int common_tokens_distance(std::string s1, std::string s2);
std::vector< std::vector<int> > calc_distance_matrix(std::vector<std::string> data);
std::vector<int> calc_max_distance_cluster(std::vector< std::vector<int> > dist, std::vector<int> cluster);
