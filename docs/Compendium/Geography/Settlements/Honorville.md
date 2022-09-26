---
title: "Honorville"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 08:44:01
location:
  name: "Honorville"
  locationtype: "Settlement"
  region: "Aimesland"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/aimesland
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/settlement/honorville
---
# Honorville

Campaign:: [[30-39 TTRPG/34 Campaigns/34.01 SumonHo/34.01 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs::

## Description



## Locations in Honorville
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/scalinea/location
WHERE location.settlement = "Honorville"
```

## People in Honorville

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Honorville]]
  and person.status = "alive"
SORT file.name asc
```



