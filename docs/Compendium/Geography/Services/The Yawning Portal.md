---
title: "The Yawning Portal"
type: location
campaign: dotmm
setting: Forgotten Realms
created: 2022-07-31 05:45:31
location:
  name: "The Yawning Portal"
  locationtype: "Inn"
  region: "Sword Coast"
  settlement: Waterdeep
tags:
  - ttrpg/setting/forgotten-realms/location/region/sword-coast
  - ttrpg/campaign/dotmm
  - ttrpg/setting/forgotten-realms/location/inn/the-yawning-portal
---
# The Yawning Portal

Campaign:: [[30-39 TTRPG/34 Campaigns/34.02 DotMM/34.02 DotMM|34.02 DotMM]]
Setting:: [[Forgotten Realms]]
GovernmentType::
NotableNPCs::

## Description

The Yawning Portal, a famous inn and tavern located near the eastern slope of [[Mount Waterdeep]], derives its name from a 40-foot-diameter well that descends into the first level of Undermountain. Located in the center of the taproom, the well was once the outer shell of Halaster’s mighty tower, which was demolished long ago. Its sheer walls are made of old mortared stones. Next to this gaping orifice hangs a winch with a simple rope-and-pulley mechanism that Durnan, the proprietor, uses to lower adventurers down the shaft and (sometimes) pull them up again. Durnan controls the winch himself and will transport only one adventurer at a time.

## People in The Yawning Portal

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[The Yawning Portal]]
  and person.status = "alive"
SORT file.name asc
```



