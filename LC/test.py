from collections import defaultdict, deque
from typing import List


def alertNames(keyName: List[str], keyTime: List[str]) -> List[str]:
    name_to_time = defaultdict(list)
    for name, hour_minute in zip(keyName, keyTime):
        hour, minute = map(int, hour_minute.split(':'))
        time = hour * 60 + minute
        name_to_time[name].append(time)
    names = []
    for name, time_list in name_to_time.items():
        time_list.sort()
        dq = deque()
        for time in time_list:
            dq.append(time)
            if dq[-1] - dq[0] > 60:
                dq.popleft()
            if len(dq) >= 3:
                names.append(name)
                break
    return sorted(names)


print(alertNames(["luis", "luis"], [
           "23:00", "01:00"]))
