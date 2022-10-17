---
title: "Vendare"
type: location
campaign: dotmm
setting: Forgotten Realms
created: 2022-07-24 09:29:08
location:
  name: "Vendare"
  locationtype: "Settlement"
  region: "Savage Frontier"
  settlement: 
tags:
  - ttrpg/setting/forgotten-realms/location/region/savage-frontier
  - ttrpg/campaign/dotmm
  - ttrpg/setting/forgotten-realms/location/settlement/vendare
---
# Vendare

Campaign:: [[32.01 DotMM]]
Setting:: [[Forgotten Realms]]
GovernmentType::
NotableNPCs::

## Description



## Locations in Vendare
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/forgotten-realms/location
WHERE location.settlement = "Vendare"
```

## People in Vendare

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Vendare]]
  and person.status = "alive"
SORT file.name asc
```



