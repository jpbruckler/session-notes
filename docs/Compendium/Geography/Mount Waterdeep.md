---
title: "Mount Waterdeep"
type: location
campaign: dotmm
setting: Forgotten Realms
created: 2022-07-31 05:47:28
location:
  name: "Mount Waterdeep"
  locationtype: "Mountain"
  region: "Sword Coast"
  settlement: Waterdeep
tags:
  - ttrpg/setting/forgotten-realms/location/region/sword-coast
  - ttrpg/campaign/dotmm
  - ttrpg/setting/forgotten-realms/location/mountain/mount-waterdeep
---
# [[Mount Waterdeep]]

Campaign:: [[32.01 DotMM]]
Setting:: [[Forgotten Realms]]
GovernmentType::
NotableNPCs::

## Description



## People in Mount Waterdeep

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Mount Waterdeep]]
  and person.status = "alive"
SORT file.name asc
```



