class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_sort = sorted(seats)          
        students_sort = sorted(students)    
        count_min = 0
        
        for i in range(len(seats)):
            if seats_sort[i] != students_sort[i]:
                count_min += abs(seats_sort[i] - students_sort[i])
            
        return count_min
    
    
"""
Another Approach
----------------

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()          
        students.sort()    
        return sum(abs(seat - student) for seat, student in zip(seats, students))

* Time complexity: O(n log n)
"""