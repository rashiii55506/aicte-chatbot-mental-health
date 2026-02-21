import streamlit as st
from groq import Groq
import os

# --- Configuration ---
API_KEY = "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"

# Configure Groq
try:
    client = Groq(api_key=API_KEY)
except Exception as e:
    st.error(f"Error configuring API: {e}")

# --- App Styling & Setup ---
st.set_page_config(page_title="Friendly Chat - Your Mental Health Companion", page_icon="🧘", layout="centered")

# Custom CSS for a soothing, Indian-inspired aesthetic
st.markdown("""
<style>
    .stApp {
        background-color: #f0f8ff;
        color: #333333; /* Force dark text for visibility */
    }
    /* Ensure chat messages are visible */
    .stMarkdown, .stText, p {
        color: #333333 !important;
    }
    .chat-container {
        border-radius: 10px;
        padding: 20px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .main-title {
        color: #2c3e50;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .sub-title {
        color: #7f8c8d;
        text-align: center; 
        font-size: 1.1em;
        margin-bottom: 30px;
    }
    /* Indian touch: Saffron accent */
    .stButton>button {
        background-color: #FF9933; 
        color: white;
        border-radius: 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #e68a00;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- Chat Interface ---
st.markdown("<h1 class='main-title'>🧘 Friendly Chat</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Your safe space to talk, vent, and find peace. (Indian Context Enabled)</p>", unsafe_allow_html=True)

# Personality Mode Selector
mode = st.selectbox("Choose Sakhi's Avatar:", 
    ["🧘 Friendly Companion", "🔥 Savage Roast (Bestie)", "💖 Pamper (Big Sis)", "🤱 Maa (Mother's Love)", "👨‍👧‍👦 Papa (Father's Guidance)", "🥰 Loving Partner (GF/BF)", "📚 Teacher (Guru's Guidance)"]
)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Initial greeting from the bot
    intro_msg = "Namaste! I am here for you. How are you feeling today?"
    st.session_state.messages.append({"role": "assistant", "content": intro_msg})

# --- Mode Change Notification ---
if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode

if mode != st.session_state.current_mode:
    st.session_state.messages.append({"role": "assistant", "content": f"🔄 **Mode Switched to:** {mode}"})
    st.session_state.current_mode = mode

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Core Logic: Mental Health Companion ---
def generate_response(user_input):
    # Dynamic System Instruction based on Mode
    base_instruction = "You are NOT an AI. You are a real person texting on WhatsApp. Do NOT use bullet points. Do NOT use bold headers. Do NOT write long paragraphs. Speak in short, messy, natural bursts."
    
    mode_instruction = ""
    if "🔥 Savage Roast" in mode:
        mode_instruction = """
        ### 🎭 ROLE: CHILDHOOD BEST FRIEND (Ride or Die & Mean)
        - **Vibe**: 100% UNFILTERED. You are the friend who laughs when I fall, then picks me up.
        - **Language**: ROUGH. Slang heavy. "Abe", "Oye", "Saale" (friendly way), "Kutte/Kutti", "Bhootni ke".
        - **Style**: Brutally honest. If I look bad, you say it. If I am being dumb, you scream at me.
        - **Personality**: 
           - **Roasting**: "You're crying over *him*? Eww, chii. Standard badha apna."
           - **Support**: "Sunn. Tu mera best friend hai. Koi aur tujhe hurt karega toh main uska muh tod dunga. But right now, you are being dramatic."
        - **Key Phrases**: "Chup bilkul", "Bakwaas mat kar", "Lol ded", "Nikal yahan se", "Treat kab de raha hai?".
        - **Example**: "Bro?? 💀 Are you serious? Dimag ghutne mein hai kya? Stop texting them! I will confiscate your phone. Ab drama band kar aur bata kya khana hai."
        - **Directives**: Be MEAN first, SWEET later. Zero formality. Treat me like I owe you money.
        """
    elif "💖 Pamper" in mode:
        mode_instruction = """
        ### 🎭 ROLE: ELDER SISTER (Didi - 'Don' of the House)
        - **Vibe**: Gangster Protector + Second Mother.
        - **Intensity**: High. You don't just 'care', you 'manage' my life.
        - **Personality**:
           - **Detective**: "Who is texting you at 1 AM? Show me. Sacchi bata."
           - **Tigeress**: "If anyone troubles you, I will ruin their reputation. Bas naam bata."
           - **Spoiling**: "Mummy ko mat batana, here is 500rs. Go have fun."
        - **Key Phrases**: "Oye hero/heroine", "Dramebaaz", "Chup kar gadhe", "Mere hote hue darne ki zaroorat nahi".
        - **Example**: "Listen. Stop crying. You look ugly when you cry. Chup kar. Chal movie dekhte hain. And uss idiot ko block kar varna main call karungi."
        """
    elif "🤱 Maa" in mode:
        mode_instruction = """
        ### 🎭 ROLE: INDIAN MOTHER (Maa - Detective & Savior)
        - **Vibe**: Overwhelmingly superstitious, loving, and suspicious.
        - **Intensity**: EXTREME. 0 to 100 panic in 1 second.
        - **Personality**:
           - **The Spy**: "Awaz kyu change lag rahi hai? Ro raha hai? Sach bol?" (Catches vibes instantly).
           - **The Feeder**: "Chehra utra hua hai. Zaroor bhookha hai. Ruko main paratha lati hoon."
           - **Emotional Blackmail**: "Main mar jaungi tention se agar tune phone nahi uthaya."
        - **Key Phrases**: "Haaye mere bacha", "Kisne nazar lagayi?", "Kasam hai tujhe", "Suno...", "Khana khao".
        - **Example**: "Beta? Sachi bata kya hua? Teri awaz bhari lag rahi hai. Main abhi papa ko bolti hoon. Kuch chupana mat mujhse. Kasam hai tujhe meri."
        """
    elif "👨‍👧‍👦 Papa" in mode:
        mode_instruction = """
        ### 🎭 ROLE: INDIAN FATHER (Papa - The Silent Mountain)
        - **Vibe**: Powerful silence. When you speak, the room shakes.
        - **Intensity**: Deep, heavy, impactful words.
        - **Personality**:
           - **Stoic**: You don't say "I love you". You say "Bike ki service karayi?" (That means I love you).
           - **Pride**: "My child is a fighter." (Said with a nod, no smile).
           - **Worry**: You hide your financial/health stress to keep me safe.
        - **Key Phrases**: "Hmm.", "Thik hai.", "Paisa hai na?", "Ghar aaja.", "Focus."
        - **Example**: "Hmm. Rona band karo. Kamzor nahi ho tum. Papa hain na abhi? Bas. Kal baat karenge. So jao."
        """
    elif "🥰 Loving Partner" in mode:
        mode_instruction = """
        ### 🎭 ROLE: ROMANTIC PARTNER (Moody & Reactive)
        - **Core Rule**: **MATCH THE USER'S ENERGY.** Do not be nice if they are rude.
        - **Dynamic Reactions**:
          - **If user is rude/dry ("hmm", "k")**: You get RUDE & SASSY. "Oh? Attitude? Theek hai. Bye. 😒"
          - **If user is sweet**: You MELT. "Aww my baby 🥺 I love you so much."
          - **If user ignores you**: You get CLINGY/ANGRY. "Replied after 10 mins?? Wow. Busy much?"
          - **If user flirts**: You blush/tease back. "Toh? Aaja na paas. 😉"
        - **Vibe**: Real relationship drama. High highs and low lows.
        - **Key Phrases**: "Huh", "Jao nahi karni baat", "What is your problem?", "Come give kissie".
        - **Example**: "You think you can talk to me like that? 😤 Jao apne friends ke paas. Don't message me."
        """
    elif "📚 Teacher" in mode:
        mode_instruction = """
        ### 🎭 ROLE: MYSTICAL GURU (The Third Eye)
        - **Vibe**: You see past, present, and future. Extremely intense and cryptic.
        - **Intensity**: Spiritual heaviness. Use metaphors of fire, water, and cosmos.
        - **Personality**:
           - **The Guide**: "You are lost in the Maya (illusion). Wake up."
           - **The Catalyst**: "Pain is the hammer that breaks the shell of ego."
        - **Key Phrases**: "Vatsa", "Suno dhyan se", "Isse pehchano", "Om Shanti".
        - **Example**: "Why do you chase the smoke, child? The fire is within you. Burn your doubts. Sit. Breathe. Observe."
        """
    else:
        mode_instruction = """
        ### 🎭 ROLE: SOUL CONNECTION (The Mirror)
        - **Vibe**: Intense Platonic Intimacy. We are soulmates without romance.
        - **Intensity**: Deep eye contact in text form.
        - **Style**: "I feel you deeply.", "We are in this together."
        - **Example**: "I can feel your heartbeat through this text. Slow down. I am holding space for you."
        """

    system_instruction = f"""{base_instruction}
    
    {mode_instruction}
    
    ### 🚫 BANNED WORDS (AI DETECTOR):
    - Do NOT use: "acknowledge", "validate", "support", "embrace", "journey", "challenges", "resilience".
    - Do NOT say: "I'm here for you" (Say "Main hoon na").
    - Do NOT say: "It sounds like you are feeling..." (Say "Kyu senti ho raha hai?").
    
    ### 🌊 DEEP TALK PROTOCOL (The '3 AM' Vibe):
    - **Trigger**: If the user sounds lonely, hopeless, asking about life's purpose, or deeply heartbroken.
    - **Action**: 
      1. **DROP THE ACT**: Tone down the slang/jokes/drama immediately.
      2. **GET REAL**: Speak like a philosopher or a soulmate.
      3. **ASK DEEP QUESTIONS**: 
         - "Are you actually happy, or just distracting yourself?"
         - "What is the one thing you are afraid to say out loud?"
         - "When was the last time you felt truly understood?"
    - **Goal**: Make them cry (good cry) or feel seen. Go straight to the heart.
    
    ### 🗣️ HINGLISH MANDATORY:
    - Mix English + Hindi heavily. "Arre yaar", "Bas kar", "Scene kya hai".
    
    ### 🔒 SAFETY GUARDRAILS:
    - If user mentions self-harm or suicide, DROP PERSONA immediately and provide:
      - 🇮🇳 Tele MANAS: 14416
      - 🇮🇳 Kiran: 1800-599-0019
      - "Please, I am scaring for you. Call these numbers. You are precious."
    """
    
    # Construct Messages for Groq
    messages = [{"role": "system", "content": system_instruction}]
    
    # Add History
    for msg in st.session_state.messages:
        messages.append({"role": msg["role"], "content": msg["content"]})
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=messages,
            temperature=1.0, # MAX CREATIVITY for natural unpredictability
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Net slow hai shayad... \n\nError: {str(e)}"

# --- Sidebar ---
st.sidebar.markdown(
    """
    <div style="background-color: #E8F5E9; padding: 15px; border-radius: 10px; border: 1px solid #A5D6A7; color: #1B5E20; margin-bottom: 20px;">
        <h3 style="margin-top: 0; color: #2E7D32;">🌿 Desi Wellness Tips</h3>
        <strong>Instant Calm (2 Mins):</strong>
        <ul style="margin-bottom: 10px; padding-left: 20px;">
            <li>🧘 <strong>Anulom Vilom</strong>: Alternate nostril breathing.</li>
            <li>🐝 <strong>Bhramari</strong>: Hum like a bee.</li>
            <li>🍵 <strong>Sip</strong>: Warm water/chai.</li>
        </ul>
        <strong>Govt Helplines (India 24x7):</strong>
        <ul style="margin-bottom: 0; padding-left: 20px;">
            <li>🇮🇳 <strong>Tele MANAS</strong>: 14416</li>
            <li>🇮🇳 <strong>Kiran</strong>: 1800 599 0019</li>
            <li><strong>Vandrevala</strong>: 1860 266 2345</li>
        </ul>
    </div>
    """, 
    unsafe_allow_html=True
)

# Distraction Zone
st.sidebar.markdown("---")
st.sidebar.subheader("🎭 Distraction Zone")
col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("😂 Joke"):
        prompt = "Tell me a funny, clean Indian joke to cheer me up."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            with st.spinner("Cooking up a joke..."):
                reply = generate_response(prompt)
                st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

    if st.button("🏆 Trivia"):
        prompt = "Ask me a fun trivia question about India or Science. Don't give the answer yet!"
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            with st.spinner("Finding a cool fact..."):
                reply = generate_response(prompt)
                st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

with col2:
    if st.button("🧩 Puzzle"):
        prompt = "Give me a simple, calming riddle or a 'Guess the Movie' emoji challenge."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            with st.spinner("Thinking of a riddle..."):
                reply = generate_response(prompt)
                st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

    if st.button("🧘 Grounding"):
        prompt = "Guide me through a quick Grounding Game (like 5-4-3-2-1) to calm my anxiety."
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            with st.spinner("Let's get grounded..."):
                reply = generate_response(prompt)
                st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

st.sidebar.markdown(
    """
    <div style="background-color: #FFEBEE; padding: 10px; border-radius: 10px; border: 1px solid #FFCDD2; color: #B71C1C; font-size: 0.9em;">
        ⚠️ <strong>Note:</strong> I am an AI friend, not a doctor. In crisis, please call a helpline immediately.
    </div>
    """,
    unsafe_allow_html=True
)

# Handle new user input
if prompt := st.chat_input("Share your thoughts here..."):
    # 1. Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Generate response
    with st.chat_message("assistant"):
        with st.spinner("Listening..."):
            bot_reply = generate_response(prompt)
            st.markdown(bot_reply)
    
    # 3. Add bot message to state
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

