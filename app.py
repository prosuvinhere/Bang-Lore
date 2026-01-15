import streamlit as st
import pandas as pd
import plotly.express as px
import io  # <--- Added this import to fix the error

# Page Configuration
st.set_page_config(
    page_title="The Most Unnecessary Bangalore Trip",
    page_icon="🍺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for the "Vibe" ---
st.markdown("""
<style>
    .big-font { font-size:30px !important; font-weight: bold; color: #FF4B4B; }
    .quote-box { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #FF4B4B; }
    .stMetric { background-color: #ffffff; border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
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
st.sidebar.info("**Dates:** Jan 23-27, 2026\n\n**Location:** Bangalore (Sarthak's PG)")

# ==========================================
# PAGE: HOME & LORE
# ==========================================
if page == "Home & Lore":
    st.title("The Most Unnecessary Bangalore Trip Presentation You'll Ever See")
    st.caption("Because regular invites are too mainstream")
    
    st.warning("⚠️ URGENT: This could've been a text, but here we are with 60 slides instead. Buckle up.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Why Does This Exist?")
        st.write("""
        * **Option A:** We have too much free time.
        * **Option B:** We wanted to annoy you.
        * **Option C:** All of the above.
        """)
        
        st.markdown("### Scientifically Proven Fun Levels")
        c1, c2, c3 = st.columns(3)
        c1.metric("Chaos Probability", "98%", "Very High")
        c2.metric("Laughter Quotient", "87%", "Abs will hurt")
        c3.metric("Unforgettable", "100%", "Good Lore")

    with col2:
        st.subheader("The Secret Sauce")
        st.info("Good People + Bad Jokes + Great Food + Random Vibes + Lore")

    st.markdown("---")
    st.subheader("📜 Past Trip Highlights (The Lore)")
    st.markdown("We have zero boring moments since 1947. Here is the evidence:")
    
    with st.expander("Click to reveal the incidents"):
        st.write("""
        * **March 2023:** The Political Car Incident (Hari "accidentally" scratched a political car).
        * **March 2025:** Hari's First "Taste" (Cheers to new beginnings).
        * **April 2025:** The Infinite Bread Glitch (A culinary mystery).
        * **April 2025:** Legendary Brownboard Discovery (A sacred relic).
        * **Nov 2025:** The Balloon Mindf*ck (Peak non-verbal communication).
        * **General Status:** Shitfaced drunk every time & spending too much on arcades.
        """) #

# ==========================================
# PAGE: THE MASTERMINDS
# ==========================================
elif page == "The Masterminds":
    st.title("The Trio Nobody Asked For But Everyone's Stuck With")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Shreyansh", "Sarthak", "Hari", "Akshith", "Devayan"])
    
    with tab1:
        st.header("Shreyansh: The Logistics Guy 📅")
        st.write("**Role:** The Brains Behind the Operation.")
        st.write("He actually knows what's happening. Has spreadsheets for his spreadsheets.")
        st.error("**Superpowers:** Planning Obsession (bathroom breaks included), Budget Master (splits bills in 2 mins), Navigation Wizard.")
        st.write("Will send you 47 reminders just to be sure.")
        
    with tab2:
        st.header("Sarthak: The Designated Bartender 🍻")
        st.write("**Signature Phrase:** 'Chalo daru pite hai' (Let's go drink).")
        st.write("**Special Skills:** Spontaneity Level 1000. Plans are merely suggestions.")
        st.success("**Greatest Hits:** 'What if we just climb that?' & 'Trust me bro'. Finds places Google Maps doesn't know exist.")
        
    with tab3:
        st.header("Hari: The Adventure Architect 🧭")
        st.write("**Role:** Bangalore Navigator & Street Food Connoisseur.")
        st.write("One half of the 'Bakchod Duo'. Frequent expeditions have made him a local legend.")
        st.info("**Abilities:** Never uses GPS because he IS the GPS. Knows which tourist traps to avoid. Pro Yulu Rider (Questionable skills).")
        
    with tab4:
        st.header("Akshith: The Corporate Professional (Sort Of) 👔")
        st.write("**Attributes:** Vertically Challenged (not the highest in the room).")
        st.write("**Employment:** Works at Cognizant (claims it's prestigious).")
        st.warning("**Weakness:** Alcohol Tolerance -5. First to pass out. Claims he doesn't drink because 'Krishna ji sab dekh rahe hain'.")

    with tab5:
        st.header("Devayan: The Jump Scare 👻")
        st.write("**Role:** The Enigma We Can't Explain.")
        st.write("**Lore:** Indiranagar Enthusiast. Has 67 children in his basement (allegedly).")
        st.error("**Rumor:** Runs an illegal empire bigger than Pablo Escobar's.")

# ==========================================
# PAGE: THE ITINERARY
# ==========================================
elif page == "The Itinerary":
    st.title("The Grand Plan: 4 Days of Mayhem")
    st.caption("Carefully planned chaos by Shreyansh, random additions by Sarthak.")
    
    st.markdown("Here is where we will be causing chaos:")
    # Placeholder for map if you have one, otherwise just text
    st.write("📍 **Destination:** Bangalore, Karnataka") 

    d1, d2, d3, d4 = st.tabs(["Day 1 (Sat)", "Day 2 (Sun)", "Day 3 (Mon)", "Day 4 (Tue)"])
    
    with d1:
        st.subheader("Saturday, Jan 24th: Nature & Spirits")
        st.markdown("""
        * **Morning:** **Bannerghatta National Park**. Lions, tigers, and a Butterfly Park for the Instagram aesthetic.
        * **Evening:** Dinner (Location TBD by Hari). Dress code: Exhausted chic.
        * **Night:** Back to **Sarthak's PG** for drinks, dancing, and karaoke that will wake the neighbors.
        """)
        
    with d2:
        st.subheader("Sunday, Jan 25th: Unlock Inner Child")
        st.markdown("""
        * **Morning:** Recovery Mode. Sleep in. Hydrate.
        * **Afternoon:** **Play Arena**. Trampolines, VR, Laser Tag, and embarrassingly competitive cricket.
        * **Evening:** **Loco Bear**. Craft beers, wings, and pizzas.
        * **Late Night:** Church Street Walk vs. Koramangala Exploration. Vibe check under the Nariyal ke ped.
        """)
        
    with d3:
        st.subheader("Monday, Jan 26th: The Mysterious Day")
        st.write("This day is intentionally left flexible (Democracy in action). Options include:")
        
        opts = st.columns(2)
        with opts[0]:
            with st.expander("Option 1: Sophisticated Adults"):
                st.write("Cubbon Park & Museum. Morning walks and pretending we are cultured.")
            with st.expander("Option 2: Relaxing"):
                st.write("Lumbini Gardens. Boating and lake vibes.")
            with st.expander("Option 3: Food Crawl"):
                st.write("MTR Breakfast, Vidyarthi Bhavan Dosa, Indian Coffee House.")
        
        with opts[1]:
            with st.expander("Option 4: The Sarthak Special"):
                st.write("Nandi Hills Sunrise. Warning: Requires waking up at 4 AM.")
            with st.expander("Option 5: The Best Option"):
                st.write("Drink All Day. Continuous flow of liquid encouragement.")
        
        st.write("**Night:** Farewell Dinner & Sarthak's PG Shenanigans part 2.")
        
    with d4:
        st.subheader("Tuesday, Jan 27th: The Day of Reckoning")
        st.write("Going home. Shreyansh to Mumbai, Hari to Delhi. Sarthak stays put.")
        st.write("Post-trip depression begins immediately.")

# ==========================================
# PAGE: BUDGET & STATS
# ==========================================
elif page == "Budget & Stats":
    st.title("Data Analysis (Very Scientific) 📊")
    
    st.subheader("Estimated Budget Breakdown")
    
    # FIXED SECTION: Using io.StringIO instead of pd.compat.StringIO
    csv_data = """Category,Cost
Bannerghatta,800
Play Arena,2000
Food & Drinks,2000
Local Transport,1500
Flights,15000
Misc,5000
Alcohol,12000"""
    
    df = pd.read_csv(io.StringIO(csv_data)) # <--- Corrected method
    
    fig = px.bar(df, x='Cost', y='Category', orientation='h', title="Where the Money Goes", color='Category')
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Notice the priority on Alcohol and Flights.")

    st.markdown("---")
    st.subheader("SWOT Analysis")
    
    c1, c2 = st.columns(2)
    with c1:
        st.success("**Strengths:**\nAll the bakchodi we will do and lore for a lifetime.")
        st.error("**Weaknesses:**\nYour social battery, 2nd hand embarrassment.")
    with c2:
        st.info("**Opportunities:**\nCringe lore, new ways to waste money.")
        st.warning("**Threats:**\nAdulting, bank accounts, Monday reality.")

    st.markdown("### Cost-Benefit Analysis")
    st.write("**Costs:** Hard-earned money, Sleep schedule.")
    st.write("**Benefits:** LORE. (That's literally the whole point).")

# ==========================================
# PAGE: LOGISTICS & LEGAL
# ==========================================
elif page == "Logistics & Legal":
    st.title("The Fine Print 📝")
    
    st.subheader("Accommodation & Transport")
    st.write("**HQ:** Sarthak's PG (The Central Command).")
    st.write("**Transport:** Uber/Ola. We split costs fairly. Hari knows the routes.")
    
    st.markdown("---")
    st.subheader("What's Included vs Not Included")
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ **INCLUDED:**\n* Guaranteed Fun\n* Lore\n* Great Company (Intentional & Accidental)")
    with col2:
        st.error("❌ **NOT INCLUDED:**\n* Your Flights\n* Getting you home safely\n* Sarthak's Random Ideas\n* Monday Morning Regrets")
    
    st.markdown("---")
    st.subheader("⚖️ Legal Notices (Not Really)")
    st.write("""
    1. We are not responsible for your poor life choices, especially those made after 9 PM.
    2. Any resemblance to actual planning is purely coincidental.
    3. Side effects may include excessive laughter and inexplicable cravings for street food.
    4. By proceeding, you agree to waive all rights to complain about the weather.
    """)

# ==========================================
# PAGE: RSVP
# ==========================================
elif page == "RSVP":
    st.title("Are You In?")
    
    st.markdown("""
    ### How to RSVP
    1. **Text Shreyansh:** He needs to add you to the spreadsheet.
    2. **Join the Group Chat:** Where the chaos happens.
    3. **Show Up:** The ultimate RSVP.
    """)
    
    if st.button("I'M COMING! 🚀"):
        st.balloons()
        st.success("Welcome to the madness! Prepare for 4 days of mayhem.")
    
    st.markdown("---")
    st.subheader("FAQs")
    with st.expander("Is this serious?"):
        st.write("Yes, but also no.")
    with st.expander("Can I bring a friend?"):
        st.write("The more the merrier.")
    with st.expander("Is Sarthak's idea safe?"):
        st.write("Define 'safe'.")
    
    st.markdown("---")
    st.caption("Presentation by Shreyansh, Sarthak & Hari. See you Jan 23-27!")