#include "cpp/functions.h"

std::vector<int> plus_two_list(const std::vector<int>& v)
{
    std::vector<int> result;
    for (auto i: v) result.push_back(i + 2);

    return result;
}

