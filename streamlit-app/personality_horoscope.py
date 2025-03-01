import streamlit as st

zodiac_traits = {
    "Aries": {
        "personality": "Aries are known for their leadership qualities, courage, and passion. They are natural-born leaders and are always ready to take on new challenges.",
        "strengths": "Energetic, courageous, determined, confident, enthusiastic.",
        "weaknesses": "Impatient, impulsive, quick-tempered, reckless.",
        "emoji": "🔥",
        "color": "#FF5733"
    },
    "Taurus": {
        "personality": "Taurus are reliable, patient, and practical. They value stability and comfort in their life, and are often seen as strong and determined individuals.",
        "strengths": "Reliable, patient, practical, devoted, responsible.",
        "weaknesses": "Stubborn, possessive, materialistic, lazy.",
        "emoji": "🌿",
        "color": "#2E8B57"
    },
    "Gemini": {
        "personality": "Geminis are known for their adaptability, intelligence, and curiosity. They love learning and are often very social and communicative.",
        "strengths": "Adaptable, outgoing, intelligent, witty, curious.",
        "weaknesses": "Indecisive, anxious, inconsistent, superficial.",
        "emoji": "💨",
        "color": "#FFD700"
    },
    "Cancer": {
        "personality": "Cancers are deeply intuitive, emotional, and empathetic. They care deeply about family and home, and are often very protective of their loved ones.",
        "strengths": "Caring, intuitive, protective, empathetic, loyal.",
        "weaknesses": "Moody, insecure, easily hurt, overly emotional.",
        "emoji": "🌙",
        "color": "#00BFFF"
    },
    "Leo": {
        "personality": "Leos are confident, ambitious, and charismatic. They love attention and enjoy being the center of the stage. They are natural performers and leaders.",
        "strengths": "Generous, warm-hearted, creative, enthusiastic, confident.",
        "weaknesses": "Arrogant, self-centered, stubborn, attention-seeking.",
        "emoji": "🌟",
        "color": "#FFD700"
    },
    "Virgo": {
        "personality": "Virgos are known for their analytical minds, attention to detail, and practicality. They are perfectionists who strive for excellence in everything they do.",
        "strengths": "Practical, analytical, hardworking, reliable, modest.",
        "weaknesses": "Overcritical, shy, worrisome, perfectionist.",
        "emoji": "🔍",
        "color": "#8A2BE2"
    },
    "Libra": {
        "personality": "Libras are known for their diplomacy, charm, and love for balance and harmony. They are great communicators and love socializing.",
        "strengths": "Charming, diplomatic, artistic, fair-minded, social.",
        "weaknesses": "Indecisive, superficial, avoids confrontations, self-pitying.",
        "emoji": "⚖️",
        "color": "#1E90FF"
    },
    "Scorpio": {
        "personality": "Scorpios are intense, passionate, and resourceful. They are known for their deep emotional strength and ability to stay focused.",
        "strengths": "Brave, resourceful, determined, loyal, ambitious.",
        "weaknesses": "Jealous, secretive, resentful, controlling.",
        "emoji": "🦂",
        "color": "#DC143C"
    },
    "Sagittarius": {
        "personality": "Sagittarians are adventurous, optimistic, and always seeking knowledge. They love freedom and exploring new possibilities.",
        "strengths": "Optimistic, adventurous, philosophical, independent, honest.",
        "weaknesses": "Impatient, tactless, overconfident, reckless.",
        "emoji": "🏹",
        "color": "#FF6347"
    },
    "Capricorn": {
        "personality": "Capricorns are disciplined, responsible, and ambitious. They take a practical and strategic approach to life and love achieving their goals.",
        "strengths": "Disciplined, responsible, patient, ambitious, practical.",
        "weaknesses": "Pessimistic, stubborn, cold, unforgiving.",
        "emoji": "🐐",
        "color": "#8B4513"
    },
    "Aquarius": {
        "personality": "Aquarians are innovative, independent, and love thinking outside the box. They value individuality and are open-minded.",
        "strengths": "Innovative, independent, intelligent, humanitarian, idealistic.",
        "weaknesses": "Unpredictable, detached, eccentric, aloof.",
        "emoji": "🌊",
        "color": "#00FFFF"
    },
    "Pisces": {
        "personality": "Pisces are compassionate, empathetic, and intuitive. They are often creative and enjoy helping others.",
        "strengths": "Compassionate, artistic, empathetic, gentle, wise.",
        "weaknesses": "Overly emotional, escapist, idealistic, gullible.",
        "emoji": "🐟",
        "color": "#4169E1"
    }
}

horoscope_for_today = {
    "Aries": "Today is a good day to take charge and make decisions. Your leadership skills will shine through!",
    "Taurus": "Today may require patience. Stay grounded, and trust that things will fall into place.",
    "Gemini": "Today is a great day for socializing! Engage with others and share your ideas.",
    "Cancer": "Today, focus on nurturing your relationships. Take time for family and friends.",
    "Leo": "Your energy and charisma are at an all-time high today. Use it to inspire others!",
    "Virgo": "Focus on your work today. Attention to detail will bring you success in your tasks.",
    "Libra": "Today is perfect for making decisions. Balance your priorities carefully.",
    "Scorpio": "Embrace the intense energy today. Focus on your long-term goals.",
    "Sagittarius": "It’s a good day for adventure! Explore new ideas and make bold choices.",
    "Capricorn": "Stay focused on your career today. Hard work will pay off soon.",
    "Aquarius": "It’s a good day for creative expression. Trust your instincts.",
    "Pisces": "Today is ideal for helping others and tapping into your creative side.",
}

st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        padding: 10px;
        border-radius: 8px;
    }
    .title {
        color: #5B5B5B;
        font-size: 36px;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    .section-header {
        color: #2e8b57;
        font-size: 24px;
        font-weight: bold;
    }
    .content {
        font-size: 18px;
        color: #333;
    }
    .horoscope {
        font-size: 20px;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("🌟 Personality Horoscope 🌟")

zodiac_sign = st.selectbox("Select your zodiac sign:", list(zodiac_traits.keys()))

selected_zodiac = zodiac_traits[zodiac_sign]

st.markdown(f"<h2 style='color:{selected_zodiac['color']};'>{selected_zodiac['emoji']} {zodiac_sign} Personality {selected_zodiac['emoji']}</h2>", unsafe_allow_html=True)
st.write(f"**Personality:** {selected_zodiac['personality']}")
st.write(f"**Strengths:** {selected_zodiac['strengths']}")
st.write(f"**Weaknesses:** {selected_zodiac['weaknesses']}")
st.markdown(f"<h3 class='section-header'>Today's Horoscope for {zodiac_sign}</h3>", unsafe_allow_html=True)
st.markdown(f"""
    <div class="horoscope" style="background-color:{selected_zodiac['color']}; color:white;">
        {horoscope_for_today.get(zodiac_sign, 'No horoscope available for today.')}
    </div>
""", unsafe_allow_html=True)

