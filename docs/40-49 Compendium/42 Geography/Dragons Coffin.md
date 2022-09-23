---
title: "Dragons Coffin"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 07:19:30
location:
  name: "Dragons Coffin"
  locationtype: "Fort"
  region: "Aimesland"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/aimesland
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/fort/dragons-coffin
---
# Dragons Coffin

Campaign:: [[Sumon-Ho]]
Setting:: [[Scalinea]]


GovernmentType::
NotableNPCs::[[Julo Aimes]], [[Oigah]], [[Drawr]]


## Description

Dragon’s Coffin is a fortress 4 miles from the outskirts of [[Aimesville]]. Dragon’s Coffin was the keep of [[Julo Aimes]] at the time of the [[Northern Invasion]]. [[Drawr]] placed the head of [[Oigah]] on a stake on the road to the gate. This was the location where the [[Northern Invasion]] ended as an organized army.



## People in Dragons Coffin

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Dragons Coffin]]
  and person.status = "alive"
SORT file.name asc
```

