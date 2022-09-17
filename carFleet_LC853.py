class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #solution by sorting
        # if not position or not speed:
        #     return 0
        # cars = sorted(zip(position, speed))
        # times = [(target - p) / s for p, s in cars]
        # result = 0
        # while len(times) > 1:
        #     lead = times.pop()
        #     if lead < times[-1]:
        #         result += 1
        #     else:
        #         times[-1] = lead
        # return result + bool(times)

        #solution by stack
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)