#include "p4fuzzclib.h"

std::vector<std::string> tokenize(std::string *str, char sep)
{
	std::vector<std::string> ret;
	std::istringstream stm(*str);
	std::string token;
	while(std::getline(stm, token, sep)){
	    ret.push_back(token);
	}
	return ret;
}

int _common_tokens_distance(std::string *s1, std::string *s2){
    int init_dist, dist;
    std::vector<std::string> s1_tokens = tokenize(s1, ' ');
    std::vector<std::string> s2_tokens = tokenize(s2, ' ');
    init_dist = dist = s1_tokens.size() + s2_tokens.size();
    for(std::vector<std::string>::iterator i = s1_tokens.begin(); i != s1_tokens.end(); i++){
        for(std::vector<std::string>::iterator j = s2_tokens.begin(); j != s2_tokens.end(); ){
            if(j->compare(*i) == 0){
                dist -= 2;
                j = s2_tokens.erase(j);
                break;
            } else {
                j++;
            }
        }
    }
    return ceil(((float)dist / (float)init_dist) * 100);
}

int common_tokens_distance(std::string s1, std::string s2){
    return _common_tokens_distance(&s1, &s2);
}

std::vector< std::vector<int> > calc_distance_matrix(std::vector<std::string> data){
    int **dist = new int*[data.size()];
    for (size_t i = 0; i < data.size(); i++){
        dist[i] = new int[data.size()];
    }
    std::vector< std::vector<int> > result;
    for(std::vector<std::string>::iterator i = data.begin(); i != data.end(); i++){
        int i_index = i - data.begin();
        for(std::vector<std::string>::iterator j = data.begin() + i_index; j != data.end(); j++){
            int j_index = j - data.begin();    
            int distance = _common_tokens_distance(&*i, &*j);
            dist[i_index][j_index] = distance;
            dist[j_index][i_index] = distance;
        }
    }
    for(unsigned int i=0; i<data.size(); i++){
        std::vector<int> partial;
        for(unsigned int j=0; j<data.size(); j++){
            partial.push_back(dist[i][j]);
        }
        result.push_back(partial);
    }
    for (size_t i = data.size(); i > 0; ){
        delete[] dist[--i];
    }
    delete[] dist;
    return result;
}

std::vector<int> calc_max_distance_cluster(std::vector< std::vector<int> > dist, std::vector<int> cluster){
    int max = 0;
    int max_points[2] = {0, 0};
    for(std::vector<int>::iterator i = cluster.begin(); i != cluster.end(); i++){
        int i_index = i - cluster.begin();
        for(std::vector<int>::iterator j = cluster.begin() + i_index; j != cluster.end(); j++){
            int distance = dist[*i][*j];
            if(distance > max){
                max = distance;
                max_points[0] = *i;
                max_points[1] = *j;
            }
        }
    }
    std::vector<int> points;
    points.push_back(max_points[0]);
    points.push_back(max_points[1]);
    return points;
}
