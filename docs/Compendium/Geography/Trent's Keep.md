---
title: "Trent's Keep"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 09:26:34
location:
  name: "Trent's Keep"
  locationtype: "Fort"
  region: "Ravaged Lands"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/ravaged-lands
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/fort/trent's-keep
---
# Trent's Keep

Campaign:: [[30-39 TTRPG/32 Campaigns/32.02 SumonHo/32.02 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs::

## Description

Hundreds of years ago, Trent’s Keep was established by [[Trent Archer]], a ranger of much renown. It was the headquarters and training grounds for the [[Archers]], a collection of druids, rangers, and others who provided advice to the civilized realms and helped to fight evil that made its way into the land. By the time of the [[Northern Invasion]], the Archers had limited influence or interest in the institutions of man. They have become reclusive and stuck to their books. As the [[Northern Invasion]] reached their keep, they joined the battle. The last of their kind were lost in the early battles or abandoned their place as Archers.

Today, Trent’s Keep is the home of the “[[Sage of Life and Death]].” The Sage of Life and Death is sought by those willing to risk the trip for the information they need. His henchmen can be found traveling throughout the Southern Lands.

## People in Trent's Keep

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Trent's Keep]]
  and person.status = "alive"
SORT file.name asc
```



