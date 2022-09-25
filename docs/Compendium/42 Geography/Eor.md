---
title: "Eor"
type: location
campaign: dotmm
setting: "Forgotten Realms"
aliases:
  - "County of Eor"
created: 2022-07-24 09:22:27
location:
  name: "Eor"
  locationtype: "Settlement"
  region: "Savage Frontier"
  settlement: 
tags:
  - ttrpg/setting/forgotten-realms/location/region/savage-frontier
  - ttrpg/campaign/dotmm
  - ttrpg/setting/forgotten-realms/location/settlement/eor
---
# Eor

Campaign:: [[30-39 TTRPG/34 Campaigns/34.02 DotMM/34.02 DotMM|34.02 DotMM]]
Setting:: [[Forgotten Realms]]
GovernmentType::
NotableNPCs::[[John Brunis]], [[Jorlon]]

## Description



## Locations in Eor
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/forgotten-realms/location
WHERE location.settlement = "Eor"
```

## People in Eor

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Eor]]
  and person.status = "alive"
SORT file.name asc
```



