class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_vel = [(position[i], speed[i]) for i in range(len(position))]

        pos_vel = sorted(pos_vel, key=lambda x:-x[0] )

        for i in range(len(pos_vel)):
            time = (target - pos_vel[i][0]) / pos_vel[i][1]
            pos_vel[i] = (pos_vel[i][0], pos_vel[i][1], time)

        stack = [pos_vel[0]]
        for i in range(len(pos_vel)):
            if pos_vel[i][2] > stack[-1][2]:
                stack.append(pos_vel[i])

        return len(stack)