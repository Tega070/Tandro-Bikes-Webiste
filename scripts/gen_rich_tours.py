import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_tour_pages import (
    HEAD_CSS, NAV_HTML, FOOTER_HTML, SCRIPTS_HTML, GTAG, LOCALBUSINESS_LD,
    breadcrumb_ld, wa_link, BASE
)

EXTRA_CSS = r"""
    .trip-facts { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 32px 0 48px; }
    @media (min-width: 640px) { .trip-facts { grid-template-columns: repeat(4, 1fr); } }
    .trip-fact { display: flex; align-items: flex-start; gap: 12px; padding: 18px; background: var(--surface); border-radius: 8px; border: 1px solid var(--border); }
    .trip-fact svg { flex-shrink: 0; color: var(--green); margin-top: 2px; }
    .trip-fact-title { font-family: var(--font-heading); font-weight: 700; font-size: 14px; color: var(--dark); margin-bottom: 2px; }
    .trip-fact-text { font-size: 13px; color: var(--muted); line-height: 1.5; }

    .sights-list { display: flex; flex-direction: column; margin-top: 8px; }
    .sight-row { display: grid; grid-template-columns: 1fr; gap: 10px; padding: 26px 0; border-bottom: 1px solid var(--border); }
    .sight-row:first-child { padding-top: 0; }
    .sight-row:last-child { border-bottom: none; padding-bottom: 0; }
    .sight-row h3 { font-family: var(--font-heading); font-weight: 700; font-size: 18px; color: var(--dark); display: flex; align-items: center; gap: 10px; }
    .sight-row h3::before { content: ''; display: block; width: 8px; height: 8px; border-radius: 50%; background: var(--green); flex-shrink: 0; }
    .sight-row p { font-size: 15px; color: var(--muted); line-height: 1.75; padding-left: 18px; }

    .day-block { margin-top: 8px; display: flex; flex-direction: column; gap: 24px; }
    .day-block-item h3 { font-family: var(--font-heading); font-weight: 700; font-size: 16px; color: var(--dark); margin-bottom: 8px; }
    .day-block-item p { font-size: 15px; color: var(--muted); line-height: 1.75; }

    .info-columns { display: grid; grid-template-columns: 1fr; gap: 32px; margin-top: 8px; }
    @media (min-width: 640px) { .info-columns { grid-template-columns: 1fr 1fr; } }
    .info-col-title { font-family: var(--font-heading); font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--green); margin-bottom: 14px; }
    .info-list { list-style: none; display: flex; flex-direction: column; gap: 10px; font-size: 15px; color: #1e293b; }
    .info-list li { display: flex; align-items: flex-start; gap: 10px; line-height: 1.5; }
    .info-list.check li::before { content: ''; display: block; flex-shrink: 0; width: 18px; height: 18px; margin-top: 1px; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2322c55e' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E"); background-size: contain; background-repeat: no-repeat; }
    .info-list.pack li::before { content: ''; display: block; flex-shrink: 0; width: 18px; height: 18px; margin-top: 1px; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%232563EB' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='9'/%3E%3C/svg%3E"); background-size: contain; background-repeat: no-repeat; }
    .info-note { margin-top: 16px; font-size: 14px; color: var(--muted); line-height: 1.7; font-style: italic; }

    .itinerary-timeline { display: flex; flex-direction: column; margin-top: 8px; }
    .itinerary-day { display: grid; grid-template-columns: 56px 1fr; gap: 20px; padding: 24px 0; border-bottom: 1px solid var(--border); position: relative; }
    .itinerary-day:first-child { padding-top: 0; }
    .itinerary-day:last-child { border-bottom: none; padding-bottom: 0; }
    .itinerary-day-badge { width: 44px; height: 44px; border-radius: 50%; background: var(--dark); color: var(--white); display: flex; align-items: center; justify-content: center; font-family: var(--font-heading); font-weight: 700; font-size: 14px; flex-shrink: 0; }
    .itinerary-day-content h3 { font-family: var(--font-heading); font-weight: 700; font-size: 16px; color: var(--dark); margin-bottom: 4px; }
    .itinerary-day-content p { font-size: 14px; color: var(--muted); line-height: 1.6; }
    .itinerary-day-time { font-family: var(--font-heading); font-size: 12px; font-weight: 600; color: var(--green); text-transform: uppercase; letter-spacing: 0.5px; }

    .meeting-box { margin-top: 8px; display: flex; flex-direction: column; gap: 10px; padding: 24px; background: var(--surface); border-radius: 8px; border: 1px solid var(--border); }
    .meeting-box-title { font-family: var(--font-heading); font-weight: 700; font-size: 16px; color: var(--dark); }
    .meeting-box-text { font-size: 14px; color: var(--muted); line-height: 1.6; }

    .not-suitable { margin-top: 12px; display: flex; flex-wrap: wrap; gap: 10px; }
    .not-suitable span { font-family: var(--font-heading); font-size: 13px; font-weight: 600; color: #b91c1c; background: rgba(239,68,68,0.1); border: 1px solid rgba(239,68,68,0.25); padding: 7px 14px; border-radius: 20px; }

    .booking-box { background: var(--dark); border-radius: 12px; padding: 40px 28px; margin-top: 8px; }
    .booking-box-title { font-family: var(--font-display); font-size: 32px; color: var(--white); margin-bottom: 12px; }
    .booking-box-text { font-size: 15px; color: rgba(255,255,255,0.65); line-height: 1.7; max-width: 560px; margin-bottom: 24px; }
"""

def facts_html(facts):
    rows = []
    for icon_path, title, text in facts:
        rows.append(f"""        <div class="trip-fact">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icon_path}</svg>
          <div><p class="trip-fact-title">{title}</p><p class="trip-fact-text">{text}</p></div>
        </div>""")
    return "\n".join(rows)

ICON_CLOCK = "<circle cx='12' cy='12' r='9'/><polyline points='12 7 12 12 15 15'/>"
ICON_MAP = "<path d='M9 20l-6-3V4l6 3 6-3 6 3v13l-6-3-6 3z'/><line x1='9' y1='7' x2='9' y2='20'/><line x1='15' y1='4' x2='15' y2='17'/>"
ICON_BIKE = "<circle cx='5.5' cy='17.5' r='3.5'/><circle cx='18.5' cy='17.5' r='3.5'/><path d='M5.5 17.5 L9.5 9 L18.5 17.5'/><path d='M9.5 9 L15 9'/>"
ICON_FLAG = "<line x1='4' y1='22' x2='4' y2='2'/><path d='M4 4h16l-3 6 3 6H4'/>"
ICON_SUN = "<circle cx='12' cy='12' r='4'/><path d='M12 2v2M12 20v2M4 12H2M22 12h-2M5 5l1.5 1.5M17.5 17.5L19 19M5 19l1.5-1.5M17.5 6.5L19 5'/>"
ICON_USERS = "<path d='M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2'/><circle cx='9' cy='7' r='4'/><path d='M23 21v-2a4 4 0 0 0-3-3.87'/><path d='M16 3.13a4 4 0 0 1 0 7.75'/>"


def sights_html(sights):
    return "\n".join(f"""        <div class="sight-row">
          <h3>{name}</h3>
          <p>{text}</p>
        </div>""" for name, text in sights)


def day_blocks_html(blocks):
    return "\n".join(f"""        <div class="day-block-item">
          <h3>{name}</h3>
          <p>{text}</p>
        </div>""" for name, text in blocks)


def info_list_html(items, css_class):
    lis = "\n".join(f"            <li>{i}</li>" for i in items)
    return f'          <ul class="info-list {css_class}">\n{lis}\n          </ul>'


def itinerary_html(stops):
    rows = []
    for i, (name, time_label, text) in enumerate(stops, 1):
        rows.append(f"""        <div class="itinerary-day">
          <div class="itinerary-day-badge">{i}</div>
          <div class="itinerary-day-content">
            <p class="itinerary-day-time">{time_label}</p>
            <h3>{name}</h3>
            <p>{text}</p>
          </div>
        </div>""")
    return "\n".join(rows)


def related_html(related):
    return "\n".join(f"""        <a href="/{r['href']}" class="related-card">
          <img src="{r['img']}" alt="{r['name']}" loading="lazy" />
          <div class="related-card-body">
            <p class="related-card-name">{r['name']}</p>
            <p class="related-card-meta">{r['meta']}</p>
          </div>
        </a>""" for r in related)


def rich_page(t):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{GTAG}
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="icon" type="image/x-icon" href="Favicons/favicon.ico" />
  <link rel="icon" type="image/png" sizes="32x32" href="Favicons/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="Favicons/favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="Favicons/apple-touch-icon.png" />
  <meta name="description" content="{t['meta_desc']}" />
  <title>{t['name']} | Tandro Bikes Georgia</title>

{LOCALBUSINESS_LD}
{breadcrumb_ld(t['name'], t['slug'])}
  <link rel="canonical" href="https://www.tandrobikes.com/{t['slug']}" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@400;600;700&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet" />

  <style>{HEAD_CSS}
{EXTRA_CSS}
    .page-header-bg {{ background-image: url('{t['hero_img']}'); }}
  </style>
</head>
<body>
{NAV_HTML}
  <!-- PAGE HEADER -->
  <section id="page-header">
    <div class="page-header-bg"></div>
    <div class="page-header-overlay"></div>
    <div class="page-header-inner">
      <p class="page-header-breadcrumb"><a href="/">Home</a> / <a href="/tours">Tours</a> / {t['name']}</p>
      <div class="page-header-meta">
        <span class="tour-badge badge-duration">{t['duration']}</span>
        <span class="tour-badge {t['badge_class']}">{t['difficulty']}</span>
      </div>
      <h1 class="page-header-title">{t['title_html']}</h1>
      <p class="page-header-sub">{t['sub']}</p>
      <div class="page-header-ctas">
        <a href="{wa_link(t['wa_text'])}" target="_blank" rel="noopener" class="btn-whatsapp">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
          {t['cta_label']}
        </a>
      </div>
    </div>
  </section>

  <!-- INTRO -->
  <section class="tour-detail-section" style="padding-bottom: 0;">
    <div class="container">
      <p class="tour-description" style="font-size:17px;">{t['intro']}</p>
      <div class="trip-facts">
{facts_html(t['facts'])}
      </div>
    </div>
  </section>

  <!-- WHAT YOU'LL SEE / HIGHLIGHTS -->
  <section>
    <div class="container">
      <p class="section-label">{t['sights_label']}</p>
      <h2 class="section-title">{t['sights_title']}</h2>
      <div class="sights-list">
{sights_html(t['sights'])}
      </div>
    </div>
  </section>

  <!-- HOW THE DAY WORKS -->
  <section style="background: var(--surface); padding-bottom: 56px;">
    <div class="container">
      <p class="section-label">Good to Know</p>
      <h2 class="section-title">How the Day Works</h2>
      <div class="day-block">
{day_blocks_html(t['day_blocks'])}
      </div>
      <p class="tour-description" style="margin-top:28px;">{t['fit_text']}</p>
      {t.get('not_suitable_html', '')}
    </div>
  </section>

  <!-- ITINERARY -->
  <section>
    <div class="container">
      <p class="section-label">Route</p>
      <h2 class="section-title">Itinerary</h2>
      <div class="itinerary-timeline">
{itinerary_html(t['itinerary'])}
      </div>
    </div>
  </section>

  <!-- WHAT'S INCLUDED / WHAT TO BRING -->
  <section style="background: var(--surface);">
    <div class="container">
      <div class="info-columns">
        <div>
          <p class="info-col-title">What's Included</p>
{info_list_html(t['included'], 'check')}
        </div>
        <div>
          <p class="info-col-title">What to Bring</p>
{info_list_html(t['bring'], 'pack')}
        </div>
      </div>
      {t.get('info_note', '')}
      {t.get('meeting_html', '')}
    </div>
  </section>

  <!-- BOOKING CTA -->
  <section>
    <div class="container">
      <div class="booking-box">
        <h2 class="booking-box-title">{t['booking_title']}</h2>
        <p class="booking-box-text">{t['booking_text']}</p>
        <a href="{wa_link(t['wa_text'])}" target="_blank" rel="noopener" class="btn-whatsapp">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
          {t['cta_label']}
        </a>
      </div>
    </div>
  </section>

  <!-- RELATED TOURS -->
  <section class="related-section">
    <div class="container">
      <p class="section-label">More Rides</p>
      <h2 class="section-title">You Might Also Like</h2>
      <div class="related-grid">
{related_html(t['related'])}
      </div>
    </div>
  </section>
{FOOTER_HTML}
{SCRIPTS_HTML}
</body>
</html>
"""
    return html


if __name__ == "__main__":
    print("module loaded")
