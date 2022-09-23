---
title: "Nuthornville"
type: location
campaign: sumonho
setting: Scalinea
aliases:
  - "Nuthornberg"
  - "Nuthornburg"
created: 2022-07-24 09:07:58
location:
  name: "Nuthornville"
  locationtype: "Settlement"
  region: "Aimesland"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/aimesland
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/settlement/nuthornville
---
# Nuthornville

Campaign:: [[30-39 TTRPG/34 Campaigns/34.01 SumonHo/34.01 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs::[[Timothy Werthy]]

## Description

- North of the [[Great Forest]]


## Locations in Nuthornville
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/scalinea/location
WHERE location.settlement = "Nuthornville"
```

## People in Nuthornville

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Nuthornville]]
  and person.status = "alive"
SORT file.name asc
```



