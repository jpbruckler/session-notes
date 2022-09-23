---
title: "Aimesville"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 03:21:30
location:
  name: "Aimesville"
  locationtype: "Settlement"
  region: "Aimesland"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/aimesland
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/settlement/aimesville
---
# Aimesville

Campaign:: [[Sumon-Ho]]
Setting:: [[Scalinea]]


GovernmentType::
NotableNPCs::


## Locations in Aimesville
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/scalinea/location
WHERE location.settlement = "Aimesville"
```

## People in Aimesville

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Aimesville]]
  and person.status = "alive"
SORT file.name asc
```

