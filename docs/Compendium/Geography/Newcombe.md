---
title: "Newcombe"
type: location
campaign: dotmm
setting: Forgotten Realms
created: 2022-07-24 09:04:04
location:
  name: "Newcombe"
  locationtype: "Settlement"
  region: "Northwest Faerun"
  settlement: 
tags:
  - ttrpg/setting/forgotten-realms/location/region/northwest-faerun
  - ttrpg/campaign/dotmm
  - ttrpg/setting/forgotten-realms/location/settlement/newcombe
---
# Newcombe

Campaign:: [[32.01 DotMM]]
Setting:: [[Forgotten Realms]]
GovernmentType::
NotableNPCs::[[Pluck]]

## Description



## Locations in Newcombe
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/forgotten-realms/location
WHERE location.settlement = "Newcombe"
```

## People in Newcombe

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Newcombe]]
  and person.status = "alive"
SORT file.name asc
```



