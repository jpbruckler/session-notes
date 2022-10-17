---
title: "Halia's Home"
type: location
campaign: aotr
setting: Forgotten Realms
created: 2022-07-24 08:41:08
location:
  name: "Halia's Home"
  locationtype: "Home"
  region: "Sword Coast North"
  settlement: "Phandalin"
tags:
  - ttrpg/setting/forgotten-realms/location/region/sword-coast-north
  - ttrpg/campaign/aotr
  - ttrpg/setting/forgotten-realms/location/home/halias-home
---
# Halia's Home

Campaign:: [[32.00 AotR]]
Setting:: [[Forgotten Realms]]
GovernmentType::
NotableNPCs::

## Description



## People in Halia's Home

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Halia's Home]]
  and person.status = "alive"
SORT file.name asc
```



