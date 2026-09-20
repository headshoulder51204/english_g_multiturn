"""Master Scenario Builder for TalkieTown US.
Assembles all 4 tiers (40 episodes, 180 total multi-turns) into scenarios.js.
"""
import json
from scenarios_tier1 import t1
from scenarios_tier2 import t2
from scenarios_tier3 import t3
from scenarios_tier4 import t4

full_data = {
    "tier1": t1,
    "tier2": t2,
    "tier3": t3,
    "tier4": t4
}

# Write scenarios.js
js_content = "window.SCENARIOS = " + json.dumps(full_data, ensure_ascii=False, indent=2) + ";\n"
with open("scenarios.js", "w", encoding="utf-8") as f:
    f.write(js_content)

total_eps = len(t1) + len(t2) + len(t3) + len(t4)
total_turns = sum(len(e['turns']) for t in [t1, t2, t3, t4] for e in t)

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("SUCCESS: Generated scenarios.js with:")
print(f"  - Tier 1 (Ages 6-8):   {len(t1)} episodes, {sum(len(e['turns']) for e in t1)} turns (3 turns/ep)")
print(f"  - Tier 2 (Ages 9-10):  {len(t2)} episodes, {sum(len(e['turns']) for e in t2)} turns (4 turns/ep)")
print(f"  - Tier 3 (Ages 11-13): {len(t3)} episodes, {sum(len(e['turns']) for e in t3)} turns (5 turns/ep)")
print(f"  - Tier 4 (Ages 14-16): {len(t4)} episodes, {sum(len(e['turns']) for e in t4)} turns (6 turns/ep)")
print(f"  - Total: {total_eps} episodes, {total_turns} turns")

