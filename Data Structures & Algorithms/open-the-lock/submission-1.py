class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        visited = set()
        configs = ["0000"]
        turns = 0

        while configs:
            turns += 1
            next_configs = []
            for cur in configs:
                config = list(cur)
                for i in range(4):
                    num = int(config[i])
                    numup = (num + 1) % 10
                    numdown = (num - 1) % 10

                    configup = config.copy()
                    configup[i] = str(numup)
                    configup = ''.join(configup)

                    configdown = config.copy()
                    configdown[i] = str(numdown)
                    configdown = ''.join(configdown)

                    for candidate in (configup, configdown):
                        if candidate == target:
                            return turns
                        if candidate not in dead and candidate not in visited:
                            visited.add(candidate)
                            next_configs.append(candidate)
            configs = next_configs
        return -1