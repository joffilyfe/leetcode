from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        table = dict(paths)

        # for path in paths:
        #     if table.get(path[0]) is None:
        #         table[path[0]] = 1
        #     else:
        #         table[path[0]] += 1

        #     if table.get(path[1]) is None:
        #         table[path[1]] = 0
        #     else:
        #         table[path[1]] += 1

        # return [city for city, visits in table.items() if visits == 0][0]

        for origin, destination in paths:
            if table.get(destination) is None:
                return destination


print(Solution().destCity(paths=[["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]))

