#!/usr/bin/env python3
"""
Trip Planner HTML Generator

Reads a JSON config file and renders a complete, self-contained HTML trip planner page.

Usage:
    python3 generate.py config.json output.html [--theme THEME]

Arguments:
    config.json   - Path to JSON config file
    output.html   - Path to output HTML file
    --theme       - Optional theme override (ocean, mountain, city, tropical, arctic)

Example:
    python3 ~/.agents/skills/trip-planner/scripts/generate.py \\
        ~/Desktop/trip-config.json \\
        ~/Desktop/my-trip-planner.html
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime

# Color themes for different trip types
THEMES = {
    'ocean': {
        'bg_start': '#0a1628',
        'bg_mid': '#0f2847',
        'bg_end': '#1a4a6e',
        'accent': '#f39c12',
    },
    'mountain': {
        'bg_start': '#0a1a0a',
        'bg_mid': '#1a3a1a',
        'bg_end': '#2a5a2a',
        'accent': '#10b981',
    },
    'city': {
        'bg_start': '#1a1a2e',
        'bg_mid': '#16213e',
        'bg_end': '#0f3460',
        'accent': '#7c4dff',
    },
    'tropical': {
        'bg_start': '#1a0a0a',
        'bg_mid': '#4a2010',
        'bg_end': '#8a5a2a',
        'accent': '#f472b6',
    },
    'arctic': {
        'bg_start': '#0a1a2e',
        'bg_mid': '#2a4a6e',
        'bg_end': '#4a7aae',
        'accent': '#06b6d4',
    },
}

# Default theme
DEFAULT_THEME = 'ocean'

# Caribbean landmasses for map
CARIBBEAN_LANDMASSES = """
var landmasses = [
  { pts: [[25.1,-80.3],[25.7,-80.1],[26.1,-80.1],[27.0,-80.2],[28.0,-80.6],[28.4,-80.6],[28.8,-80.7],[29.0,-81.0],[29.3,-81.3],[29.9,-81.4],[30.4,-81.4],[30.7,-81.5],[30.7,-87.5],[29.5,-89.5],[29.0,-89.2],[28.8,-89.0],[29.5,-87.0],[29.0,-85.0],[28.0,-82.5],[27.3,-82.5],[26.8,-82.0],[26.0,-81.7],[25.5,-81.3],[25.1,-80.3]], color: '#1a3a2a' },
  { pts: [[23.2,-84.5],[23.1,-82.0],[23.5,-81.0],[22.6,-79.0],[22.0,-77.5],[20.5,-74.2],[20.0,-75.0],[20.0,-77.5],[21.0,-80.0],[22.0,-82.5],[23.2,-84.5]], color: '#1a3a2a' },
  { pts: [[21.5,-87.2],[20.5,-87.0],[19.5,-87.5],[18.5,-88.5],[18.0,-88.0],[17.5,-88.5],[16.0,-88.5],[15.5,-88.0],[15.7,-87.0],[16.5,-86.0],[17.5,-86.0],[18.5,-86.5],[19.5,-87.0],[20.0,-87.5],[21.0,-86.9],[21.5,-86.7],[22.0,-86.8],[21.5,-87.2]], color: '#1a3a2a' },
  { pts: [[18.5,-78.3],[18.3,-77.1],[17.7,-76.2],[17.8,-77.2],[18.2,-78.0],[18.5,-78.3]], color: '#1a3a2a' },
  { pts: [[19.9,-73.5],[20.1,-72.0],[19.5,-71.0],[18.3,-71.5],[18.0,-73.0],[18.5,-74.5],[19.8,-74.5],[19.9,-73.5]], color: '#1a3a2a' },
  { pts: [[27.2,-78.5],[26.5,-78.0],[25.8,-77.7],[25.5,-77.0],[24.8,-76.0],[24.3,-76.2],[24.8,-77.5],[25.5,-78.5],[26.0,-79.0],[27.2,-78.5]], color: '#162e22' },
  { pts: [[16.5,-86.0],[16.3,-85.0],[15.8,-83.5],[15.0,-83.8],[14.5,-84.5],[14.0,-83.5],[13.5,-83.0],[13.0,-83.5],[13.2,-87.0],[14.0,-87.5],[15.0,-87.0],[15.8,-86.5],[16.5,-86.0]], color: '#1a3a2a' },
  { pts: [[18.5,-88.5],[18.5,-87.8],[17.5,-87.5],[16.0,-88.5],[16.0,-89.2],[17.5,-89.2],[18.5,-88.5]], color: '#1a3a2a' },
  { pts: [[15.5,-88.5],[15.5,-89.2],[13.5,-92.0],[14.5,-91.5],[15.0,-89.5],[15.5,-88.5]], color: '#1a3a2a' },
];
"""

def get_theme(theme_name):
    """Get theme colors by name."""
    theme = theme_name.lower() if theme_name else DEFAULT_THEME
    return THEMES.get(theme, THEMES[DEFAULT_THEME])

def render_activity(activity):
    """Render a single activity card."""
    recommended = activity.get('recommended', False)
    badge = activity.get('badge', 'premium')
    badge_map = {
        'free': 'badge-free',
        'premium': 'badge-premium',
        'splurge': 'badge-splurge',
    }
    badge_class = badge_map.get(badge, 'badge-premium')
    badge_label = {'free': '🆓 Free', 'premium': '💎 Premium', 'splurge': '💰 Splurge'}.get(badge, badge)
    
    recommended_class = 'recommended' if recommended else ''
    recommended_label = '⭐ Recommended' if recommended else ''
    
    pros_html = ''.join([f'<li>{pro}</li>' for pro in activity.get('pros', [])])
    
    html = f'''
    <div class="option-card {recommended_class}">
      <span class="option-badge {badge_class}">{recommended_label or badge_label}</span>
      <h4>{activity.get('name', 'Activity')}</h4>
      <div class="option-price">{activity.get('price', '$0')}</div>
      <p>{activity.get('description', '')}</p>
      <ul class="option-pros">
        {pros_html}
      </ul>
    </div>
    '''
    return html.strip()

def render_timeline_block(block):
    """Render a single timeline block."""
    html = f'''
    <div class="time-block visible">
      <div class="time-dot-wrap"><div class="time-dot"></div></div>
      <div class="time-card">
        <div class="time-label">{block.get('time', '00:00')}</div>
        <h3>{block.get('title', 'Event')}</h3>
        <p>{block.get('description', '')}</p>
        <div class="tag-row">
          <span class="tag">📍 {block.get('type', 'Activity')}</span>
        </div>
      </div>
    </div>
    '''
    return html.strip()

def render_tips(tips):
    """Render tips list."""
    tips_html = ''.join([f'<li><span class="bullet">💡</span><span>{tip}</span></li>' for tip in tips])
    return tips_html

def render_packing_items(items):
    """Render packing checklist items."""
    items_html = ''.join([
        f'<div class="pack-item" onclick="togglePack(this)"><div class="pack-check"></div>{item}</div>'
        for item in items
    ])
    return items_html

def render_budget_breakdown(budget_items):
    """Render budget breakdown (optional)."""
    if not budget_items:
        return ''
    
    html = '<div style="margin-bottom: 16px;">'
    for item in budget_items:
        pct = item.get('fill_pct', 0)
        html += f'''
        <div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 4px;">
          <span>{item.get('label', 'Item')}: ${item.get('amount', 0)}</span>
          <span>{pct}%</span>
        </div>
        <div style="height: 4px; background: rgba(255,255,255,0.1); border-radius: 2px; margin-bottom: 8px; overflow: hidden;">
          <div style="height: 100%; width: {pct}%; background: linear-gradient(90deg, var(--accent-primary), rgba(255,215,0,0.8));"></div>
        </div>
        '''
    html += '</div>'
    return html

def render_destination(dest, index):
    """Render a complete destination panel."""
    dest_id = dest.get('id', f'dest-{index}')
    dest_name = dest.get('name', f'Destination {index}')
    dest_country = dest.get('country', '')
    dest_date = dest.get('date', '')
    dest_emoji = dest.get('emoji', '📍')
    dest_color = dest.get('color', '#34d399')
    dest_image = dest.get('image_url', 'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=800&q=80')
    
    activities = dest.get('activities', [])
    activities_html = ''.join([render_activity(a) for a in activities])
    
    timeline = dest.get('timeline', [])
    timeline_html = ''.join([render_timeline_block(b) for b in timeline])
    
    tips = dest.get('tips', [])
    tips_html = render_tips(tips)
    
    packing = dest.get('packing', [])
    packing_html = render_packing_items(packing)
    packing_count = len(packing)
    
    budget = dest.get('budget', {})
    budget_items = budget.get('items', [])
    budget_breakdown_html = render_budget_breakdown(budget_items)
    budget_total = budget.get('total', 0)
    if isinstance(budget_total, (int, float)):
        budget_total = f'${budget_total}'
    
    # Build the destination block
    html = f'''
    <!-- Destination: {dest_name} -->
    <div class="day-panel" id="{dest_id}">

      <div class="port-banner" style="background: linear-gradient(135deg, {dest_color}, rgba(255,215,0,0.8));">
        <div class="port-icon">{dest_emoji}</div>
        <div class="port-info">
          <h2>{dest_name}</h2>
          <p class="port-sub">{dest_country} · {dest_date}</p>
          <div class="weather-badge">📍 {dest_country}</div>
        </div>
      </div>

      <div class="hero-image">
        <img src="{dest_image}" alt="{dest_name}" loading="lazy">
        <div class="hero-caption">{dest_emoji} {dest_name}</div>
      </div>

      <div class="budget-bar">
        <div class="budget-icon">💰</div>
        <div class="budget-info">
          <div class="budget-label">Estimated Budget</div>
          <div class="budget-amount">{budget_total}</div>
          <div class="budget-detail">Activities · Food · Transport · Shopping</div>
        </div>
        <div class="budget-progress">
          <div class="budget-fill" style="width: 50%; background: linear-gradient(90deg, {dest_color}, rgba(255,215,0,0.8));"></div>
        </div>
      </div>

      {budget_breakdown_html}

      <!-- Activities Section -->
      <div class="options-section">
        <h3>🎯 Things to Do</h3>
        <div class="option-cards">
          {activities_html}
        </div>
      </div>

      <!-- Timeline -->
      <div class="timeline">
        {timeline_html}
      </div>

      <!-- Tips (collapsible) -->
      <div class="collapsible open">
        <div class="collapsible-header" onclick="toggleCollapse(this)">
          <h3>💡 Local Tips</h3>
          <span class="chevron">▼</span>
        </div>
        <div class="collapsible-body">
          <ul class="tips-list">
            {tips_html}
          </ul>
        </div>
      </div>

      <!-- Pack Checklist (collapsible & interactive) -->
      <div class="collapsible open">
        <div class="collapsible-header" onclick="toggleCollapse(this)">
          <h3>🎒 Packing Checklist</h3>
          <span class="chevron">▼</span>
        </div>
        <div class="collapsible-body">
          <div class="pack-progress">
            <span class="{dest_id}-pack-text">0 / {packing_count} packed</span>
            <div class="pack-progress-bar"><div class="pack-progress-fill" id="{dest_id}-pack-fill"></div></div>
          </div>
          <div class="pack-grid" id="{dest_id}-checklist">
            {packing_html}
          </div>
        </div>
      </div>

    </div>
    '''
    
    return html

def render_tab_buttons(destinations):
    """Render tab navigation buttons."""
    html = ''
    for i, dest in enumerate(destinations):
        dest_id = dest.get('id', f'dest-{i}')
        dest_emoji = dest.get('emoji', '📍')
        dest_name = dest.get('name', f'Stop {i+1}')
        active_class = 'active' if i == 0 else ''
        html += f'''<button class="tab-btn {active_class}" data-tab="{dest_id}" onclick="showTab('{dest_id}')">{dest_emoji} {dest_name}</button>
'''
    return html

def get_map_bounds(destinations):
    """Calculate map bounds from destinations."""
    if not destinations:
        return {'minLng': -92, 'maxLng': -74, 'minLat': 13, 'maxLat': 31}  # Caribbean default
    
    lats = [d.get('lat', 0) for d in destinations]
    lngs = [d.get('lng', 0) for d in destinations]
    
    min_lat = min(lats) - 2
    max_lat = max(lats) + 2
    min_lng = min(lngs) - 2
    max_lng = max(lngs) + 2
    
    return {
        'minLat': min_lat,
        'maxLat': max_lat,
        'minLng': min_lng,
        'maxLng': max_lng,
    }

def render_map_ports_js(destinations):
    """Render JavaScript ports array for canvas map."""
    ports_js = 'var ports = [\n'
    
    for dest in destinations:
        name = dest.get('name', 'Port')
        lat = dest.get('lat', 0)
        lng = dest.get('lng', 0)
        color = dest.get('color', '#60a5fa')
        emoji = dest.get('emoji', '📍')
        country = dest.get('country', '')
        date = dest.get('date', '')
        
        facts = [f"📅 {date}", f"🌍 {country}"]
        facts_str = '", "'.join(facts)
        
        ports_js += f'''  {{ name: '{name}', lat: {lat}, lng: {lng}, color: '{color}', emoji: '{emoji}', location: '{country}', badge: 'PORT', facts: ["{facts_str}"] }},
'''
    
    ports_js += '];\n'
    return ports_js

def render_map_bounds_js(bounds):
    """Render JavaScript map bounds object."""
    return f'''var MAP = {{
    minLng: {bounds['minLng']},
    maxLng: {bounds['maxLng']},
    minLat: {bounds['minLat']},
    maxLat: {bounds['maxLat']}
}};
'''

def render_map_legend(destinations):
    """Render HTML legend for map."""
    html = ''
    for dest in destinations:
        name = dest.get('name', 'Destination')
        color = dest.get('color', '#60a5fa')
        html += f'<div class="legend-item"><span class="legend-dot" style="background:{color}"></span>{name}</div>\n'
    return html

def generate_html(config, template_path):
    """Generate HTML from config and template."""
    # Load base template
    with open(template_path, 'r') as f:
        base_html = f.read()
    
    # Extract config fields
    trip_name = config.get('trip_name', 'My Trip')
    trip_subtitle = config.get('subtitle', '')
    departure_date = config.get('departure_date', '')
    trip_type = config.get('trip_type', 'cruise')
    vehicle_emoji = config.get('vehicle_emoji', '🚀')
    destinations = config.get('destinations', [])
    
    # Get theme
    theme_name = config.get('theme', DEFAULT_THEME)
    theme = get_theme(theme_name)
    
    # Render components
    tab_buttons = render_tab_buttons(destinations)
    tab_panels = ''.join([render_destination(dest, i) for i, dest in enumerate(destinations)])
    
    map_ports_js = render_map_ports_js(destinations)
    map_bounds = get_map_bounds(destinations)
    map_bounds_js = render_map_bounds_js(map_bounds)
    map_legend = render_map_legend(destinations)
    
    # Substitute placeholders
    html = base_html
    html = html.replace('{{TRIP_NAME}}', trip_name)
    html = html.replace('{{TRIP_SUBTITLE}}', trip_subtitle)
    html = html.replace('{{DEPARTURE_DATE}}', f'"{departure_date}"')
    html = html.replace('{{VEHICLE_EMOJI}}', vehicle_emoji)
    html = html.replace('{{BG_START}}', f"'{theme['bg_start']}'")
    html = html.replace('{{BG_MID}}', f"'{theme['bg_mid']}'")
    html = html.replace('{{BG_END}}', f"'{theme['bg_end']}'")
    html = html.replace('{{ACCENT_PRIMARY}}', f"'{theme['accent']}'")
    html = html.replace('{{TAB_PANELS}}', tab_panels)
    html = html.replace('{{COUNTDOWN_LABEL}}', 'until departure')
    html = html.replace('{{MAP_PORTS_JS}}', map_ports_js)
    html = html.replace('{{MAP_BOUNDS_JS}}', map_bounds_js)
    html = html.replace('{{MAP_LANDMASSES_JS}}', CARIBBEAN_LANDMASSES)
    
    # Inject tabs
    tabs_div = html.find('<!-- Tabs -->')
    if tabs_div > 0:
        # Find the actual tabs div
        tabs_start = html.find('<div class="tabs" id="tabs">', tabs_div)
        tabs_end = html.find('</div>', tabs_start)
        if tabs_start > 0 and tabs_end > 0:
            html = html[:tabs_start + len('<div class="tabs" id="tabs">')] + '\n' + tab_buttons + html[tabs_end:]
    
    # Inject map legend
    legend_div = html.find('<div class="map-legend" id="map-legend">')
    if legend_div > 0:
        legend_end = html.find('</div>', legend_div)
        if legend_end > 0:
            html = html[:legend_div + len('<div class="map-legend" id="map-legend">')] + '\n' + map_legend + html[legend_end:]
    
    return html

def main():
    """Main entry point."""
    if len(sys.argv) < 3:
        print("Usage: python3 generate.py <config.json> <output.html> [--theme THEME]")
        sys.exit(1)
    
    config_path = sys.argv[1]
    output_path = sys.argv[2]
    theme_override = None
    
    if len(sys.argv) >= 5 and sys.argv[3] == '--theme':
        theme_override = sys.argv[4]
    
    # Read config
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"❌ Error reading config: {e}")
        sys.exit(1)
    
    # Apply theme override
    if theme_override:
        config['theme'] = theme_override
    
    # Get template path (relative to this script)
    script_dir = Path(__file__).parent
    template_path = script_dir.parent / 'templates' / 'base.html'
    
    if not template_path.exists():
        print(f"❌ Template not found: {template_path}")
        sys.exit(1)
    
    # Generate HTML
    try:
        html = generate_html(config, str(template_path))
    except Exception as e:
        print(f"❌ Error generating HTML: {e}")
        sys.exit(1)
    
    # Write output
    try:
        output_file = Path(output_path).expanduser()
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(html)
    except Exception as e:
        print(f"❌ Error writing output: {e}")
        sys.exit(1)
    
    # Success
    print(f"✅ Trip planner generated successfully!")
    print(f"📄 File: {output_file}")
    print(f"\nYou can now:")
    print(f"  • Open: open {output_file}")
    print(f"  • Share the HTML file with family")
    print(f"  • Print to PDF for offline access")

if __name__ == '__main__':
    main()
