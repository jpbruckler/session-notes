---
title: "Thornburg"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 09:23:50
location:
  name: "Thornburg"
  locationtype: "Settlement"
  region: "Aimesland"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/aimesland
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/settlement/thornburg
---
# Thornburg

Campaign:: [[30-39 TTRPG/34 Campaigns/34.01 SumonHo/34.01 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs:: [[Silvia Volgo]]

## Description



## Locations in Thornburg
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/scalinea/location
WHERE location.settlement = "Thornburg"
```

## People in Thornburg

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Thornburg]]
  and person.status = "alive"
SORT file.name asc
```



