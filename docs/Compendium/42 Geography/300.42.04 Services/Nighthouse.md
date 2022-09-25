---
title: "Nighthouse"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 07:48:15
location:
  name: "Nighthouse"
  locationtype: "Temple"
  region: "Ravaged Lands"
  settlement: "Blissville"
tags:
  - ttrpg/setting/scalinea/location/region/ravaged-lands
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/temple/nighthouse
---
# Nighthouse

Campaign:: [[30-39 TTRPG/34 Campaigns/34.01 SumonHo/34.01 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs::

## Description

Before and during the [[Northern Invasion]], [[Gwyn Hovey|Gwyn]] was a cleric of [[Sutamo]] stationed in the Nighthouse in [[Blissville]] (it’s near the [[Great Forest]] in what is now the [[Ravaged Lands]]). [[Blissville]] was one of the 11 or 13 City-states. The Nighthouse was the seat of the religious order, housed the Bishop to the [[The Darkhouse|Church of Sutamo]], and received the 4 other ‘high priest’ Head of Households from the other churches dedicated to [[Sutamo]]. 

Members of the Nighthouse worked to support the Church, its parishioners, and the local community during the siege. After the eastern wall was breached, the city was pillaged in the day by orges, bugbears, orcs, and goblins. Throughout the night, wights, wraiths, and specters sought out the living, and eventually the city of [[Blissville]] was overrun.

## People in Nighthouse

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Nighthouse]]
  and person.status = "alive"
SORT file.name asc
```



