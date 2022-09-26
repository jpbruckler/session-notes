---
title: "Phandalin"
type: location
campaign: aotr
setting: Forgotten Realms
created: 2022-07-24 09:11:27
location:
  name: "Phandalin"
  locationtype: "Settlement"
  region: "Sword Coast North"
  settlement: 
tags:
  - ttrpg/setting/forgotten-realms/location/region/sword-coast-north
  - ttrpg/campaign/aotr
  - ttrpg/setting/forgotten-realms/location/settlement/phandalin
---
# Phandalin

Campaign:: [[30-39 TTRPG/34 Campaigns/34.03 AotR/34.03 AotR|34.03 AotR]]
Setting:: [[Forgotten Realms]]
GovernmentType::
NotableNPCs::

## Description



## Locations in Phandalin
```dataview
TABLE location.locationtype AS Type from #ttrpg/setting/forgotten-realms/location
WHERE location.settlement = "Phandalin"
```

## People in Phandalin

```dataview
TABLE type AS "Person Type", factions AS Factions FROM #ttrpg 
WHERE LastLocation = [[Phandalin]]
  and person.status = "alive"
SORT file.name asc
```




# Phandalin

```leaflet
id: phandalin-town
image:
  - [[phandalin-player.jpg]]
  - [[phandalin-dm.jpg]]
bounds: [[0,0],[821.42,1178.57]]
height: 500px
width: 850px
unit: ft
# lat/long in percent doesn’t center
# does ist not respect scale or bounds?
# would be easier if this was a coordinate in "bounds" range,
# as the "final" coordinates will be.
coordinates: [[Barthen's Provisions]]
minZoom: -2
maxZoom: 2
defaultZoom: 1
zoomTag: nearby
marker: shoppe,396.1962921770559,403.72345836348046,Lionshield Coster,,-2,10
```


X 1178.57142857143  
Y 821.428571428571

Town Council 
- [[Sildar Hallwinter]]
- [[Halia Thornton]]

## Locations Around Town

### Alderleaf Farm

### [[Barthen's Provisions]]

### Barthen's Home

### Edermath Orchard

### [[Halia's Home]]

### Harbin Wester's House

### [[300-399 Gaming/300 DND 5E/40-49 Compendium/42 Geography/300.42.04 Services/Lionshield Coster|Lionshield Coster]]

### Linene's House

### Phandalin Miner's Exchange

### Shrine of Luck

### Sister Garael's Home

### Stonehill Inn

### The Sleeping Giant

### Townmaster's Hall

### [[Tresendar Manor]]

### Woodworker

