---
title: "Waycombe"
type: location
campaign: dotmm
setting: Forgotten Realms
created: 2022-07-24 09:30:13
location:
  name: "Waycombe"
  locationtype: "Settlement"
  region: "Savage Frontier"
  settlement:
tags:
  - ttrpg/setting/forgotten-realms/location/region/savage-frontier
  - ttrpg/campaign/dotmm
  - ttrpg/setting/forgotten-realms/location/settlement/waycombe
---
# Waycombe

Campaign:: [[30-39 TTRPG/34 Campaigns/34.02 DotMM/34.02 DotMM|34.02 DotMM]]
Setting:: [[Forgotten Realms]]
GovernmentType::
NotableNPCs::

## Description



## Locations in Waycombe
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/forgotten-realms/location
WHERE location.settlement = "Waycombe"
```

## People in Waycombe

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Waycombe]]
  and person.status = "alive"
SORT file.name asc
```



