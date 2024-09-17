class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_start = set()
        city_destintion = set()

        for i, d in paths:
            city_start.add(i)
            city_destintion.add(d)

        return list(city_destintion - city_start)[0]
