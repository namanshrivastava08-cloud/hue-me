import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Hue & Me",
    page_icon="🎨",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    scroll-behavior: smooth;
}

.main {
    background-color: #fffaf7;
}

.hero {
    background: linear-gradient(135deg,#fff4ef,#ffe8f0);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    margin-bottom: 40px;
}

.hero-title {
    font-size: 55px;
    font-weight: 700;
    color: #8b5e3c;
}

.hero-tagline {
    font-size: 24px;
    color: #444;
    margin-top: -10px;
}

.section-title {
    font-size: 38px;
    font-weight: bold;
    color: #7a3e3e;
    margin-top: 40px;
    margin-bottom: 20px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.package-card {
    background: linear-gradient(135deg,#fff0f5,#fffaf0);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.07);
}

.footer {
    text-align:center;
    padding:30px;
    color:gray;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "✨ Navigate",
    [
        "Home",
        "Body Type",
        "Skin Undertone",
        "Packages",
        "Appointment Booking",
        "About Us"
    ]
)

# ---------------- HOME ----------------
if menu == "Home":

    st.markdown("""
    <div class="hero">
        <img src="https://i.imgur.com/u8VQZ4T.png" width="220">
        <div class="hero-title">Hue & Me</div>
        <div class="hero-tagline">
            Because every you has a perfect hue ✨
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "/mnt/data/WhatsApp Image 2026-05-22 at 7.53.55 PM.jpeg",
        use_container_width=True
    )

    st.markdown('<div class="section-title">Welcome to Hue & Me</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    Fashion isn’t just about what you wear — it’s about how your colors tell your story.<br><br>

    At <b>Hue & Me</b>, our curiosity about colors and creativity in styling come together to help you discover the shades that truly belong to you.<br><br>

    From understanding your personal color palette to building a style that reflects your personality, we transform fashion into a journey of self-expression.<br><br>

    <b>Because the right hue doesn’t just change your outfit — it changes how you feel.</b>
    </div>
    """, unsafe_allow_html=True)

# ---------------- BODY TYPE ----------------
elif menu == "Body Type":

    st.markdown('<div class="section-title">Find Your Body Type</div>', unsafe_allow_html=True)

    st.write("""
Every body is unique, but most shapes fall into a few common categories.
Knowing your body type helps you choose clothes that fit better, flatter your shape, and boost confidence.
""")

    st.image(
        "/mnt/data/WhatsApp Image 2026-03-09 at 5.57.32 PM.jpeg",
        use_container_width=True
    )

    st.markdown("---")

    # Hourglass
    st.markdown("""
    <div class="card">
    <h3>1️⃣ Hourglass</h3>

    <b>Criteria</b>
    <ul>
    <li>Bust and hips are almost the same width</li>
    <li>Waist is clearly defined and smaller</li>
    <li>Curves are balanced</li>
    </ul>

    <b>Style Tip:</b><br>
    Fitted dresses, wrap tops, and high-waist bottoms highlight your natural shape.
    </div>
    """, unsafe_allow_html=True)

    # Pear
    st.markdown("""
    <div class="card">
    <h3>2️⃣ Pear (Triangle)</h3>

    <b>Criteria</b>
    <ul>
    <li>Hips are wider than shoulders</li>
    <li>Waist is defined</li>
    <li>Upper body is narrower</li>
    </ul>

    <b>Style Tip:</b><br>
    Statement tops, structured shoulders, and darker bottoms balance the body.
    </div>
    """, unsafe_allow_html=True)

    # Apple
    st.markdown("""
    <div class="card">
    <h3>3️⃣ Apple (Round)</h3>

    <b>Criteria</b>
    <ul>
    <li>Upper body is broader</li>
    <li>Waist is less defined</li>
    <li>Weight is more around the stomach area</li>
    </ul>

    <b>Style Tip:</b><br>
    Flowy tops, V-necks, and A-line dresses create a balanced silhouette.
    </div>
    """, unsafe_allow_html=True)

    # Rectangle
    st.markdown("""
    <div class="card">
    <h3>4️⃣ Rectangle (Straight)</h3>

    <b>Criteria</b>
    <ul>
    <li>Bust, waist, and hips are almost equal</li>
    <li>Minimal curves</li>
    <li>Straight body structure</li>
    </ul>

    <b>Style Tip:</b><br>
    Layering, belts, and peplum styles help create curves.
    </div>
    """, unsafe_allow_html=True)

    # Inverted Triangle
    st.markdown("""
    <div class="card">
    <h3>5️⃣ Inverted Triangle</h3>

    <b>Criteria</b>
    <ul>
    <li>Shoulders are broader than hips</li>
    <li>Narrow lower body</li>
    <li>Athletic upper frame</li>
    </ul>

    <b>Style Tip:</b><br>
    Wide-leg pants, A-line skirts, and minimal shoulder detail balance proportions.
    </div>
    """, unsafe_allow_html=True)

# ---------------- SKIN UNDERTONE ----------------
elif menu == "Skin Undertone":

    st.markdown('<div class="section-title">Find Your Skin Undertone ✨</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <h3>01 — The Vein Test</h3>

    Blue or purple veins → <b>Cool undertone</b><br>
    Green veins → <b>Warm undertone</b><br>
    A mix of both → <b>Neutral undertone</b>

    <br><br>

    <h3>02 — The Jewelry Test</h3>

    Silver looks better → <b>Cool undertone</b><br>
    Gold looks better → <b>Warm undertone</b><br>
    Both look great → <b>Neutral undertone</b>

    <br><br>

    <h3>03 — The Sun Test</h3>

    Burns easily → <b>Cool undertone</b><br>
    Tans easily → <b>Warm undertone</b><br>
    Burns then tans → <b>Neutral undertone</b>

    </div>
    """, unsafe_allow_html=True)

# ---------------- PACKAGES ----------------
elif menu == "Packages":

    st.markdown('<div class="section-title">Our Packages</div>', unsafe_allow_html=True)

    packages = {
        "Hue Starter":
        "Basic body type analysis, skin undertone identification, and basic color suggestions.",

        "Hue Discovery":
        "Personal color palette analysis, body type analysis, and outfit suggestions based on your features.",

        "Style & Hue Package":
        "Complete color analysis, body shape analysis, and personalized styling recommendations.",

        "Wardrobe Glow-Up":
        "Closet evaluation, outfit combinations, and guidance on building a versatile wardrobe.",

        "Complete 360° Hue Experience":
        "Full fashion analysis including color palette, body type, personal style report, and occasion-based styling tips."
    }

    for name, desc in packages.items():
        st.markdown(f"""
        <div class="package-card">
        <h3>{name}</h3>
        <p>{desc}</p>
        <b>💫 Price on Request</b>
        </div>
        """, unsafe_allow_html=True)

# ---------------- APPOINTMENT ----------------
elif menu == "Appointment Booking":

    st.markdown('<div class="section-title">Book Your Appointment</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    Upload your image and share your styling query with us.
    </div>
    """, unsafe_allow_html=True)

    name = st.text_input("Full Name")
    phone = st.text_input("Contact Number")
    query = st.text_area("Your Query")

    st.subheader("📸 Upload or Take a Photo")

    photo = st.camera_input("Take a Photo")
    upload = st.file_uploader("Upload an Image", type=["jpg","png","jpeg"])

    if st.button("Submit Appointment"):

        if name and phone:
            st.success("✨ Appointment request submitted successfully!")
        else:
            st.error("Please fill all required details.")

# ---------------- ABOUT ----------------
elif menu == "About Us":

    st.markdown('<div class="section-title">About Us</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    At <b>Hue & Me</b>, we believe style begins with understanding yourself.<br><br>

    Our platform helps you discover the colors, shapes, and styles that naturally complement who you are.<br><br>

    Instead of chasing trends, we focus on helping you build a look that feels authentic, confident, and effortless.<br><br>

    Every person carries a unique palette — sometimes it just needs the right place to be discovered.<br><br>

    <b>Hue & Me is that place.</b>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <h3>📩 Connect With Us</h3>

    Email: hello@hueandme.com <br><br>

    Instagram: @hueandme <br><br>

    Website: www.hueandme.com

    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
Because somewhere between a shade and a style, you’ll find the hue that feels like you ✨
</div>
""", unsafe_allow_html=True)
