---
title: "Fortress Down Under"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 08:33:56
location:
  name: "Fortress Down Under"
  locationtype: "Dungeon"
  region: "Aimesland"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/aimesland
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/dungeon/fortress-down-under
---
# Fortress Down Under

Campaign:: [[30-39 TTRPG/34 Campaigns/34.01 SumonHo/34.01 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs::[[Grenl]], [[Yusdrayl]], [[Belak]]

## Description

- Contains a shrine to [[Ashardalon]] in the lower levels
- Occupied by the [[Kobold Body]] (led by [[Yusdrayl|Queen Yusdrayl]]) and the [[Durbuluk Tribe]] (led by Matron [[Grenl]]) in the upper levels, where there's a bit of an uneasy truce between the 2 factions.
- [[Belak|Belak The Outcast]] made his home in the lower levels of the fortress, and was trying to corrupt a great tree
- The resting place of [[Vivian Powell|Vivian Powell's]] children, once [[Belak]] was done with them.


## People in Fortress Down Under

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Fortress Down Under]]
  and person.status = "alive"
SORT file.name asc
```



