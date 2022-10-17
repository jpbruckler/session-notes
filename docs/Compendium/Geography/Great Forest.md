---
title: "Great Forest"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 08:39:45
location:
  name: "Great Forest"
  locationtype: "Forest"
  region: "Ravaged Lands"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/ravaged-lands
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/forest/great-forest
---
# Great Forest

Campaign:: [[30-39 TTRPG/32 Campaigns/32.02 SumonHo/32.02 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs::

## Description



## People in Great Forest

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Great Forest]]
  and person.status = "alive"
SORT file.name asc
```



