---
title: "Drinverth"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 08:15:47
location:
  name: "Drinverth"
  locationtype: "Settlement"
  region: "Underdark"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/underdark
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/settlement/drinverth
---
# Drinverth

Campaign:: [[30-39 TTRPG/32 Campaigns/32.02 SumonHo/32.02 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs::

## Description

From the book [[Perilous Realms]]:

"...a diverse subterranean city called Drinverth ruled by a druegar king, and a portal that leads to a long forgotten region similar to this land with a large corrupted port city called [[Waterdeep]].)"

## Locations in Drinverth
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/scalinea/location
WHERE location.settlement = "Drinverth"
```

## People in Drinverth

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Drinverth]]
  and person.status = "alive"
SORT file.name asc
```



