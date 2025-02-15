from typing import List
def query_results(limit: int, queries: List[List[int]]) -> List[int]:
    unique_colors = [0]*len(queries)
    current_index = 0
    is_unique = [False]*(limit+2)

    for ball in queries:
        if is_unique[ball[1]]:
            unique_colors[current_index] = unique_colors[current_index-1]
        else:
            unique_colors[current_index] = unique_colors[current_index - 1]+1
            is_unique[ball[1]] = True
        current_index += 1
    return unique_colors

def main():
    print(query_results(limit=4, queries=[[1,4],[2,5],[1,3],[3,4]]))
    # print(query_results(limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]))


main()
