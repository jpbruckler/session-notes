---
title: "Clinic of Healing"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 07:54:17
location:
  name: "Clinic of Healing"
  locationtype: "Temple"
  region: "Aimesland"
  settlement: "Fowlerville"
tags:
  - ttrpg/setting/scalinea/location/region/aimesland
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/temple/clinic-of-healing
---
# Clinic of Healing

Campaign:: [[30-39 TTRPG/34 Campaigns/34.01 SumonHo/34.01 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
NotableNPCs:: [[Lesdyl]]
Quests:: [[Silhouette Murder]]

## Description

- The primary hospital in [[Fowlerville]].
- [[Danger Inc.]] was pointed here to talk to [[Lesdyl]] to get more information into the death of [[LM]].

They learned from [[Lesdyl]] that [[LM]] was stabbed twice in the gut and had an arrow in his shoulder. [[Mary]], his wife, had two arrows including one right at her heart. In discussion, none of the arrows were very deep nor did they show much signs of bleeding. She also had a bruise on her face like she was punched. After further discussion, [[Lesdyl]] remembered [[Mary]] also had some minor bruising in the neck area. [[LM]] was filthy on his back, but [[Mary]] didn’t have much in the way of mud or dirt.


## People in Clinic of Healing

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Clinic of Healing]]
  and person.status = "alive"
SORT file.name asc
```






