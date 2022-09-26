---
title: "Blissville"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 07:46:20
location:
  name: "Blissville"
  locationtype: "Settlement"
  region: "Aimesland"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/aimesland
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/settlement/blissville
---
# Blissville

Campaign:: [[30-39 TTRPG/34 Campaigns/34.01 SumonHo/34.01 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs::

## Description

Situated near the [[Great Forest]] in what is now known as the [[Ravaged Lands]].


## Locations in Blissville
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/scalinea/location
WHERE location.settlement = "Blissville"
```

## People in Blissville

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Blissville]]
  and person.status = "alive"
SORT file.name asc
```



