---
title: "Rainsburg"
type: location
campaign: sumonho
setting: Scalinea
created: 2022-07-24 09:13:17
location:
  name: "Rainsburg"
  locationtype: "Settlement"
  region: "Aimesland"
  settlement: 
tags:
  - ttrpg/setting/scalinea/location/region/aimesland
  - ttrpg/campaign/sumonho
  - ttrpg/setting/scalinea/location/settlement/rainsburg
---
# Rainsburg

Campaign:: [[30-39 TTRPG/32 Campaigns/32.02 SumonHo/32.02 SumonHo|34.01 SumonHo]]
Setting:: [[Scalinea]]
GovernmentType::
NotableNPCs::[[Olseris]], [[Eljas]]

## Description

Hometown of both [[Eljas]] and [[Olseris]]

12 miles northeast of [[Fowlerville]] across the Rinder River. It is a small town in the foothills leading up to the [[Barrier Mountains]], in a region called kosketus taivas. Many of the inhabitants farm potatoes, wheat, and barley.

The village proper is made up of 8 buildings. Four businesses serve the resident’s needs; a general store, a blacksmith, a tavern, and a butcher’s shop. Two businesses serve primarily other businesses; the mill (wind mill) and the 4-stall stables. Also, two buildings meet the religious needs; the Kalevala temple and the disease-ward shrine dedicated to Kiputytto.

The Kalevala temple is a sturdy, defensible building with 3 levels; 2 indoors and 1 outdoors. The Kalevala temple is ministered primarily by the churches of [[Rondos]] (1 priestess and 1 deacon) and [[Ilmatar]] (1 cleric and 1 deacon), with a resident priest of [[Yipen]] and a visiting cleric of Aino. The Templars and faithful guards also perform lite patrols of the town. This includes 2 [[Rondos]] Templars, 2 Aino Templars, 1 [[Ilmatar]] Templar, 4 Rondos guards, 2 [[Yipen]] guards, and 1 [[Ilmatar]] guard. The Aino cleric and templars have been in Rainsburg intermittently over the last 2 years. 

- Entering the double doors with raised portcullis on the front (southern side) of the building, a visitor would walk up the stairs toward the main worship area. The main worship area has several 4x6 windows (with bars) that can be closed by releasing the rope. There are also 2 smaller worship rooms. There are a man-sized doors on both the east and west side of the building that open into a curved hallway to another metal door. Two trap doors on the 2nd floor lead to the open-aired 3rd floor, which has an attractive but functional 3.5 foot tall wall and a roof. This building is the location that the populace would run to in the event of an emergency.   

The shrine is a small 12x20 building with 2 rooms maintained by a local citizen. It represents an attempt to ward off citizen and crop diseases.


## Locations in Rainsburg
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/scalinea/location
WHERE location.settlement = "Rainsburg"
```

## People in Rainsburg

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Rainsburg]]
  and person.status = "alive"
SORT file.name asc
```



