import json
from pathlib import Path
base=Path(__file__).resolve().parents[1]
for file in sorted((base/'cases').glob('*.json')):
 c=json.loads(file.read_text(encoding='utf8'));ids={s['id'] for s in c['suspects']};clues={x['id'] for x in c['clues']};hot={h['clue'] for h in c['hotspots'] if h['clue']};ev=set(c['solution']['evidenceClues'])
 assert c['solution']['culprit'] in ids,(file,'missing culprit')
 assert 2<=len(ev)<=3 and ev<=clues and ev<=hot,(file,'evidence unavailable')
 assert len(c['hotspots'])>=len(ev),(file,'hotspots missing')
 assert all(h.get('clue') in clues for h in c['hotspots']),(file,'empty hotspot')
 assert len(hot)==len(c['hotspots']),(file,'duplicate clue hotspots')
 assert len({x['id'] for x in c['hotspots']})==len(c['hotspots'])
 assert sum(s['suspect']==c['solution']['culprit'] for s in c['statements'])==1
 for s in c['statements']: assert set(s['contradictedBy'])<=hot
 for h in c['hotspots']: assert h['room'] in c['rooms']
 print(file.name,'OK')
print('All cases passed structural validation. Narrative uniqueness requires human review.')
