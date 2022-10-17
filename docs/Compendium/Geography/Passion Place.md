---
title: "Passion Place"
type: location
campaign: sumonho
setting: Scalinea
aliases:
  - "Lower Ecstasy"
created: 2022-07-24 08:55:53
location:
  name: "Passion Place"
  locationtype: "Settlement"
  region: "Ravaged Lands"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/ravaged-lands
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/settlement/passion-place
---
# Passion Place

Campaign:: [[30-39 TTRPG/32 Campaigns/32.02 SumonHo/32.02 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs::[[Olgann]]

## Description

Passphrase: "I kneel with the Master"

[[Averos]] said over 3 messages: 

>[!quote] Averos
>After many, many hours of research the only reference to the Passion Place was an area bandit lieutenant’s letter written 15 years ago. According to the letter, it’s Master is a very powerful entity; a [[Battle Mage]], a warrior spell caster. The letter references a password (opps, passphrase) to allow passage by the place’s guards. Since the passphrase was widely distributed, it was never changed according to the letter. The passphrase is ‘I kneel with the Master.’ That’s all the pertinent information.



## Locations in Passion Place
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/scalinea/location
WHERE location.settlement = "Passion Place"
```

## People in Passion Place

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Passion Place]]
  and person.status = "alive"
SORT file.name asc
```



