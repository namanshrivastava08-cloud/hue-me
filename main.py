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

html, body, [class*="css"]  {
    scroll-behavior: smooth;
    font-family: 'Poppins', sans-serif;
}

/* MAIN APP */

.stApp {
    background-color: #fffaf7;
}

/* CENTER IMAGE */

[data-testid="stImage"] {
    text-align: center;
}

/* HERO SECTION */

.hero {
    background: linear-gradient(135deg,#ffe9e3,#fff0f5);
    padding: 60px 40px;
    border-radius: 30px;
    margin-bottom: 60px;
    text-align: center;
}

.hero-title {
    font-size: 72px;
    font-weight: 700;
    color: #8a5238;
    margin-top: 15px;
    margin-bottom: 10px;
}

.hero-tagline {
    font-size: 28px;
    color: #444;
    margin-top: 0px;
}

/* CENTER STREAMLIT IMAGE */

[data-testid="stImage"] {
    text-align: center;
}


/* NAVBAR */

.navbar {
    text-align:center;
    margin-bottom:40px;
}

.navbar a {
    text-decoration:none;
    margin:15px;
    color:#7a3e3e !important;
    font-weight:bold;
    font-size:18px;
}

/* SECTION TITLES */

.section-title {
    font-size: 42px;
    font-weight: bold;
    color: #7a3e3e !important;
    margin-top: 50px;
    margin-bottom: 25px;
}

/* NORMAL CARD */

.card {
    background: white !important;
    color: #222 !important;
    padding: 30px;
    border-radius: 22px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* PACKAGE CARD */

.package-card {
    background: linear-gradient(135deg,#fff0f5,#fffaf0);
    color: #222 !important;
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 25px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

/* TEXT COLORS */

.card h3,
.card p,
.card li,
.card b,
.package-card h3,
.package-card p,
.package-card b {
    color: #222 !important;
}

/* GENERAL TEXT */

p, li, span, div {
    color: #222;
}

/* INPUTS */

input, textarea {
    color: black !important;
}

/* FOOTER */

.footer {
    text-align:center;
    padding:30px;
    color:#555;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HOME ----------------

st.markdown('<div id="home"></div>', unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------

st.markdown("""
<div class="hero">

<div style="text-align:center;">
""", unsafe_allow_html=True)

# LOGO
st.image(
    "logo.jpeg",
    width=220
)

# TITLE + TAGLINE
st.markdown("""
<h1 class="hero-title">Hue & Me</h1>

<p class="hero-tagline">
Because every you has a perfect hue ✨
</p>

</div>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="card">

Fashion isn’t just about what you wear — it’s about how your colors tell your story.<br><br>

At <b>Hue & Me</b>, our curiosity about colors and creativity in styling come together to help you discover the shades that truly belong to you.<br><br>

From understanding your personal color palette to building a style that reflects your personality, we transform fashion into a journey of self-expression.<br><br>

<b>Because the right hue doesn’t just change your outfit — it changes how you feel.</b>

</div>
""", unsafe_allow_html=True)
st.image(
        "https://images.unsplash.com/photo-1529139574466-a303027c1d8b",
        use_container_width=True
    )

# ---------------- BODY TYPE ----------------

st.markdown('<div id="bodytype"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Find Your Body Type</div>', unsafe_allow_html=True)

st.write("""
Every body is unique, but most shapes fall into a few common categories.
Knowing your body type helps you choose clothes that fit better, flatter your shape, and boost confidence.
""")

st.image(
    "bodychart.jpeg",
    use_container_width=True
)

body_types = [
    (
        "1️⃣ Hourglass",
        [
            "Bust and hips are almost the same width",
            "Waist is clearly defined and smaller",
            "Curves are balanced"
        ],
        "Fitted dresses, wrap tops, and high-waist bottoms highlight your natural shape."
    ),

    (
        "2️⃣ Pear (Triangle)",
        [
            "Hips are wider than shoulders",
            "Waist is defined",
            "Upper body is narrower"
        ],
        "Statement tops, structured shoulders, and darker bottoms balance the body."
    ),

    (
        "3️⃣ Apple (Round)",
        [
            "Upper body is broader",
            "Waist is less defined",
            "Weight is more around the stomach area"
        ],
        "Flowy tops, V-necks, and A-line dresses create a balanced silhouette."
    ),

    (
        "4️⃣ Rectangle (Straight)",
        [
            "Bust, waist, and hips are almost equal",
            "Minimal curves",
            "Straight body structure"
        ],
        "Layering, belts, and peplum styles help create curves."
    ),

    (
        "5️⃣ Inverted Triangle",
        [
            "Shoulders are broader than hips",
            "Narrow lower body",
            "Athletic upper frame"
        ],
        "Wide-leg pants, A-line skirts, and minimal shoulder detail balance proportions."
    )
]

for title, points, tip in body_types:

    st.markdown(f"""
    <div class="card">
    <h3>{title}</h3>

    <b>Criteria</b>
    <ul>
    <li>{points[0]}</li>
    <li>{points[1]}</li>
    <li>{points[2]}</li>
    </ul>

    <b>Style Tip:</b><br>
    {tip}

    </div>
    """, unsafe_allow_html=True)

# ---------------- SKIN UNDERTONE ----------------

st.markdown('<div id="undertone"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">Find Your Skin Undertone ✨</div>',
    unsafe_allow_html=True
)

st.write("""
The secret behind colors that make you glow?
Your skin undertone helps you discover shades that naturally suit you.
""")

# 3 COLUMNS
col1, col2, col3 = st.columns(3)

# ---------------- VEIN TEST ----------------

with col1:
    st.image(
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    width=320
)

    st.markdown("""
    <div class="card">

    <h3>01 — The Vein Test</h3>

    Look at the veins on your wrist in natural light.<br><br>

    Blue or purple veins → <b>Cool undertone</b><br><br>

    Green veins → <b>Warm undertone</b><br><br>

    A mix of both → <b>Neutral undertone</b>

    </div>
    """, unsafe_allow_html=True)

# ---------------- JEWELRY TEST ----------------

with col2:

    st.image(
    "https://images.unsplash.com/photo-1496747611176-843222e1e57c",
    width=320
)

    st.markdown("""
    <div class="card">

    <h3>02 — The Jewelry Test</h3>

    Notice which jewelry enhances your look.<br><br>

    Silver looks better → <b>Cool undertone</b><br><br>

    Gold looks better → <b>Warm undertone</b><br><br>

    Both look great → <b>Neutral undertone</b>

    </div>
    """, unsafe_allow_html=True)

# ---------------- SUN TEST ----------------

with col3:

   st.image(
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    width=320
)

    st.markdown("""
    <div class="card">

    <h3>03 — The Sun Test</h3>

    Think about how your skin reacts to sunlight.<br><br>

    Burns easily → <b>Cool undertone</b><br><br>

    Tans easily → <b>Warm undertone</b><br><br>

    Burns then tans → <b>Neutral undertone</b>

    </div>
    """, unsafe_allow_html=True)

# ---------------- PACKAGES ----------------

st.markdown('<div id="packages"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">Our Packages</div>',
    unsafe_allow_html=True
)

packages = [

    ("Hue Starter",
     "Basic body type analysis, skin undertone identification, and basic color suggestions.",
     "₹1499"),

    ("Hue Discovery",
     "Personal color palette analysis, body type analysis, and outfit suggestions based on your features.",
     "₹1999"),

    ("Style & Hue Package",
     "Complete color analysis, body shape analysis, and personalized styling recommendations.",
     "₹2999"),

    ("Wardrobe Glow-Up",
     "Closet evaluation, outfit combinations, and guidance on building a versatile wardrobe.",
     "₹4499"),

    ("Complete 360° Hue Experience",
     "Full fashion analysis including color palette, body type, personal style report, and occasion-based styling tips.",
     "₹6999")
]

for name, desc, price in packages:

    st.markdown(f"""
    <div class="package-card">

    <h3>{name}</h3>

    <p>{desc}</p>

    <h2 style="color:#8a5238;">{price}</h2>

    </div>
    """, unsafe_allow_html=True)

# ---------------- APPOINTMENT ----------------

st.markdown('<div id="appointment"></div>', unsafe_allow_html=True)

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

st.markdown('<div id="about"></div>', unsafe_allow_html=True)

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
