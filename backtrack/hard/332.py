from typing import List, Set, Tuple
import copy


class Solution:
    def __init__(self) -> None:
        self.itinerary = None
        self.tickets: List[Tuple[str, str]] = []

    def _search(self, used: List[bool], current: List[str], count: int):
        if self.itinerary is not None:
            return

        if count == len(self.tickets):
            if self.itinerary is None:
                self.itinerary = current
            return

        source = current[-1]
        for idx, ticket in enumerate(self.tickets):
            if ticket[0] == source and not used[idx]:
                used[idx] = True
                current_copy = copy.copy(current)
                current_copy.append(ticket[1])
                self._search(used, current_copy, count + 1)
                if self.itinerary is not None:
                    return
                used[idx] = False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.itinerary = None
        self.tickets = list(sorted(map(lambda x: tuple(x), tickets)))
        self._search([False for _ in self.tickets], ['JFK'], 0)
        return self.itinerary


solution = Solution()
print(
    solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"],
                            ["LHR", "SFO"]]))
print(
    solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
                            ["ATL", "JFK"], ["ATL", "SFO"]]))
print(
    solution.findItinerary([["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"],
                            ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"],
                            ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"],
                            ["JFK", "TIA"]]))
