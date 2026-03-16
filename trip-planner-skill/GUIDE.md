---
title: Trip Planner Skill — Complete How-To Guide
---

# 📚 Trip Planner Skill — Complete How-To Guide

A step-by-step guide to using the trip-planner skill to create interactive, beautiful HTML trip planner pages.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Understanding the Workflow](#understanding-the-workflow)
3. [Asking Questions Phase-by-Phase](#asking-questions-phase-by-phase)
4. [Building the JSON Config](#building-the-json-config)
5. [Running the Generator](#running-the-generator)
6. [Customizing Your Planner](#customizing-your-planner)
7. [Examples by Trip Type](#examples-by-trip-type)
8. [Advanced Tips](#advanced-tips)

---

## Quick Start

### In 60 Seconds

```bash
# 1. Ask the agent for trip planning help
Agent: "Plan a trip for me!"

# 2. Answer the agent's questions (5–10 minutes)
Agent: "Name of trip?"
You: "Mediterranean Cruise 2026"

# Agent asks more questions...

# 3. Agent generates HTML
Agent: "Generating your planner..."

# 4. Opens automatically
✅ HTML planner opens in your browser!
```

---

## Understanding the Workflow

### 🔄 The Three Phases

```
┌─────────────────────────────────────────────────────┐
│ PHASE 1: Gather Input                               │
│ Agent asks conversational questions, one group at   │
│ a time. User provides details about trip.           │
│                                                      │
│ Trip Basics → Transport → Destinations → Budget →  │
│ Packing → Map Coordinates → Special Needs          │
└─────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────┐
│ PHASE 2: Build JSON                                 │
│ Agent synthesizes user responses into a JSON config │
│ file matching the generate.py schema                │
└─────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────┐
│ PHASE 3: Generate & Output                          │
│ Agent calls generate.py with the JSON config        │
│ Script renders complete HTML file                   │
│ HTML opens in browser                               │
└─────────────────────────────────────────────────────┘
```

### ✅ What You Get

A **single, self-contained HTML file** with:

- ✨ **Beautiful dark theme** with ocean/sky gradients
- 🎨 **Glass morphism UI** with blur effects & animations
- 🗺️ **Interactive canvas map** with animated ship/plane/car
- 📊 **Budget tracker** per destination
- 📋 **Activity comparison cards** (free/premium/splurge)
- 📅 **Animated timeline** with scroll effects
- ✅ **Interactive packing checklist** with progress
- ⏳ **Countdown timer** to departure
- 📱 **Responsive design** (works on phone & tablet)
- 🚀 **No build step required** — just open in browser!

---

## Asking Questions Phase-by-Phase

### 🎯 Phase 1: Trip Basics

Ask one question at a time. Be conversational!

```
Agent: "Let's plan an amazing trip! 🌍
        First, I need the basics:
        
        What's the name of your trip? 
        (e.g., 'Caribbean Cruise 2026', 'Europe 2026', 'Road Trip 2026')"

User: "Mediterranean Cruise April 2026"

Agent: "Love it! 🚢 Now, what type of trip is this?
        
        • cruise
        • road_trip
        • flight
        • backpacking
        • family_vacation"

User: "cruise"

Agent: "Perfect! Cruise it is. When does it depart?
        (Start date as YYYY-MM-DD, e.g., 2026-04-12)"

User: "2026-04-12"

Agent: "And when do you return?
        (End date as YYYY-MM-DD)"

User: "2026-04-19"

Agent: "April 12–19, got it! ✓
        
        One more: Where are you flying from?
        (City & airport, e.g., 'Seattle (SEA)', 'New York (JFK)')"

User: "Seattle WA"

Agent: "Final bit: Can you describe the trip in 1–2 words for a subtitle?
        (e.g., 'Western Caribbean · 👶 Family', 'Mediterranean · ✨ Romantic')"

User: "Western Caribbean · 👶 Toddler-Friendly"

Agent: "✅ Trip basics complete! Let me ask about transport next..."
```

**Key Tips:**
- Ask one question per message (easier to follow)
- Suggest formats or examples
- Confirm understanding after each answer
- Use emojis to stay upbeat

### 🚗 Phase 2: Transport

If applicable, ask about flights, car rental, parking, hotels before/after.

```
Agent: "Great! Now, the logistics:

        Do you have flight details? 
        (Airline, confirmation #, from→to, date & time)
        
        Or just say 'No flights' if you're already at the port."

User: "Southwest Airlines, SEA to Orlando MCO, April 10, 11:55 PM, confirmation AYLD5A"

Agent: "Got it! 
        • Southwest AYLD5A
        • SEA → MCO
        • April 10, 11:55 PM
        
        Any car rental? (Company, dates, confirmation #)"

User: "Yes, Avis Full Size, April 11 1 PM to April 12 1 PM, 08401756US6"

Agent: "Perfect. And parking at your home airport?
        (Parking lot name, address, cost)"

User: "Seatac Crest Motor Inn, 18845 International Blvd, SeaTac, $109"

Agent: "✅ Transport locked in. Now for the destinations..."
```

**Transport Data to Collect:**
- Flights: airline, confirmation, route, time, seat class (if relevant)
- Car rental: company, dates, vehicle type, confirmation
- Parking: lot name, address, cost, valet/self-park
- Hotels: before/after cruise, check-in/out, cost

### 🏝️ Phase 3: Destinations

**First, ask the count:**

```
Agent: "How many destinations / port stops / cities will you visit?
        (Not counting your home port)"

User: "4 — CocoCay, Cozumel, Costa Maya, and Roatán"
```

**Then, for each destination, ask in order:**

```
Agent: "Let's detail Destination 1: CocoCay
        
        1️⃣  What's the location & country?
        (e.g., 'Cozumel, Mexico 🇲🇽')"

User: "CocoCay, Bahamas 🇧🇸"

Agent: "2️⃣  What date/day will you be there?
        (e.g., 'Day 2 — April 13')"

User: "Day 2 — April 13"

Agent: "3️⃣  Pick an emoji to represent this destination
        (🏝️ 🏖️ 🤿 🏔️ 🗼 🎪 etc.)"

User: "🏝️"

Agent: "4️⃣  What color theme should this destination have?
        (Hex color, e.g., '#f472b6' for pink, or I can suggest one)
        
        [If user is unsure, suggest: 'For a tropical island, how about #f472b6 (pink) or #34d399 (turquoise)?']"

User: "#f472b6"

Agent: "5️⃣  Now, 3–5 activities/things to do at CocoCay:
        
        For each, tell me:
        • Activity name
        • Cost (e.g., '$45' or 'Free')
        • Type: free / premium / splurge
        • Quick description (1–2 sentences)
        • Is it a 'recommended pick'? (yes/no)
        
        First activity?"

User: "Coco Beach Club, $75–99, premium, Infinity pool with kiddie area and private beach, recommended"

Agent: "Got it! 
        • Coco Beach Club
        • $75–99 (premium)
        • Kiddie infinity pool ✓
        
        Next activity?"

User: "South Beach free area, free, free beach with calm shallow water, not recommended but good backup"

Agent: "3rd activity?"

User: "Overwater cabanas, $350–600, splurge, book with friends to split cost!"

Agent: "✅ 3 activities recorded for CocoCay.
        
        6️⃣  Timeline for CocoCay: 
        What's your rough schedule?
        (e.g., 8 AM arrive, 9 AM beach, 12 PM lunch, 3 PM back to ship)
        
        Give me 3–5 time-blocks with activity name."

User: "7 AM breakfast ship, 8:30 AM tender to island, 9 AM beach & snorkel, 12 PM lunch, 3 PM back to ship"

Agent: "Perfect timeline! 
        
        7️⃣  Local tips for CocoCay:
        (3–5 insider tips — what should they know?)"

User: "Get in tender line early for best spots, reef-safe sunscreen required, oasis lagoon is huge, no baby changing tables so bring portable pad, drinks on ship are cheaper than island"

Agent: "🎒 8️⃣  Packing items specific to CocoCay:
        (5–8 items)"

User: "Baby swimsuit, swim diapers, reef safe SPF 50, sun hat, snorkel gear for adults, beach toys, waterproof phone case, portable changing pad"

Agent: "✅ CocoCay details complete!
        
        What's the latitude & longitude for CocoCay?
        (Or I can look it up — I'll estimate 25.82°N, 77.71°W)"

User: "Those coordinates are perfect!"

Agent: "Excellent! Let me detail the next destination... 
        Destination 2: Cozumel, Mexico
        
        1️⃣  Country & flag?"

User: "Cozumel, Mexico 🇲🇽"

[... repeat process for remaining destinations ...]
```

**For Each Destination, Collect:**

| Field | Example | Notes |
|-------|---------|-------|
| Name & Country | "Cozumel, Mexico 🇲🇽" | Include flag emoji |
| Date/Day | "Day 4 — April 15" | Helps with timeline |
| Emoji | "🤿" | Visual identifier |
| Color Hex | "#34d399" | For theme/theme consistency |
| Activities (3–5) | Name, Price, Badge, Description, Recommended? | See activity structure |
| Timeline (3–5 items) | Time, Activity, Description | Anchor the day |
| Tips (3–5) | Local knowledge, logistics | Make it actionable |
| Packing (5–8) | Items specific to destination | Pre-fill traveler's checklist |
| Lat/Lng | 25.8248, -77.7077 | For interactive map |
| Image URL | Unsplash link | Hero image for tab |

### 💰 Phase 4: Budget

```
Agent: "Let's break down the budget:
        
        For CocoCay:
        • Total estimated spend? (e.g., '$100–150')"

User: "$150"

Agent: "Great. How does that break down?
        (Activities, Food, Transport, Shopping — give me rough % or $ for each)
        
        E.g., 'Activities $75, Food $40, Transport $20, Shopping $15'"

User: "Beach Club $75, Food $40, Activities $20, Souvenirs $15"

Agent: "✅ CocoCay Budget:
        • Beach Club: $75 (50%)
        • Food: $40 (27%)
        • Activities: $20 (13%)
        • Souvenirs: $15 (10%)
        
        Next destination (Cozumel) budget?"

[Repeat for each destination...]
```

**Budget Breakdown Tips:**
- Suggest typical categories: Activities, Food, Transport, Shopping, Tips
- Ask for estimates (agents don't need exact #s)
- Calculate percentages for visual bar charts

### 🎒 Phase 5: Packing & Special Needs

```
Agent: "Finally, some logistics:
        
        Are there any special considerations?
        (Toddler? Elderly parents? Accessibility needs? Adventure focus? Luxury?)"

User: "16-month-old toddler, first cruise, very family-focused"

Agent: "Great context! That'll help me suggest activities and packing.
        
        Any general packing items to remember?
        (Not per-destination, but overall)"

User: "Passports, credit cards, toddler medications, extra diapers, familiar comfort toy"

Agent: "Perfect! I have all the info I need.
        
        Let me build your planner now... ✨"

[Agent generates JSON config and calls generate.py]

Agent: "✅ Your trip planner is ready!
        
        📱 Open here: ~/Desktop/caribbean-cruise-2026-planner.html
        
        You can:
        • Share the link with family
        • Print to PDF for offline access
        • Edit the HTML directly to add more details
        
        Want me to update anything?"
```

---

## Building the JSON Config

Once you've gathered all the info, structure it into JSON:

```json
{
  "trip_name": "Star of the Seas Caribbean Cruise",
  "subtitle": "Western Caribbean · April 12–19 · 👶 Toddler-Friendly",
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
      "type": "Full Size",
      "start_date": "April 11",
      "end_date": "April 12"
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
      "date": "Day 2 — April 13",
      "emoji": "🏝️",
      "color": "#f472b6",
      "lat": 25.8248,
      "lng": -77.7077,
      "image_url": "https://images.unsplash.com/photo-XXX",
      "budget": {
        "total": 150,
        "items": [
          {"label": "Beach Club", "amount": 75, "fill_pct": 50},
          {"label": "Food", "amount": 40, "fill_pct": 27},
          {"label": "Activities", "amount": 20, "fill_pct": 13},
          {"label": "Souvenirs", "amount": 15, "fill_pct": 10}
        ]
      },
      "activities": [
        {
          "name": "Coco Beach Club",
          "price": "$75–99",
          "badge": "premium",
          "description": "Infinity pool with kiddie area, private beach, lunch included.",
          "recommended": true,
          "pros": ["Infinity pool", "Kiddie splash zone", "Lunch buffet", "Private beach"]
        },
        {
          "name": "South Beach (Free)",
          "price": "$0",
          "badge": "free",
          "description": "Beautiful free beach with calm water and lounge chairs.",
          "recommended": false,
          "pros": ["Free", "Calm water", "Less crowded"]
        }
      ],
      "timeline": [
        {
          "time": "7:00 AM",
          "title": "Breakfast on Ship",
          "description": "Fill up before heading to island."
        },
        {
          "time": "8:30 AM",
          "title": "Arrive at CocoCay",
          "description": "Tender to island. Head to beach."
        }
      ],
      "tips": [
        "Get in tender line early for best beach spots",
        "Reef-safe sunscreen required",
        "Oasis Lagoon is the largest freshwater pool in Caribbean",
        "No baby changing stations — bring portable changing pad"
      ],
      "packing": [
        "Baby swimsuit + swim diapers (3+)",
        "Reef-safe SPF 50",
        "Sun hat + UV rash guard",
        "Snorkel gear (adults)",
        "Waterproof phone case",
        "Portable changing pad",
        "Comfort toy"
      ]
    }
  ],
  "special_focus": "toddler-friendly"
}
```

**Key Fields:**
- `trip_name` — Full name
- `subtitle` — Short description (appears under title)
- `departure_date` — ISO format (YYYY-MM-DD)
- `trip_type` — cruise | road_trip | flight | backpacking | family_vacation
- `theme` — ocean | mountain | city | tropical | arctic (controls gradient colors)
- `vehicle_emoji` — 🚢 ✈️ 🚗 🎒 🏕️
- `destinations` — Array of destination objects
  - Each destination must have: id, name, country, date, emoji, color, lat, lng, image_url
  - Activities: name, price, badge (free|premium|splurge), description, recommended
  - Timeline: time, title, description
  - Tips: array of strings
  - Packing: array of strings

---

## Running the Generator

### Command Line

```bash
python3 ~/.agents/skills/trip-planner/scripts/generate.py config.json output.html
```

**Example:**
```bash
python3 ~/.agents/skills/trip-planner/scripts/generate.py \
  ~/Desktop/cruise-config.json \
  ~/Desktop/caribbean-cruise-2026-planner.html
```

**Output:**
```
✅ Trip planner generated successfully!
📄 File: ~/Desktop/caribbean-cruise-2026-planner.html
   
You can now:
• Open in browser: open ~/Desktop/caribbean-cruise-2026-planner.html
• Share the HTML file with family
• Print to PDF
```

### From the Agent

The agent can run this for you:

```python
# Pseudocode (agent implementation)

import json
import subprocess

config = {
  "trip_name": "My Caribbean Cruise",
  "subtitle": "Western Caribbean · April 12–19 · 👶 Family",
  # ... (full config from user input)
}

# Save config to temp file
with open("/tmp/trip_config.json", "w") as f:
  json.dump(config, f)

# Run generator
result = subprocess.run([
  "python3",
  "~/.agents/skills/trip-planner/scripts/generate.py",
  "/tmp/trip_config.json",
  "~/Desktop/my-trip-planner.html"
], capture_output=True)

print(result.stdout)  # Print success message
```

---

## Customizing Your Planner

### ✏️ Editing After Generation

The generated HTML is **fully editable**. You can:

1. **Change colors:**
   - Find `:root { --bg-start: ... }` in the `<style>` tag
   - Modify hex color values

2. **Update content:**
   - Change tab button text
   - Edit timeline descriptions
   - Update packing list items
   - Modify destination names

3. **Add more destinations:**
   - Duplicate a `<div class="day-panel">` block
   - Create new tab button in `<div class="tabs">`
   - Update `showTab()` JavaScript function

4. **Adjust canvas map:**
   - Modify `ports[]` array in the canvas script
   - Update latitude/longitude for routes
   - Add/remove landmass outlines

### 🎨 Theme Customization

**CSS Variables** at top of `<style>`:

```css
:root {
  /* Background gradients */
  --bg-start: #0a1628;
  --bg-mid: #0f2847;
  --bg-end: #1a4a6e;

  /* Text colors */
  --text-primary: #f0f4f8;
  --text-secondary: rgba(255,255,255,0.7);

  /* Accent colors per destination */
  --accent-costa: #f39c12;
  --accent-roatan: #2ecc71;
  /* etc. */

  /* Glass morphism */
  --card-bg: rgba(255,255,255,0.07);
  --card-border: rgba(255,255,255,0.12);
  --glass: rgba(255,255,255,0.06);
}
```

**Change overall theme:**
```css
/* For a warmer, tropical theme */
:root {
  --bg-start: #1a0a0a;      /* Warm dark brown */
  --bg-mid: #4a2010;        /* Tan */
  --bg-end: #8a5a2a;        /* Lighter tan */
}
```

### 🗺️ Interactive Map Customization

The canvas map in the HTML is fully customizable. To adjust the region:

```javascript
// Find this in the canvas script:
var MAP = { minLng:-92, maxLng:-74, minLat:13, maxLat:31 };

// Change to your region:
// Europe: { minLng:-10, maxLng:40, minLat:35, maxLat:70 }
// USA: { minLng:-130, maxLng:-60, minLat:20, maxLat:50 }
// Southeast Asia: { minLng:95, maxLng:145, minLat:-10, maxLat:20 }
```

To add new landmass outlines:

```javascript
// Add array of [lat, lng] coordinates
var newIsland = [[x1,y1], [x2,y2], [x3,y3], ...];

// Add to landmasses array
landmasses.push({
  pts: newIsland,
  color: '#1a3a2a'
});
```

---

## Examples by Trip Type

### 🚢 Cruise Example

**Trip Basics:**
- Name: "Star of the Seas Caribbean Cruise"
- Type: cruise
- Dates: April 12–19, 2026
- Departs: Port Canaveral, FL

**Destinations:**
1. CocoCay (Bahamas) — Day 2
2. Cozumel (Mexico) — Day 4
3. Costa Maya (Mexico) — Day 5
4. Roatán (Honduras) — Day 6

**Theme:** Ocean (blue gradients)
**Vehicle:** 🚢

**Activities per destination:**
- Beach/water sports
- Snorkeling & diving
- Shore excursions
- Food tours
- Cultural sites

**Timeline:**
- Early morning: breakfast on ship
- Mid-morning: arrival at port
- Afternoon: activities & beach
- Evening: return to ship

---

### 🚗 Road Trip Example

**Trip Basics:**
- Name: "Pacific Coast Highway"
- Type: road_trip
- Dates: July 1–15, 2026
- Home: San Francisco, CA

**Destinations:**
1. Carmel-by-the-Sea — Day 1–2
2. Big Sur — Day 3–4
3. Santa Barbara — Day 5–6
4. Los Angeles — Day 7–8

**Theme:** Coastal (grays & blues)
**Vehicle:** 🚗

**Activities per destination:**
- Scenic drives
- Hiking trails
- Beach access
- Local restaurants
- Photo spots
- Wine tasting
- Lodging info

**Budget:**
- Gas
- Hotels
- Food & dining
- Activities & attractions

---

### ✈️ Flight Trip Example

**Trip Basics:**
- Name: "Europe 2026"
- Type: flight
- Dates: June 10–25, 2026
- Home: New York (JFK)

**Destinations:**
1. London — Day 1–3
2. Paris — Day 4–6
3. Amsterdam — Day 7–8
4. Berlin — Day 9–11

**Theme:** City (dark purples & grays)
**Vehicle:** ✈️

**Transport:**
- Flights: details for each leg
- Train passes (Europe)
- Car rentals in each city
- Hotels

**Activities:**
- Museums
- Historical sites
- Food experiences
- Nightlife
- Shopping

---

### 🎒 Backpacking Example

**Trip Basics:**
- Name: "Southeast Asia Adventure"
- Type: backpacking
- Dates: December 1–31, 2026
- Home: USA

**Destinations:**
1. Bangkok, Thailand
2. Chiang Mai, Thailand
3. Luang Prabang, Laos
4. Hanoi, Vietnam

**Theme:** Tropical (greens & golds)
**Vehicle:** 🎒

**Activities:**
- Temple visits
- Hiking & trekking
- Local markets
- Street food tours
- Meditation retreats
- Budget accommodations

**Budget:**
- Usually very low (backpacker-friendly)
- Per destination breakdown

**Special Focus:**
- Safety tips
- Visa info
- Best transportation between cities

---

## Advanced Tips

### 💡 Pro Tips

1. **Use Unsplash for images**
   - Search "[destination] landscape" on unsplash.com
   - Copy the full image URL (quality=quality)
   - Example: `https://images.unsplash.com/photo-XXX?w=800&q=80`

2. **Find lat/lng easily**
   - Google Maps: right-click → copy coordinates
   - Format: `25.8248, -77.7077` (lat, lng with decimals)

3. **Budget tips**
   - Ask user for rough estimates, not exact prices
   - Activities typically: free ($0–10), premium ($10–50), splurge ($50+)
   - Include tips & taxes in estimates

4. **Activity descriptions**
   - Be specific: "Snorkel the Mesoamerican Barrier Reef" not just "snorkel"
   - Include why it's great
   - Mention any special tips (e.g., "Wear water shoes", "Bring towel")

5. **Color selection**
   - Match destination vibe: beaches=pink/turquoise, mountains=green, cities=purple
   - Hex color suggestions:
     - Tropical/Beaches: `#f472b6` (pink), `#34d399` (turquoise), `#fbbf24` (gold)
     - Mountains: `#10b981` (green), `#6366f1` (indigo), `#8b5cf6` (purple)
     - Cities: `#7c4dff` (deep purple), `#1f2937` (charcoal), `#0ea5e9` (cyan)
     - Adventure: `#dc2626` (red), `#f59e0b` (orange), `#a16207` (brown)

6. **Timeline best practices**
   - 3–5 time blocks per destination
   - Include: breakfast/lunch/dinner, arrival/departure, main activities
   - Format times as "9:00 AM", "12:30 PM", "6:00 PM"

7. **Packing checklist**
   - Pre-fill with destination-specific items
   - Include: weather-appropriate clothing, activity gear, comfort items
   - Mark essentials as "must-pack"

8. **Tips section**
   - Insider knowledge: "Get there early", "Book in advance", "Try the local..."
   - Logistical: "Taxis don't use meters", "WiFi is spotty", "Cash accepted everywhere"
   - Cultural: "Learn a few local phrases", "Respect dress codes at temples"

### 🎓 Common Gotchas

**Problem:** "Coordinates are backwards (lng, lat instead of lat, lng)"
**Solution:** Remember: **Latitude first, then Longitude**
- Latitude: -90 to +90 (North/South)
- Longitude: -180 to +180 (East/West)
- Example: New York = 40.7128 (lat), -74.0060 (lng)

**Problem:** "Activity prices have dollar signs but don't render"
**Solution:** Use consistent format: "$45", "$0–50", "Free"

**Problem:** "Canvas map doesn't show landmasses"
**Solution:** Check that coordinates are within the `MAP` bounds. For Caribbean: `-92 to -74` (lng), `13 to 31` (lat)

**Problem:** "Packing checklist doesn't save progress when I reload"
**Solution:** This is a local-page feature. Progress doesn't persist unless you print/PDF. The HTML is read-only in most cases — to save, user needs to print to PDF or screenshot.

### 🚀 Extending the Skill

**Ideas for future enhancements:**

1. **Weather integration** — Show forecast for each destination
2. **Dynamic pricing** — Pull real activity prices from APIs
3. **Photo gallery** — Embed Instgram or Flickr feeds per destination
4. **Travel budget tracker** — Real-time spending calculator
5. **Mobile app export** — Generate .ics calendar files
6. **Collaboration** — Shareable links with family input
7. **Post-trip journal** — Turn planner into a travel diary
8. **PDF export** — Built-in print-to-PDF with better formatting

---

## Support & Troubleshooting

### ❓ FAQs

**Q: Can I add more destinations after generation?**
A: Yes! Duplicate a destination panel (`<div class="day-panel">`) and update the tab button and JavaScript.

**Q: Can I share the HTML with family?**
A: Absolutely! Just email the .html file or share via cloud storage (Dropbox, Google Drive, etc.).

**Q: Will it work offline?**
A: Yes! Except images require internet. Download the page first with images cached.

**Q: Can I print it to PDF?**
A: Yes! Use browser print (Cmd+P / Ctrl+P), select "Save as PDF", and it'll preserve all styling.

**Q: Do I need to pay anything?**
A: No! This skill is free and open-source.

### 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| HTML won't open | Check file path, ensure .html extension |
| Images won't load | Verify Unsplash URLs are still valid |
| Map is blank | Check lat/lng coordinates are in correct range |
| Animations are slow | Reduce particle count in CSS or simplify gradients |
| Checklist progress doesn't save | This is expected — use browser's "Save As..." to preserve |
| Can't run generate.py | Ensure Python 3 installed: `python3 --version` |

---

**Next Steps:** [Load the skill](#) and start planning your trip! 🎉
