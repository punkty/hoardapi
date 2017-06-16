# Documentation

### Getting Started

Lets make a request to the hoard api. Maybe we are looking to fill a blacksmith's shop or an item that will be in the chest at the end of the dungeon. Regardless, we want a weapon and we'll be selecting the first one in our weapon resources.

The request made will be as follows:

```http
http://hoardapi.com/api/weapon/1
```
The response we get back:

```json
{
	"id": 1,
	"name": "Rusty Dagger",
	"price": "1 gp",
	"damage": "1d4",
	"range": "20/60",
	"type": "Simple Melee",
	"weight": "1 lb",
	"stealth": "",
	"description": "A common dagger that has been exposed to the elements",
	"magical": false,
	"magical_properties": [],
	"stats": [
		{
			"charisma": 0,
			"constitution": 0,
			"defense": 0,
			"dexterity": 0,
			"intelligence": 0,
			"luck": 0,
			"perception": 0,
			"strength": 0,
			"wisdom": 0
		}
	]
}
```

### Authentication



# Resources

### Root

The base URL for accessing hoard API is:

```http
http://hoardapi.com/api/
```

**Example response:**

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "armor": "http://localhost:8000/armor/",
    "magicalproperty": "http://localhost:8000/magicalproperty/",
    "mount": "http://localhost:8000/mount/",
    "potion": "http://localhost:8000/potion/",
    "tool": "http://localhost:8000/tool/",
    "trinket": "http://localhost:8000/trinket/",
    "weapon": "http://localhost:8000/weapon/"
}
```

**Attributes:**

- ```armor```
-- The URL root for armor resources
- ```magicalproperty``` 
-- The URL root for magical property resources
- ```mount```
-- The URL root for mount resources
- ```potion```
-- The URL root for potion resources
- ```tool```
-- The URL root for tool resources
- ```trinket```
-- The URL root for trinket resources
- ```weapon```
-- The URL root for weapon resources