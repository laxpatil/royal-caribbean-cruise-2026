---
name: trip-planner
description: Interactive trip planner agent — asks user questions and generates a beautiful self-contained HTML trip planner page with countdown, tabs per destination, activity options, budget tracker, timeline, packing checklist, interactive canvas map, scroll animations, and glass morphism UI
---

# 🌍 Trip Planner Skill

Turn any AI agent into an **interactive trip planner wizard** that gathers user input and generates a stunning, self-contained HTML trip planner page.

## Overview

This skill transforms conversations into fully-featured trip planning documents. The agent:

1. **Asks conversational questions** in phases (trip basics → transport → destinations → budget → packing)
2. **Builds a JSON configuration** from user responses
3. **Calls the `generate.py` script** to render a complete HTML file
4. **Opens the page in the browser**
5. **Optionally pushes to git**

The resulting HTML is **fully self-contained** (no external dependencies except Google Fonts) with:
- Dark ocean/sky gradients matching trip type
- Animated particle backgrounds & wave effects
- Interactive canvas route map with animated vehicle
- Tab-based navigation per destination
- Countdown timer to departure
- Budget tracker per destination
- Activity comparison cards (free/premium/splurge badges)
- Interactive timeline with scroll animations
- Packing checklist with progress tracking
- All JavaScript inline with no build step required

---

## How It Works

### Phase 1: Conversational Gathering

Ask the user questions in this order, **one group at a time**:

#### Group A — Trip Basics
- "What's the name of your trip?" (e.g., "Caribbean Cruise 2026")
- "What's the trip type?" (cruise / road_trip / flight / backpacking / family_vacation)
- "What are the dates?" (start date YYYY-MM-DD → end date)
- "Where are you flying from?" (home city/airport)
- "Describe the trip in 1-2 words for a subtitle" (e.g., "Western Caribbean · 👶 Family")

#### Group B — Transport
- "Do you have flight details?" (airline, confirmation #, from→to)
- "Will you rent a car?" (company, dates, confirmation #)
- "Parking arrangements?" (airport, cost, lot name)
- "Hotel before/after?" (dates, name, cost)

#### Group C — Destinations
- "How many port stops / cities / destinations?"
- **For each destination, ask:**
  - Name & country (e.g., "Cozumel, Mexico 🇲🇽")
  - Date/day (e.g., "Day 2 — Apr 13")
  - Emoji representing the place (🏝️ or 🗼)
  - Color theme hex (e.g., "#34d399") or suggest one
  - 3–5 activities with:
    - Activity name (e.g., "Snorkel the Barrier Reef")
    - Price (e.g., "$45" or "Free")
    - Badge category: "free" | "premium" | "splurge"
    - 1–2 sentence description
    - Pros (list of 3–5 benefits)
    - Is it "recommended"? (true/false)
  - Recommended lunch spot (name + description)
  - Timeline items (time of day + activity + description)
  - Local tips (3–5 tips)
  - Packing items (5–8 items specific to this destination)

#### Group D — Budget
- Per destination budget total (e.g., "$150–200")
- Budget breakdown by category (activities, food, transport, shopping)
  - Each as % or $ amount

#### Group E — Packing & Special Needs
- Any special considerations? (toddler, elderly, accessibility, adventure focus)
- General packing items (not per-destination)
- Dietary restrictions or allergies to note?

#### Group F — Map Details
- Latitude & longitude for each destination (or ask agent to estimate based on city name)
- What's the primary mode of transport? (🚢 cruise / ✈️ flight / 🚗 road trip / 🎒 hiking/backpacking)

### Phase 2: Generate HTML

Once all inputs are collected:

1. **Build the JSON config** matching the schema (see `scripts/generate.py` docstring)
2. **Call the generate.py script:**
   ```bash
   python3 ~/.agents/skills/trip-planner/scripts/generate.py config.json ~/Desktop/my-trip-planner.html
   ```
3. **The script outputs** a complete, standalone HTML file
4. **Display success message** with the file path

### Phase 3: Output & Share

- **Open in browser** (auto-launch)
- **Print to PDF** for sharing or offline access
- **Push to GitHub** if user provides a repo URL

---

## Usage Example

```
User: "I want to plan a trip!"
Agent: "Great! Let's build your interactive trip planner. First, the basics:
  • What's the name of your trip? (e.g., 'Caribbean Cruise 2026')"

User: "Royal Caribbean Western Caribbean Cruise April 2026"

Agent: "Perfect! 🚢 Now, what's the trip type? 
  - cruise
  - road_trip
  - flight
  - backpacking
  - family_vacation"

User: "cruise"

Agent: "April cruise — fun! What dates exactly? (Start date YYYY-MM-DD)"
...
[After all questions are gathered]

Agent: "Excellent! I've collected all the info. Let me generate your HTML planner now..."

[Generates HTML and opens in browser]

Agent: "✅ Your trip planner is ready! Open it here: ~/Desktop/caribbean-cruise-2026-planner.html
  You can share it with family, print it, or bookmark it for reference!"
```

---

## Input Schema (JSON Config)

The `generate.py` script expects a JSON file with this structure:

```json
{
  "trip_name": "Caribbean Cruise 2026",
  "subtitle": "Western Caribbean · April 12–19 · 👶 Family",
  "departure_date": "2026-04-12",
  "trip_type": "cruise",
  "theme": "ocean",
  "vehicle_emoji": "🚢",
  "home_city": "Seattle, WA",
  "transport": {
    "flights": [
      {
        "airline": "Southwest Airlines",
        "confirmation": "AYLD5A",
        "from": "SEA",
        "to": "MCO",
        "date": "April 10",
        "time": "11:55 PM"
      }
    ],
    "car_rental": {
      "company": "Avis",
      "confirmation": "08401756US6",
      "start_date": "April 11",
      "end_date": "April 12",
      "type": "Full Size"
    },
    "parking": {
      "lot": "Seatac Crest Motor Inn",
      "address": "18845 International Blvd, SeaTac",
      "confirmation": "VN554608",
      "cost": 109.29
    }
  },
  "destinations": [
    {
      "id": "cococay",
      "name": "CocoCay",
      "country": "Bahamas 🇧🇸",
      "date": "Day 2 — Apr 13",
      "emoji": "🏝️",
      "color": "#f472b6",
      "lat": 25.8248,
      "lng": -77.7077,
      "image_url": "https://images.unsplash.com/...",
      "budget": {
        "total": 150,
        "items": [
          {
            "label": "Beach Club",
            "amount": 75,
            "fill_pct": 50
          },
          {
            "label": "Food",
            "amount": 40,
            "fill_pct": 27
          },
          {
            "label": "Snorkeling",
            "amount": 35,
            "fill_pct": 23
          }
        ]
      },
      "activities": [
        {
          "name": "Coco Beach Club",
          "price": "$75–99",
          "badge": "premium",
          "description": "Infinity pool with kiddie area, overwater cabanas, and private beach.",
          "recommended": true,
          "pros": ["Kiddie splash zone", "Lunch included", "Private beach", "Instagram-worthy"]
        },
        {
          "name": "South Beach (Free)",
          "price": "$0",
          "badge": "free",
          "description": "Beautiful free beach with calm, shallow turquoise water.",
          "recommended": false,
          "pros": ["Free lounge chairs", "Calm shallow water", "Less crowded"]
        }
      ],
      "timeline": [
        {
          "time": "7:00 AM",
          "title": "Breakfast on the Ship",
          "description": "Fill up before heading to the island."
        },
        {
          "time": "8:30 AM",
          "title": "Arrive at CocoCay",
          "description": "Tender to island. Head straight to beach area."
        }
      ],
      "tips": [
        "CocoCay is a tender port — strollers fold before boarding the small boat",
        "Get in line early for best beach spots",
        "Oasis Lagoon is the largest freshwater pool in the Caribbean",
        "Reef-safe sunscreen only — Bahamas requires it"
      ],
      "packing": [
        "Baby swimsuit + swim diapers (3+)",
        "Reef-safe SPF 50",
        "Sun hat + UV rash guard",
        "Toddler snacks & water bottles",
        "Sand toys (bucket & shovel)"
      ]
    }
  ],
  "special_focus": "toddler-friendly"
}
```

---

## Output

The generated HTML includes:

### Visual Design
- **Dark gradient background** (ocean blue for cruises, forest green for mountains, etc.)
- **Glass morphism cards** with blur effects
- **Animated wave effects** in the background
- **Particle twinkling animation** (stars, snow, bubbles based on theme)
- **Smooth scroll animations** for timeline items

### Interactive Features
- **Tab navigation** per destination + travel tab
- **Countdown timer** (days/hours/mins/secs until departure)
- **Canvas map** showing animated route between all destinations
- **Budget tracker** per destination with visual progress bars
- **Activity comparison cards** with free/premium/splurge badges
- **Timeline animation** on scroll (staggered fade-in)
- **Collapsible sections** (tips, packing checklist, confirmations)
- **Interactive packing checklist** with real-time progress
- **Scroll progress bar** at the top
- **Back-to-top button** (contextual color per tab)

### Content Sections
- **Header** with trip name, dates, subtitle, hero image
- **Countdown** to departure
- **Interactive canvas map** with ship route, ports, landmasses
- **Tab buttons** for each destination + travel logistics
- **Per-destination panels:**
  - Port banner (themed gradient background)
  - Hero image
  - Budget breakdown bar
  - Activity options (comparison cards)
  - Timeline with time-blocks
  - Tips (collapsible)
  - Packing checklist (collapsible, interactive)

### Technical
- **Single HTML file** — no external dependencies (except Google Fonts)
- **All CSS inline** in `<style>` tag
- **All JavaScript inline** in `<script>` tags
- **Responsive** (mobile-friendly CSS media queries)
- **Accessibility** (semantic HTML, focus states, contrast ratios)

---

## Customization Guide

### Colors & Themes

Each trip type has a default theme:

- **cruise** → ocean blues (`#0a1628` → `#1a4a6e`)
- **road_trip** → asphalt grays & forest (`#0f0f0f` → `#2a4a2a`)
- **flight** → sky gradients (`#001f3f` → `#0074d9`)
- **backpacking** → mountain greens (`#0a3d1a` → `#1a5a2a`)
- **family_vacation** → warm tropicals (`#2a1a0a` → `#5a3a1a`)

Per-destination colors can be hex codes (e.g., `#34d399`) or named colors passed to the template.

### Adding More Destinations

After generating, you can manually add more destination tabs by:

1. Adding a new tab button in the `<div class="tabs">` section
2. Duplicating a `<div class="day-panel">` block
3. Updating the `showTab()` JS function with new tab IDs

Or regenerate with updated JSON config.

### Canvas Map Coordinates

The interactive map uses **WGS84 latitude/longitude** bounds:
- Default bounds for Caribbean: `minLng: -92, maxLng: -74, minLat: 13, maxLat: 31`
- Adjust `MAP` object in canvas JS for different regions

Landmasses are hardcoded SVG-like arrays for common Caribbean islands. Add more `var islandName = [...]` arrays and include in the `landmasses[]` array.

### Fonts & Typography

Uses **Google Fonts "Nunito"** (sans-serif, weights 400–900). Change in the `@import` line if desired.

CSS variables for easy theming:
```css
:root {
  --bg-start: #0a1628;
  --bg-mid: #0f2847;
  --bg-end: #1a4a6e;
  --accent-primary: #f39c12;
  /* ... etc */
}
```

---

## File Structure

```
~/.agents/skills/trip-planner/
├── SKILL.md                      ← This file
├── GUIDE.md                      ← Detailed how-to guide
├── templates/
│   ├── base.html                 ← Main HTML template with {{PLACEHOLDERS}}
│   └── destination-block.html    ← Per-destination tab template
└── scripts/
    └── generate.py               ← Python script to render HTML from JSON
```

---

## Running the Skill

### Step 1: Load the Skill
```
Agent, load the "trip-planner" skill
```

### Step 2: Ask the Agent to Plan
```
"Let's plan a trip to Europe!"
```

### Step 3: Follow the Conversational Flow
The agent will ask Phase 1 → Phase 2 → ... questions.

### Step 4: Generate
Agent calls `generate.py` and opens the planner in your browser.

---

## API Reference

### `generate.py` Script

**Usage:**
```bash
python3 ~/.agents/skills/trip-planner/scripts/generate.py <config.json> <output.html> [--theme THEME]
```

**Arguments:**
- `config.json` — Path to JSON config file
- `output.html` — Output HTML file path (typically `~/Desktop/{trip-name}-planner.html`)
- `--theme` — Optional theme override (ocean, mountain, city, tropical, arctic)

**Returns:**
- Writes complete HTML to `output.html`
- Prints: `✅ Trip planner generated: ~/Desktop/my-trip-planner.html`

---

## Examples

### Example 1: Caribbean Cruise
```json
{
  "trip_name": "Star of the Seas",
  "subtitle": "Western Caribbean · April 12–19 · 👶 Toddler-Friendly",
  "departure_date": "2026-04-12",
  "trip_type": "cruise",
  "theme": "ocean",
  "vehicle_emoji": "🚢",
  "destinations": [
    { "name": "CocoCay", "emoji": "🏝️", "color": "#f472b6", ... },
    { "name": "Cozumel", "emoji": "🤿", "color": "#34d399", ... },
    ...
  ]
}
```

### Example 2: Road Trip
```json
{
  "trip_name": "Pacific Coast Highway",
  "subtitle": "California · 10 Days · 🚗 Road Trip",
  "departure_date": "2026-07-01",
  "trip_type": "road_trip",
  "theme": "coastal",
  "vehicle_emoji": "🚗",
  "destinations": [
    { "name": "San Francisco", "emoji": "🌉", ... },
    { "name": "Big Sur", "emoji": "🏔️", ... },
    { "name": "Los Angeles", "emoji": "☀️", ... }
  ]
}
```

### Example 3: Backpacking Adventure
```json
{
  "trip_name": "Thailand & Laos",
  "subtitle": "Southeast Asia · 3 Weeks · 🎒 Backpacking",
  "departure_date": "2026-12-01",
  "trip_type": "backpacking",
  "theme": "tropical",
  "vehicle_emoji": "🎒",
  "destinations": [
    { "name": "Bangkok", "emoji": "🏯", ... },
    { "name": "Chiang Mai", "emoji": "🏞️", ... },
    { "name": "Luang Prabang", "emoji": "🌾", ... }
  ]
}
```

---

## Tips for Best Results

1. **Get latitude/longitude early** — Use Google Maps to find precise coords for each destination
2. **Collect high-quality images** — Find good Unsplash URLs for each destination
3. **Be specific with activities** — Include prices, pros/cons, and recommendations
4. **Gather budget breakdowns** — Per-destination spending helps with planning
5. **Ask about special needs** — Toddlers, accessibility, dietary needs change everything
6. **Suggest themes** — If the user is unsure, recommend based on trip type
7. **Build incrementally** — Generate, review in browser, ask for tweaks, regenerate

---

## Troubleshooting

**Q: The HTML won't open in a browser**
A: Check that the output path is correct and has `.html` extension. Try manually opening with `open ~/Desktop/my-trip-planner.html`

**Q: Canvas map is blank**
A: Verify lat/lng coordinates are valid WGS84 format (lat: -90 to 90, lng: -180 to 180)

**Q: Images won't load**
A: Unsplash URLs expire or become unavailable. Update image URLs in the JSON config

**Q: Animations are choppy**
A: Large canvas or complex gradients can cause lag. Simplify theme or reduce particle count

**Q: Can't run generate.py**
A: Ensure Python 3 is installed. Test with: `python3 --version`

---

## Advanced Customization

### Adding New Destination Archetypes

Extend the `activities` suggestion logic in your agent prompt with domain-specific activities:

**Beach Destinations:** snorkeling, swimming, paddleboarding, beach volleyball, sunset dinner
**City Destinations:** museums, restaurants, walking tours, nightlife, shopping
**Mountain Destinations:** hiking, rock climbing, alpine skiing, scenic drives, wildlife
**Adventure:** zip-lining, skydiving, bungee jumping, cave exploration, white water rafting

### Modifying the Canvas Map

The `#cruise-map-canvas` JavaScript is fully configurable:
- Change `landmasses[]` arrays to add different coastlines
- Adjust `MAP` bounds for different regions
- Modify `routeLoop` to animate different vehicle paths
- Add compass rose, depth contours, or other overlays

### Extending Packing Checklist

The checklist is interactive in real-time. Add pre-populated items based on:
- Trip type (cruise vs. backpacking)
- Destinations (beach vs. mountain)
- Special needs (kids, accessibility, seasons)

---

## License

This skill is part of the Enchante AI Agent platform.

---

**Need help?** Ask your agent: "How do I use the trip-planner skill?"
