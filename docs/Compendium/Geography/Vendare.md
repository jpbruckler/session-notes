---
title: Vendare
id: e40644fb-be99-4c67-8f39-1e93533d609b
created: 2022-10-22
tags:
  - ttrpg/location
  - ttrpg/setting/forgotten-realms/location/region/silver-marches
  - ttrpg/setting/forgotten-realms/location/settlement
---

# [[Vendare]]


!!! info
    - campaign:: [[32.01 DotMM]]
    - setting:: [[Forgotten Realms]]
    - type:: location, ttrpg
    - locationType:: settlement
    - location:: [[Silver Marches]]

## Description


## Locations in Vendare
```dataview
TABLE locationType AS Type from #ttrpg/setting/forgotten-realms/location
WHERE contains(location,[[Vendare]])
```

## People in Vendare

```dataview
TABLE type AS "Person Type", status AS Status, factions AS Factions FROM #ttrpg 
WHERE lastLocation = [[Vendare]]
SORT file.name asc
```

