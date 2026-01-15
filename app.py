import streamlit as st
import pandas as pd
import plotly.express as px
import io

# Page Configuration
st.set_page_config(
    page_title="The Most Unnecessary Bangalore Trip",
    page_icon="🍺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for the "Vibe" ---
# UPDATED: Removed the .stMetric white background style to match your dark mode screenshot.
st.markdown("""
<style>
    .big-font { 
        font-size:30px !important; 
        font-weight: bold; 
        color: #FF4B4B; 
    }
    
    /* Dark Mode Friendly Quote Box */
    .quote-box { 
        background-color: rgba(255, 255, 255, 0.1); 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 5px solid #FF4B4B; 
        color: white;
        margin-bottom: 20px;
    }
    
    /* Just adding a little spacing to metrics for better layout */
    div[data-testid="stMetric"] {
        padding: 10px 0px;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", [
    "Home & Lore", 
    "The Masterminds", 
    "The Itinerary", 
    "Budget & Stats", 
    "Logistics & Legal", 
    "RSVP"
])

st.sidebar.markdown("---")
[cite_start]st.sidebar.info("**Dates:** Jan 23-27, 2026\n\n**Location:** Bangalore (Sarthak's PG) [cite: 366]")

# ==========================================
# PAGE: HOME & LORE
# ==========================================
if page == "Home & Lore":
    [cite_start]st.title("The Most Unnecessary Bangalore Trip Presentation You'll Ever See [cite: 1]")
    [cite_start]st.caption("Because regular invites are too mainstream [cite: 3]")
    
    [cite_start]st.warning("⚠️ URGENT: This could've been a text, but here we are with 60 slides instead. Buckle up. [cite: 4-8]")

    col1, col2 = st.columns(2)
    
    with col1:
        [cite_start]st.subheader("Why Does This Exist? [cite: 9]")
        st.write("""
        * **Option A:** We have too much free time.
        * **Option B:** We wanted to annoy you.
        * [cite_start]**Option C:** All of the above. [cite: 10-15]
        """)
        
        [cite_start]st.markdown("### Scientifically Proven Fun Levels [cite: 121]")
        # These will now render in default dark mode style (White text on transparent bg)
        c1, c2, c3 = st.columns(3)
        [cite_start]c1.metric("Chaos Probability", "98%", "Very High") # [cite: 122, 125]
        [cite_start]c2.metric("Laughter Quotient", "87%", "Abs will hurt") # [cite: 123, 126, 129]
        [cite_start]c3.metric("Unforgettable", "100%", "Good Lore") # [cite: 124, 127, 130]

    with col2:
        [cite_start]st.subheader("The Secret Sauce [cite: 147]")
        [cite_start]st.info("Good People + Bad Jokes + Great Food + Random Vibes + Lore [cite: 149-153]")

    st.markdown("---")
    [cite_start]st.subheader("📜 Past Trip Highlights (The Lore) [cite: 98]")
    [cite_start]st.markdown("We have zero boring moments since 1947. Here is the evidence[cite: 97]:")
    
    with st.expander("Click to reveal the incidents"):
        st.write("""
        * [cite_start]**March 2023:** The Political Car Incident (Hari "accidentally" scratched a political car). [cite: 99-100]
        * [cite_start]**March 2025:** Hari's First "Taste" (Cheers to new beginnings). [cite: 105-106]
        * [cite_start]**April 2025:** The Infinite Bread Glitch (A culinary mystery). [cite: 101-102]
        * [cite_start]**April 2025:** Legendary Brownboard Discovery (A sacred relic). [cite: 103-104]
        * [cite_start]**Nov 2025:** The Balloon Mindf*ck (Peak non-verbal communication). [cite: 109-110]
        * [cite_start]**General Status:** Shitfaced drunk every time & spending too much on arcades. [cite: 111]
        """)

# ==========================================
# PAGE: THE MASTERMINDS
# ==========================================
elif page == "The Masterminds":
    [cite_start]st.title("The Trio Nobody Asked For But Everyone's Stuck With [cite: 19]")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Shreyansh", "Sarthak", "Hari", "Akshith", "Devayan"])
    
    with tab1:
        [cite_start]st.header("Shreyansh: The Logistics Guy 📅 [cite: 20-21]")
        [cite_start]st.write("**Role:** The Brains Behind the Operation. [cite: 22]")
        [cite_start]st.write("He actually knows what's happening. Has spreadsheets for his spreadsheets. [cite: 23, 27-28]")
        [cite_start]st.error("**Superpowers:** Planning Obsession (bathroom breaks included), Budget Master (splits bills in 2 mins), Navigation Wizard. [cite: 33-41]")
        [cite_start]st.write("Will send you 47 reminders just to be sure. [cite: 31-32]")
        
    with tab2:
        [cite_start]st.header("Sarthak: The Designated Bartender 🍻 [cite: 42-43]")
        [cite_start]st.write("**Signature Phrase:** 'Chalo daru pite hai' (Let's go drink). [cite: 45]")
        [cite_start]st.write("**Special Skills:** Spontaneity Level 1000. Plans are merely suggestions. [cite: 52-53]")
        [cite_start]st.success("**Greatest Hits:** 'What if we just climb that?' & 'Trust me bro'. Finds places Google Maps doesn't know exist. [cite: 47, 58-59]")
        
    with tab3:
        [cite_start]st.header("Hari: The Adventure Architect 🧭 [cite: 60-62]")
        [cite_start]st.write("**Role:** Bangalore Navigator & Street Food Connoisseur. [cite: 64, 67]")
        [cite_start]st.write("One half of the 'Bakchod Duo'. Frequent expeditions have made him a local legend. [cite: 63, 71]")
        [cite_start]st.info("**Abilities:** Never uses GPS because he IS the GPS. Knows which tourist traps to avoid. Pro Yulu Rider (Questionable skills). [cite: 74-76, 70]")
        
    with tab4:
        [cite_start]st.header("Akshith: The Corporate Professional (Sort Of) 👔 [cite: 77-78]")
        [cite_start]st.write("**Attributes:** Vertically Challenged (not the highest in the room). [cite: 80-81]")
        [cite_start]st.write("**Employment:** Works at Cognizant (claims it's prestigious). [cite: 82-83]")
        [cite_start]st.warning("**Weakness:** Alcohol Tolerance -5. First to pass out. Claims he doesn't drink because 'Krishna ji sab dekh rahe hain'. [cite: 85-88]")

    with tab5:
        [cite_start]st.header("Devayan: The Jump Scare 👻 [cite: 490]")
        [cite_start]st.write("**Role:** The Enigma We Can't Explain. [cite: 491]")
        [cite_start]st.write("**Lore:** Indiranagar Enthusiast. Has 67 children in his basement (allegedly). [cite: 492, 497-498]")
        [cite_start]st.error("**Rumor:** Runs an illegal empire bigger than Pablo Escobar's. [cite: 500-501]")

# ==========================================
# PAGE: THE ITINERARY
# ==========================================
elif page == "The Itinerary":
    [cite_start]st.title("The Grand Plan: 4 Days of Mayhem [cite: 156-157]")
    [cite_start]st.caption("Carefully planned chaos by Shreyansh, random additions by Sarthak. [cite: 159]")
    
    st.markdown("Here is where we will be causing chaos:")
    

[Image of Bangalore city map]

    st.write("📍 **Destination:** Bangalore, Karnataka") 

    d1, d2, d3, d4 = st.tabs(["Day 1 (Sat)", "Day 2 (Sun)", "Day 3 (Mon)", "Day 4 (Tue)"])
    
    with d1:
        [cite_start]st.subheader("Saturday, Jan 24th: Nature & Spirits [cite: 160-162]")
        st.markdown("""
        * [cite_start]**Morning:** **Bannerghatta National Park**. Lions, tigers, and a Butterfly Park for the Instagram aesthetic. [cite: 163-170]
        * **Evening:** Dinner (Location TBD by Hari). [cite_start]Dress code: Exhausted chic. [cite: 171-173]
        * [cite_start]**Night:** Back to **Sarthak's PG** for drinks, dancing, and karaoke that will wake the neighbors. [cite: 184-185]
        """)
        
    with d2:
        [cite_start]st.subheader("Sunday, Jan 25th: Unlock Inner Child [cite: 187-188]")
        st.markdown("""
        * [cite_start]**Morning:** Recovery Mode. Sleep in. Hydrate. [cite: 189-191]
        * **Afternoon:** **Play Arena**. [cite_start]Trampolines, VR, Laser Tag, and embarrassingly competitive cricket. [cite: 198-217]
        * **Evening:** **Loco Bear**. [cite_start]Craft beers, wings, and pizzas. [cite: 223-239]
        * **Late Night:** Church Street Walk vs. Koramangala Exploration. [cite_start]Vibe check under the Nariyal ke ped. [cite: 246-261]
        """)
        
    with d3:
        [cite_start]st.subheader("Monday, Jan 26th: The Mysterious Day [cite: 270-271]")
        [cite_start]st.write("This day is intentionally left flexible (Democracy in action). Options include: [cite: 273-279]")
        
        opts = st.columns(2)
        with opts[0]:
            with st.expander("Option 1: Sophisticated Adults"):
                [cite_start]st.write("Cubbon Park & Museum. Morning walks and pretending we are cultured. [cite: 280-284]")
            with st.expander("Option 2: Relaxing"):
                [cite_start]st.write("Lumbini Gardens. Boating and lake vibes. [cite: 286-287]")
            with st.expander("Option 3: The Food Crawl"):
                [cite_start]st.write("MTR Breakfast, Vidyarthi Bhavan Dosa, Indian Coffee House. [cite: 289-296]")
        
        with opts[1]:
            with st.expander("Option 4: The Sarthak Special"):
                [cite_start]st.write("Nandi Hills Sunrise. Warning: Requires waking up at 4 AM. [cite: 299-303]")
            with st.expander("Option 5: The Best Option"):
                [cite_start]st.write("Drink All Day. Continuous flow of liquid encouragement. [cite: 306-307]")
        
        [cite_start]st.write("**Night:** Farewell Dinner & Sarthak's PG Shenanigans part 2. [cite: 323-325]")
        
    with d4:
        [cite_start]st.subheader("Tuesday, Jan 27th: The Day of Reckoning [cite: 327-328]")
        [cite_start]st.write("Going home. Shreyansh to Mumbai, Hari to Delhi. Sarthak stays put. [cite: 330-331]")
        [cite_start]st.write("Post-trip depression begins immediately. [cite: 332]")

# ==========================================
# PAGE: BUDGET & STATS
# ==========================================
elif page == "Budget & Stats":
    [cite_start]st.title("Data Analysis (Very Scientific) 📊 [cite: 393]")
    
    [cite_start]st.subheader("Estimated Budget Breakdown [cite: 381]")
    
    # FIXED: Using io.StringIO instead of pd.compat.StringIO
    csv_data = """Category,Cost
Bannerghatta,800
Play Arena,2000
Food & Drinks,2000
Local Transport,1500
Flights,15000
Misc,5000
Alcohol,12000"""
    
    # [cite_start]Data derived from the chart on slide 55 [cite: 382-392]
    df = pd.read_csv(io.StringIO(csv_data))
    
    fig = px.bar(df, x='Cost', y='Category', orientation='h', title="Where the Money Goes", color='Category')
    st.plotly_chart(fig, use_container_width=True)
    [cite_start]st.caption("Notice the priority on Alcohol and Flights. [cite: 391-392]")

    st.markdown("---")
    [cite_start]st.subheader("SWOT Analysis [cite: 402]")
    
    c1, c2 = st.columns(2)
    with c1:
        [cite_start]st.success("**Strengths:**\nAll the bakchodi we will do and lore for a lifetime. [cite: 405]")
        [cite_start]st.error("**Weaknesses:**\nYour social battery, 2nd hand embarrassment. [cite: 407]")
    with c2:
        [cite_start]st.info("**Opportunities:**\nCringe lore, new ways to waste money. [cite: 410]")
        [cite_start]st.warning("**Threats:**\nAdulting, bank accounts, Monday reality. [cite: 409]")

    st.markdown("### Cost-Benefit Analysis")
    [cite_start]st.write("**Costs:** Hard-earned money, Sleep schedule. [cite: 394, 396]")
    [cite_start]st.write("**Benefits:** LORE. (That's literally the whole point). [cite: 395, 399, 401]")

# ==========================================
# PAGE: LOGISTICS & LEGAL
# ==========================================
elif page == "Logistics & Legal":
    [cite_start]st.title("The Fine Print 📝 [cite: 335]")
    
    [cite_start]st.subheader("Accommodation & Transport [cite: 364]")
    [cite_start]st.write("**HQ:** Sarthak's PG (The Central Command). [cite: 366-367]")
    [cite_start]st.write("**Transport:** Uber/Ola. We split costs fairly. Hari knows the routes. [cite: 369-370]")
    
    st.markdown("---")
    st.subheader("What's Included vs Not Included")
    col1, col2 = st.columns(2)
    with col1:
        [cite_start]st.success("✅ **INCLUDED:**\n* Guaranteed Fun\n* Lore\n* Great Company (Intentional & Accidental) [cite: 343-347]")
    with col2:
        [cite_start]st.error("❌ **NOT INCLUDED:**\n* Your Flights\n* Getting you home safely\n* Sarthak's Random Ideas\n* Monday Morning Regrets [cite: 350-363]")
    
    st.markdown("---")
    [cite_start]st.subheader("⚖️ Legal Notices (Not Really) [cite: 413]")
    st.write("""
    1. [cite_start]We are not responsible for your poor life choices, especially those made after 9 PM. [cite: 414-416]
    2. [cite_start]Any resemblance to actual planning is purely coincidental. [cite: 417-418]
    3. [cite_start]Side effects may include excessive laughter and inexplicable cravings for street food. [cite: 419-420]
    4. [cite_start]By proceeding, you agree to waive all rights to complain about the weather. [cite: 424-425]
    """)

# ==========================================
# PAGE: RSVP
# ==========================================
elif page == "RSVP":
    st.title("Are You In?")
    
    st.markdown("""
    ### [cite_start]How to RSVP [cite: 448]
    1. [cite_start]**Text Shreyansh:** He needs to add you to the spreadsheet. [cite: 452, 455]
    2. [cite_start]**Join the Group Chat:** Where the chaos happens. [cite: 453, 456]
    3. [cite_start]**Show Up:** The ultimate RSVP. [cite: 454, 457]
    """)
    
    if st.button("I'M COMING! 🚀"):
        st.balloons()
        st.success("Welcome to the madness! Prepare for 4 days of mayhem.")
    
    st.markdown("---")
    [cite_start]st.subheader("FAQs [cite: 435]")
    with st.expander("Is this serious?"):
        [cite_start]st.write("Yes, but also no. [cite: 436-437]")
    with st.expander("Can I bring a friend?"):
        [cite_start]st.write("The more the merrier. [cite: 442-443]")
    with st.expander("Is Sarthak's idea safe?"):
        [cite_start]st.write("Define 'safe'. [cite: 444-445]")
    
    st.markdown("---")
    [cite_start]st.caption("Presentation by Shreyansh, Sarthak & Hari. See you Jan 23-27! [cite: 486-488]")
