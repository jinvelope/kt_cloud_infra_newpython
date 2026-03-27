# Step16_RegExp3.py

import re

logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]

lists = []
for log in logs:
    m_log = re.search(r"WARN|ERROR", log)
    if m_log:
        lists.append(log)

for list in lists:
    print(list)