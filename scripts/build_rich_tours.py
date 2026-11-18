# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_rich_tours import rich_page, ICON_CLOCK, ICON_MAP, ICON_BIKE, ICON_FLAG, ICON_SUN, ICON_USERS
from gen_tour_pages import BASE

TOURS = [
    # ===================== TRUSO VALLEY =====================
    dict(
        slug="truso-valley-tour",
        name="Truso Valley Bike Tour",
        meta_desc="A private mountain bike or e-bike day tour into Truso Valley from Tbilisi or Kazbegi — mineral terraces, stone villages and Zakagori Fortress.",
        duration="Full Day", difficulty="Moderate", badge_class="badge-moderate",
        hero_img="Images/Turso Valley to use.jpeg",
        title_html="Truso Valley<br><span>Bike Tour</span>",
        sub="White mineral terraces, red-stained springs, old stone villages and a fortress above the river — a private ride from Tbilisi or Kazbegi.",
        cta_label="Book This Tour",
        intro="A private mountain bike or e-bike tour from Tbilisi or Kazbegi. White mineral terraces, red-stained springs, old stone villages and a fortress above the river — Truso has a surprising amount to see in one valley, and a bike lets you cover more of it. Our route follows the Tergi River through a narrow gorge and into the open valley, passing mineral springs and the villages of Ketrisi and Abano on the way towards Zakagori Fortress. You can join us from Tbilisi with return transfers, or start locally if you are already staying in the Kazbegi area.",
        facts=[
            (ICON_USERS, "Tour Type", "Private guided day tour"),
            (ICON_MAP, "Starting Options", "Tbilisi or the Kazbegi area, by arrangement"),
            (ICON_BIKE, "Cycling Distance", "Approx. 25–35 km, depending on preference"),
            (ICON_CLOCK, "Cycling Time", "Approx. 3–4 hours, plus sightseeing and breaks"),
            (ICON_CLOCK, "Total Duration", "A full day from Tbilisi"),
            (ICON_FLAG, "Difficulty", "Moderate — confidence on uneven gravel is needed"),
            (ICON_BIKE, "Surface &amp; Bikes", "Mostly gravel and dirt tracks · MTB or E-bike"),
            (ICON_SUN, "Season", "Usually late May – October, weather dependent"),
        ],
        sights_label="Truso Valley",
        sights_title="What You'll See",
        sights=[
            ("The Gorge and the Open Valley", "The scenery changes as we ride. The road follows the river into the narrow Kasari gorge, with steep rock walls beside it. Further in, the gorge opens into mountain fields. From here, you can see much further up the valley, with the river flowing and old settlements ahead."),
            ("Truso's Mineral Springs and Travertines", "Some of Truso's most unusual sights are right beside the track. Mineral-rich water flows over the ground and leaves deposits behind, building terraces and coloring patches orange and red. These formations are called travertines, and some are protected natural monuments. We'll stop near to have a better look."),
            ("Ketrisi and Abano", "Ruined houses, stone walls and towers show how much life there once was here. Many buildings now stand empty, although the valley still has seasonal residents and religious communities. Riding through these settlements gives the day another side beyond the scenery: you see the remains of mountain villages."),
            ("Abano Mineral Lake", "This small lake is easy to miss if you only follow the main vehicle track. Gas rises through the water, sending bubbles to the surface. When possible, we'll leave the bikes and approach for a look. We follow the guide's instructions, keep back from the edge and stay out of the water."),
            ("Zakagori Fortress", "Further up, the stone ruins of Zakagori stand on a hill above the river. The fortress area is our planned turnaround point, with time to take in the view before riding back. There is a border-police post nearby, and access depends on their instructions. Our standard tour does not continue into the restricted upper valley."),
        ],
        day_blocks=[
            ("Starting from Tbilisi", "We leave in the morning and travel along the military highway towards Kobi. The drive is about three hours each way, depending on traffic and road conditions. At the agreed starting point, we set up the bikes, go through the route and begin riding into Truso."),
            ("Already Staying in Kazbegi?", "We can bring the bikes and guide to the area and arrange your transfer to the starting point and back. Tell us where you are staying when you enquire, and we will confirm the meeting point, timing and price."),
        ],
        fit_text="<strong>Is this ride right for you?</strong> You should be comfortable cycling on gravel, braking on descents and riding over loose stones. The standard route follows valley tracks, but uneven surfaces and short climbs still require some effort. You can walk any section you are uncomfortable riding. A mountain bike suits regular cyclists with reasonable fitness. An e-bike reduces the pedalling effort and can be a good choice for riders who want a more relaxed pace. However, both options require confident bike handling.",
        itinerary=[
            ("Depart Tbilisi", "Morning", "We travel along the Georgian Military Highway towards Kobi, roughly three hours depending on traffic and road conditions."),
            ("Bike Setup &amp; Route Briefing", "On Arrival", "At the agreed starting point we set up the bikes, go through the route and begin riding into Truso."),
            ("Kasari Gorge", "En Route", "The road follows the Tergi River into the narrow gorge before opening into mountain fields."),
            ("Mineral Springs &amp; Travertines", "En Route", "A stop beside the track to see Truso's orange and red mineral terraces up close."),
            ("Ketrisi &amp; Abano Villages", "Mid-Ride", "Riding through the ruined stone houses and towers of these seasonal mountain settlements."),
            ("Abano Mineral Lake", "Mid-Ride", "An optional stop on foot to see the bubbling mineral lake, approached carefully on the guide's instructions."),
            ("Zakagori Fortress", "Turnaround Point", "The stone ruins above the river mark our planned turnaround, with time to take in the view."),
            ("Ride Back &amp; Return Transfer", "Afternoon", "We retrace the route back to the vehicle and transfer back towards Tbilisi or your Kazbegi accommodation."),
        ],
        included=[
            "A local English-speaking cycling guide",
            "A mountain bike or e-bike, as booked",
            "A helmet",
            "Bike transportation",
            "Transfers as agreed",
        ],
        bring=[
            "Passport",
            "Comfortable cycling/sport clothes and shoes with good grip",
            "A warm layer and a waterproof jacket",
            "Water, lunch and snacks",
            "Sunglasses",
            "A small backpack",
        ],
        info_note="<p class=\"info-note\">Meals, drinks and personal travel insurance are separate. Bring drinking water and a packed lunch or substantial snacks — food stops in the valley are seasonal. Mountain weather can change quickly, including in summer; we confirm access and riding conditions before departure and adjust the route if necessary.</p>",
        booking_title="Book Your Truso Valley Bike Tour",
        booking_text="Send us your preferred date, group size, starting location, bike choice and each rider's height. For e-bikes, please also include rider weights. We will confirm the route, available bikes and total price for your group. Your reservation is confirmed after prepayment.",
        wa_text="Hi%2C+I%27d+like+to+book+the+Truso+Valley+Bike+Tour!",
        related=[
            dict(name="Juta–Sno Bike Tour", href="juta-sno-tour", img="Images/Juta Image to use for tours.jpeg", meta="Full Day · Moderate"),
            dict(name="Kazbegi &amp; Gudauri — 7-Day Tour", href="kazbegi-bike-tour", img="Images/Kazbegi Tour 1.jpeg", meta="7 Days · Challenging"),
            dict(name="Gwaldi Pass E-Bike Adventure", href="gwaldi-pass-tour", img="Images/gwaldi-pass-ebike-adventure.jpeg", meta="3–4h · Challenging"),
        ],
    ),

    # ===================== JUTA-SNO =====================
    dict(
        slug="juta-sno-tour",
        name="Juta–Sno Bike Tour",
        meta_desc="A private mountain bike or e-bike day tour from Tbilisi or Kazbegi through Juta and Sno — Chaukhi peaks, stone sculptures and Sno Fortress.",
        duration="Full Day", difficulty="Moderate", badge_class="badge-moderate",
        hero_img="Images/Juta Image to use for tours.jpeg",
        title_html="Juta–Sno<br><span>Bike Tour</span>",
        sub="High mountain villages, the sharp peaks of Chaukhi, and giant stone faces standing in a field — a private ride from Tbilisi or Kazbegi.",
        cta_label="Book This Tour",
        intro="A private mountain bike or e-bike tour from Tbilisi or Kazbegi. High mountain villages, the sharp peaks of Chaukhi and giant stone faces standing in a field. This ride connects Juta and Sno through a river valley, with mountain scenery and village stops along the way. Our route follows the valley road between Sno and Juta, passing small settlements, open slopes and rocky sections above the river. You can join us from Tbilisi with return transfers, or start locally if you are already staying in the Kazbegi area.",
        facts=[
            (ICON_USERS, "Tour Type", "Private guided day tour"),
            (ICON_MAP, "Starting Options", "Tbilisi or the Kazbegi area, by arrangement"),
            (ICON_BIKE, "Cycling Distance", "Approx. 15–30 km, depending on preference and transfers"),
            (ICON_CLOCK, "Cycling Time", "Approx. 2–4 hours, plus sightseeing and breaks"),
            (ICON_CLOCK, "Total Duration", "A full day from Tbilisi"),
            (ICON_FLAG, "Difficulty", "Moderate — confidence on gravel and descents is needed"),
            (ICON_BIKE, "Surface &amp; Bikes", "Mixed asphalt and gravel · MTB or E-bike"),
            (ICON_SUN, "Season", "Usually June – October, weather dependent"),
        ],
        sights_label="Juta &amp; Sno Valley",
        sights_title="What You'll See",
        sights=[
            ("Juta Village", "Juta sits at around 2,200 metres, near the upper end of the valley. The village is a starting point for walks into the Chaukhi mountains, with houses and seasonal guesthouses on the slopes. We stop here before continuing with the riding."),
            ("The Chaukhi Mountains", "The pointy rock peaks of Chaukhi are there beyond Juta. If you would like to include a walk, we can leave the bikes and climb above the village towards the Fifth Season area for a better view. The first section is steep, and we agree the walking distance beforehand."),
            ("Sno Valley", "The road follows the river through small villages, including Karkucha, with open mountain slopes between them. Some parts are paved, while others are gravel and rougher track. There is time to stop along the way, and the balance of climbing and descending depends on the version of the ride you choose."),
            ("The Stone Heads of Sno", "Large faces carved from stone stand in a field near Sno. They are the work of local sculptor Merab Piranishvili, whose sculptures include portraits of Georgian poets and writers such as Shota Rustaveli and Ilia Chavchavadze."),
            ("Sno Fortress", "A stone tower and defensive wall stand on a rocky spot in the village. The fortress once helped protect the local population and control the routes through the valley. We stop nearby to see it from outside."),
        ],
        day_blocks=[
            ("Starting from Tbilisi", "We leave in the morning and travel along the military highway towards the Kazbegi region, then turn into Sno Valley — around 3.5–4 hours each way, depending on the starting point, traffic and road conditions. At the agreed starting point, we set up the bikes, go through the route and begin riding. The day includes stops in Sno and Juta, with an optional walk above Juta arranged beforehand."),
            ("Already Staying in Kazbegi?", "We can bring the bikes and guide to the area and arrange your transfer to the starting point and back. Tell us where you are staying when you enquire, and we will confirm the meeting point, timing and price."),
        ],
        fit_text="<strong>Is this ride right for you?</strong> You should be comfortable cycling on gravel, controlling your speed on descents and riding over loose stones. The road has bends, uneven sections and stretches shared with vehicles. You can walk any section you are uncomfortable riding. A mountain bike suits regular cyclists with reasonable fitness. An e-bike is a good option if your route includes more climbing or you would prefer less pedalling effort. However, both options require confident bike handling.",
        itinerary=[
            ("Depart Tbilisi", "Morning", "Along the Georgian Military Highway towards Kazbegi, then into Sno Valley — around 3.5–4 hours each way."),
            ("Bike Setup &amp; Route Briefing", "On Arrival", "At the agreed starting point we set up the bikes, go through the route and begin riding."),
            ("Sno Valley Villages", "En Route", "Riding past Karkucha and other small settlements along the river, on mixed asphalt and gravel."),
            ("Stone Heads of Sno", "Mid-Ride", "A stop at the field of carved stone faces by sculptor Merab Piranishvili."),
            ("Sno Fortress", "Mid-Ride", "Viewing the stone tower and defensive wall from outside."),
            ("Juta Village", "Upper Valley", "Arrival at Juta, around 2,200m, below the Chaukhi peaks — with an optional walk above the village."),
            ("Ride Back &amp; Return Transfer", "Afternoon", "Retracing the valley road back to the vehicle and transferring towards Tbilisi or your Kazbegi accommodation."),
        ],
        included=[
            "A local English-speaking cycling guide",
            "A mountain bike or e-bike, as booked",
            "A helmet",
            "Bike transportation",
            "Transfers as agreed",
        ],
        bring=[
            "Passport or ID",
            "Comfortable cycling/sport clothes and shoes with good grip",
            "A warm layer and a waterproof jacket",
            "Water, lunch and snacks",
            "Sunglasses",
            "A small backpack",
        ],
        info_note="<p class=\"info-note\">Meals, drinks and personal travel insurance are separate. Bring drinking water and a packed lunch or substantial snacks — cafés in Juta are seasonal. Mountain weather can change quickly, including in summer, and the road towards Juta can also be affected by landslides and roadworks. We confirm safe, permitted access before booking and check conditions again before departure.</p>",
        booking_title="Book Your Juta–Sno Bike Tour",
        booking_text="Send us your preferred date, group size, starting location, bike choice and each rider's height. For e-bikes, please also include rider weights. We will confirm the route, available bikes and total price for your group. Your reservation is confirmed after prepayment.",
        wa_text="Hi%2C+I%27d+like+to+book+the+Juta%E2%80%93Sno+Bike+Tour!",
        related=[
            dict(name="Truso Valley Bike Tour", href="truso-valley-tour", img="Images/Turso Valley to use.jpeg", meta="Full Day · Moderate"),
            dict(name="Kazbegi &amp; Gudauri — 7-Day Tour", href="kazbegi-bike-tour", img="Images/Kazbegi Tour 1.jpeg", meta="7 Days · Challenging"),
            dict(name="Gwaldi Pass E-Bike Adventure", href="gwaldi-pass-tour", img="Images/gwaldi-pass-ebike-adventure.jpeg", meta="3–4h · Challenging"),
        ],
    ),

    # ===================== KUTAISI CITY CENTER (GetYourGuide style) =====================
    dict(
        slug="kutaisi-city-center-tour",
        name="Kutaisi Bike Tour: City Center, History &amp; Riverside Paths",
        meta_desc="A 2-hour guided bike tour of Kutaisi — the Colchis Fountain, the White Bridge, riverside settlements and the option to climb to Bagrati Cathedral.",
        duration="2 Hours", difficulty="Easy", badge_class="badge-easy",
        hero_img="Images/Kutaisi City Ride Image.jpg",
        title_html="Kutaisi Bike Tour<br><span>City Center &amp; Riverside</span>",
        sub="Explore Georgia's oldest city in a unique and memorable way: by bike. Ride through its fascinating landmarks and view the city from a fresh perspective.",
        cta_label="Check Availability",
        intro="Ready to pedal through history? This fun, active, and informative ride allows you to cover a lot, while diving deep into Kutaisi's culture, history, and charm. It's perfect for all fitness levels. A friendly, knowledgeable local guide brings the city's stories to life as you ride past its most iconic landmarks and hidden gems — with the option to climb a gentle hill to the UNESCO-listed Bagrati Cathedral.",
        facts=[
            (ICON_CLOCK, "Duration", "2 hours"),
            (ICON_USERS, "Group Size", "Minimum 2 people per booking · private groups available"),
            (ICON_FLAG, "Guide", "Live, English-speaking local guide"),
            (ICON_SUN, "Cancellation", "Free cancellation up to 24 hours in advance"),
        ],
        sights_label="Kutaisi",
        sights_title="What You'll Cycle Past",
        sights=[
            ("The Heart of Imereti", "The city center and the golden Colchis Fountain — the pulse of Kutaisi."),
            ("Cultural Icons", "The beautiful, historic Meskhishvili Theater and the Opera Hall."),
            ("Photo Opportunities", "Cross the famous iconic White Bridge and the Rustaveli Bridge, capturing beautiful river and mountain views."),
            ("Local Life", "Discover the city's oldest educational institutions, the 1st and 3rd Public Schools, and the Rioni riverside settlements."),
            ("Engineering Marvel", "View the impressive Soviet-era architecture of the Gumati Water Dam."),
            ("Optional Ascent — Bagrati Cathedral (UNESCO)", "Choose to climb a gentle hill, only 1 km from the center, to visit the breathtaking 11th-century Bagrati Cathedral, a magnificent UNESCO World Heritage monument with stunning city views."),
        ],
        day_blocks=[
            ("Your Local Expert", "A friendly, knowledgeable local guide brings Kutaisi's history and stories to life, making sure you're comfortable, safe, and enjoying every moment of your active exploration."),
            ("Starting &amp; Ending Point", "The tour conveniently starts and ends at Hotel Terrace Kutaisi — easy to find and reach."),
        ],
        fit_text="<strong>Is this ride right for you?</strong> This relaxed, flat city ride is designed for all fitness levels, with gentle pacing and plenty of stops. The optional climb to Bagrati Cathedral is a short, gentle hill only 1 km from the center.",
        itinerary=[
            ("Hotel Terrace Kutaisi", "Starting Location", "Meet your guide and bike at the starting point."),
            ("Colchis Fountain", "~20 min", "A ride through the city center to Kutaisi's golden landmark fountain."),
            ("White Bridge, Kutaisi", "~20 min", "Crossing the iconic bridge for river and mountain views."),
            ("Gumati 1 HPP", "~40 min", "Riding along the riverside to view the Soviet-era hydroelectric dam."),
            ("Secret Stop", "~20 min", "A local, off-the-guidebook spot your guide will share along the way."),
            ("Bagrati Cathedral (Optional)", "~40 min", "A gentle climb to the 11th-century UNESCO cathedral, before returning to Hotel Terrace Kutaisi."),
        ],
        included=[
            "A bike for each person",
            "Local guide services",
        ],
        bring=[
            "Comfortable clothes and closed-toe shoes",
            "Water bottle",
            "Sunglasses &amp; sun protection",
            "Camera or phone for photos",
        ],
        info_note="<p class=\"info-note\">Not suitable for people over 250 lbs (113 kg) or over 80 years. Alcohol and drugs are not permitted during the tour.</p>",
        not_suitable_html="<div class=\"not-suitable\"><span>Not suitable: over 250 lbs (113 kg)</span><span>Not suitable: over 80 years</span><span>Not allowed: alcohol &amp; drugs</span></div>",
        meeting_html="<div class=\"meeting-box\"><p class=\"meeting-box-title\">Meeting Point</p><p class=\"meeting-box-text\">Hotel Terrace Kutaisi — 10/26 May II All., Kutaisi 4600, Georgia. The tour both starts and ends here.</p></div>",
        booking_title="Book Your Kutaisi City Bike Tour",
        booking_text="Message us on WhatsApp with your preferred date and group size (minimum 2 people) to check availability. Private groups can also be arranged.",
        wa_text="Hi%2C+I%27d+like+to+book+the+Kutaisi+City+Center+%26+Riverside+bike+tour!",
        related=[
            dict(name="Kutaisi City Ride", href="kutaisi-city-ride-tour", img="Images/Kutaisi City Ride Image.jpg", meta="2–3h · Easy"),
            dict(name="Winery Tour", href="winery-tour", img="Images/Winery Tour image.jpeg", meta="4–5h · Easy"),
            dict(name="Tskaltubo Tour", href="tskaltubo-tour", img="Images/Tskaltubo Tour.jpeg", meta="3h · Easy"),
        ],
    ),
]

if __name__ == "__main__":
    for t in TOURS:
        out_path = os.path.join(BASE, f"{t['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(rich_page(t))
        print("wrote", out_path)
