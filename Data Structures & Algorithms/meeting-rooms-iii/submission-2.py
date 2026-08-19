class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        freeRooms = list(range(n))
        heapq.heapify(freeRooms)
        busyRooms = []  # [end_time, room_number]
        count = [0] * n

        for start, end in meetings:
            # free up any rooms that have finished by 'start'
            while busyRooms and busyRooms[0][0] <= start:
                _, room = heapq.heappop(busyRooms)
                heapq.heappush(freeRooms, room)

            if freeRooms:
                room = heapq.heappop(freeRooms)
                heapq.heappush(busyRooms, [end, room])
            else:
                busy_end, room = heapq.heappop(busyRooms)
                new_end = busy_end + (end - start)
                heapq.heappush(busyRooms, [new_end, room])

            count[room] += 1

        best = 0
        for i in range(1, n):
            if count[i] > count[best]:
                best = i
        return best