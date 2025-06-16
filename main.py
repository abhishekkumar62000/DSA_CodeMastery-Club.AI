import streamlit as st
import json
import random
import smtplib
import google.generativeai as genai
from email.message import EmailMessage
import os
import hashlib
from datetime import date, datetime, timedelta
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(page_title="DSA_CodeMastery Club", page_icon="\U0001F916", layout="wide")
# --- Enhanced, Unique, Animated Dark Gradient Background with Floating Blobs ---
st.markdown('''
    <style>
    html, body, .stApp {
        background: linear-gradient(120deg, #232526 0%, #414345 100%) !important;
        min-height: 100vh;
        font-family: 'Segoe UI', 'Roboto', 'Montserrat', sans-serif;
        position: relative;
        overflow-x: hidden;
    }
    /* Multiple animated floating blobs for more depth and color */
    .stApp:after, .stApp:before, .stApp .blob3, .stApp .blob4, .stApp .blob5, .stApp .blob6 {
        content: '';
        position: fixed;
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
        filter: blur(2px);
    }
    .stApp:after {
        top: -120px; left: -120px;
        width: 400px; height: 400px;
        background: radial-gradient(circle at 60% 40%, #8f5cff 0%, #2b5876 100%);
        opacity: 0.22;
        animation: blobMove1 18s ease-in-out infinite alternate;
    }
    .stApp:before {
        bottom: -100px; right: -100px;
        width: 350px; height: 350px;
        background: radial-gradient(circle at 40% 60%, #ff512f 0%, #dd2476 100%);
        opacity: 0.19;
        animation: blobMove2 22s ease-in-out infinite alternate;
    }
    .stApp .blob3 {
        top: 30vh; left: -80px;
        width: 220px; height: 220px;
        background: radial-gradient(circle at 70% 30%, #43e97b 0%, #38f9d7 100%);
        opacity: 0.15;
        animation: blobMove3 24s ease-in-out infinite alternate;
    }
    .stApp .blob4 {
        bottom: 10vh; right: 10vw;
        width: 180px; height: 180px;
        background: radial-gradient(circle at 30% 70%, #fa709a 0%, #fee140 100%);
        opacity: 0.13;
        animation: blobMove4 28s ease-in-out infinite alternate;
    }
    .stApp .blob5 {
        top: 60vh; left: 60vw;
        width: 180px; height: 180px;
        background: radial-gradient(circle at 60% 60%, #00c6ff 0%, #0072ff 100%);
        opacity: 0.13;
        animation: blobMove5 32s ease-in-out infinite alternate;
    }
    .stApp .blob6 {
        top: 10vh; right: 10vw;
        width: 140px; height: 140px;
        background: radial-gradient(circle at 40% 60%, #f7971e 0%, #ffd200 100%);
        opacity: 0.11;
        animation: blobMove6 36s ease-in-out infinite alternate;
    }
    @keyframes blobMove1 {
        0% { transform: scale(1) translate(0,0); }
        100% { transform: scale(1.2) translate(60px, 40px); }
    }
    @keyframes blobMove2 {
        0% { transform: scale(1) translate(0,0); }
        100% { transform: scale(1.1) translate(-40px, -60px); }
    }
    @keyframes blobMove3 {
        0% { transform: scale(1) translate(0,0); }
        100% { transform: scale(1.15) translate(40px, 60px); }
    }
    @keyframes blobMove4 {
        0% { transform: scale(1) translate(0,0); }
        100% { transform: scale(1.1) translate(-30px, -40px); }
    }
    @keyframes blobMove5 {
        0% { transform: scale(1) translate(0,0); }
        100% { transform: scale(1.18) translate(30px, -30px); }
    }
    @keyframes blobMove6 {
        0% { transform: scale(1) translate(0,0); }
        100% { transform: scale(1.12) translate(-20px, 30px); }
    }
    /* Sparkle overlay for extra vibrance */
    .stApp .sparkle {
        content: '';
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        pointer-events: none;
        background: url('https://svgshare.com/i/13dF.svg') repeat;
        opacity: 0.08;
        animation: sparkleMove 20s linear infinite;
        z-index: 1;
    }
    @keyframes sparkleMove {
        0% {background-position: 0 0;}
        100% {background-position: 200px 200px;}
    }
    /* Sidebar with glassmorphism effect */
    .stSidebar, .css-1d391kg, .css-1lcbmhc {
        background: rgba(44,47,59,0.92) !important;
        color: #fff !important;
        border-radius: 24px 0 0 24px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(10px);
        border-right: 2px solid #8f5cff55;
    }
    /* Sidebar radio and text */
    .stRadio > label, .stTextInput > label, .stSelectbox > label {
        color: #fff !important;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    /* Main title and headers with rainbow gradient */
    .stTitle, .stHeader, .stSubheader {
        background: linear-gradient(90deg, #8f5cff, #43e97b, #fa709a, #fee140, #6366f1);
        background-size: 200% 200%;
        color: transparent !important;
        -webkit-background-clip: text;
        background-clip: text;
        animation: rainbowText 4s ease-in-out infinite;
        font-weight: 900;
        text-shadow: 2px 2px 8px #8f5cff33;
    }
    @keyframes rainbowText {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    /* Card-like containers with glassmorphism, dark mode */
    .stMarkdown, .stDataFrame, .stTable, .stAlert, .stSuccess, .stInfo, .stError {
        background: rgba(44,47,59,0.92);
        border-radius: 18px;
        box-shadow: 0 4px 24px #8f5cff33;
        padding: 1.3em 1.1em;
        margin-bottom: 1.3em;
        animation: fadeInUp 0.8s;
        border: 1.5px solid #8f5cff33;
        color: #fff !important;
    }
    /* Buttons with animated gradient */
    .stButton > button {
        background: linear-gradient(270deg, #8f5cff, #43e97b, #fa709a, #fee140, #6366f1);
        background-size: 400% 400%;
        color: #fff;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        font-size: 1.1em;
        box-shadow: 0 2px 12px #8f5cff33;
        transition: transform 0.1s, box-shadow 0.1s;
        animation: gradientMove 6s ease-in-out infinite;
    }
    .stButton > button:hover {
        transform: scale(1.07);
        box-shadow: 0 6px 24px #8f5cff55;
        filter: brightness(1.1);
    }
    @keyframes gradientMove {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    /* Animations */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    /* Progress bar with animated color */
    .stProgress > div > div {
        background: linear-gradient(90deg, #8f5cff 0%, #43e97b 50%, #fa709a 100%);
        border-radius: 10px;
        animation: gradientMove 4s linear infinite;
    }
    /* Quiz radio buttons */
    .stRadio > div {
        background: #232526;
        border-radius: 10px;
        padding: 0.6em 1.1em;
        margin-bottom: 0.6em;
        border: 1.5px solid #8f5cff33;
        box-shadow: 0 2px 8px #8f5cff22;
        color: #fff !important;
    }
    /* Custom flashcard style */
    .flashcard {
        background: linear-gradient(135deg, #232526 60%, #8f5cff22 100%);
        border-radius: 16px;
        box-shadow: 0 2px 12px #8f5cff22;
        padding: 1.7em;
        margin: 1.2em 0;
        text-align: center;
        font-size: 1.25em;
        animation: fadeInUp 0.8s;
        border: 1.5px solid #8f5cff33;
        color: #fff !important;
    }
    </style>
    <div class="blob3"></div>
    <div class="blob4"></div>
    <div class="blob5"></div>
    <div class="blob6"></div>
    <div class="sparkle"></div>
''', unsafe_allow_html=True)

# --- Enhanced, Interactive, Colorful Animated Title Block ---
st.markdown('''
    <style>
    .super-animated-title-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 1.7em;
        margin-bottom: 2.5em;
        z-index: 10;
        position: relative;
    }
    .super-animated-title {
        font-size: 3.3em;
        font-family: 'Montserrat', 'Segoe UI', sans-serif;
        font-weight: 900;
        letter-spacing: 1.5px;
        padding: 0.15em 0.7em;
        border-radius: 32px;
        background: linear-gradient(90deg, #ff6a00, #ee0979, #43e97b, #38f9d7, #fa709a, #fee140, #6366f1, #f472b6, #34d399, #fbbf24, #ff6a00);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        color: transparent;
        text-shadow: 0 0 24px #fff7, 0 2px 32px #a5b4fc99, 0 0 8px #ff6a00cc;
        animation: superGradientFlow 7s ease-in-out infinite, superBounceIn 1.3s cubic-bezier(.68,-0.55,.27,1.55) 1;
        filter: drop-shadow(0 2px 24px #a5b4fc55);
        position: relative;
    }
    .super-animated-title .emoji {
        font-size: 1.25em;
        vertical-align: middle;
        margin-right: 0.18em;
        filter: drop-shadow(0 0 12px #fee140cc);
        animation: emojiPop 2.5s infinite alternate;
    }
    .super-animated-title .club {
        background: linear-gradient(90deg, #fbbf24, #6366f1, #fa709a, #43e97b, #fee140);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        color: transparent;
        animation: clubGradient 4s ease-in-out infinite;
        text-shadow: 0 0 18px #fee14099;
    }
    .super-animated-title .caption {
        display: block;
        font-size: 0.38em;
        font-weight: 700;
        margin-top: 0.18em;
        letter-spacing: 1.2px;
        background: linear-gradient(90deg, #43e97b, #fa709a, #fee140, #6366f1, #f472b6);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        color: transparent;
        text-shadow: 0 0 10px #fff7, 0 2px 12px #6366f1cc;
        opacity: 0.96;
        animation: captionGradient 6s ease-in-out infinite, fadeInDown 1.2s 0.7s both;
    }
    @keyframes superGradientFlow {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    @keyframes clubGradient {
        0% {background-position: 0% 50%;}
        100% {background-position: 100% 50%;}
    }
    @keyframes captionGradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    @keyframes superBounceIn {
        0% {transform: scale(0.7) translateY(-60px); opacity: 0;}
        60% {transform: scale(1.13) translateY(10px); opacity: 1;}
        80% {transform: scale(0.97) translateY(-4px);}
        100% {transform: scale(1) translateY(0);}
    }
    @keyframes emojiPop {
        0% {transform: scale(1) rotate(-8deg);}
        100% {transform: scale(1.22) rotate(8deg);}
    }
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    <div class="super-animated-title-container">
        <div class="super-animated-title">
            <span class="emoji">🌈</span> DSA_CodeMastery <span class="club">Club.AI</span>
            <span class="caption">Your AI-Powered DSA Learning Hub 🚀 | Learn, Practice, Master — All in One Place!</span>
        </div>
    </div>
''', unsafe_allow_html=True)

# Folder setup
os.makedirs("data", exist_ok=True)
os.makedirs("progress", exist_ok=True)
os.makedirs("schedules", exist_ok=True)
os.makedirs("auth", exist_ok=True)

USER_FILE = 'auth/users.json'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def auth_ui():
    st.sidebar.subheader("\U0001F510 Login or Signup")
    users = load_users()
    action = st.sidebar.radio("Choose Action", ["Login", "Signup"])

    if action == "Signup":
        new_user = st.sidebar.text_input("Create Username")
        new_email = st.sidebar.text_input("Your Email")
        new_pass = st.sidebar.text_input("Create Password", type="password")
        if st.sidebar.button("Signup"):
            if new_user in users:
                st.sidebar.warning("Username already exists!")
            else:
                users[new_user] = {
                    "password": hash_password(new_pass),
                    "email": new_email
                }
                save_users(users)
                st.sidebar.success("Signup successful! Please login.")
                st.rerun()

    elif action == "Login":
        user = st.sidebar.text_input("Username")
        passwd = st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            if user in users and users[user]['password'] == hash_password(passwd):
                st.session_state.logged_in = True
                st.session_state.username = user
                st.session_state.email = users[user]['email']
                st.success(f"Welcome, {user}!")
                st.rerun()
            else:
                st.sidebar.error("Invalid credentials")

def load_questions():
    with open('data/dsa_questions.json', 'r') as f:
        return json.load(f)

def get_user_progress_file():
    return f"progress/{st.session_state['username']}_progress.json"

def load_progress():
    path = get_user_progress_file()
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                content = f.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        except json.JSONDecodeError:
            return {}
    return {}

def save_progress(topic, increment=1):
    today = str(date.today())
    progress = load_progress()

    if today not in progress:
        progress[today] = {}
    if topic not in progress[today]:
        progress[today][topic] = 0
    progress[today][topic] += increment

    with open(get_user_progress_file(), 'w') as f:
        json.dump(progress, f, indent=2)

def get_user_schedule_file():
    return f"schedules/{st.session_state['username']}_schedule.json"

def load_schedule():
    path = get_user_schedule_file()
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_schedule(schedule):
    path = get_user_schedule_file()
    with open(path, 'w') as f:
        json.dump(schedule, f, indent=2)

def send_email_alert(subject, message, to_email=None):
    try:
        from_email = "abhiydv23096@gmail.com"
        password = "lckb mgdo mqao wdef"  # Gmail App Password
        if to_email is None:
            to_email = st.session_state.get('email')

        # Add greeting and reminder context
        greeting = f"Hello {st.session_state.get('username', 'User')},\n\n"
        reminder_note = "This is a friendly reminder that you have a scheduled task in your DSA StudyBot app.\nYou recently used the 'Your Scheduled Tasks' feature to set this reminder.\n\n"
        full_message = greeting + reminder_note + message + "\n\nBest wishes for your study!\n- DSA StudyBot"

        msg = EmailMessage()
        msg.set_content(full_message)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        st.error(f"❌ Email alert failed: {e}")

def quiz_interface(topic, questions):
    st.subheader(f"\U0001F9E0 Quiz on {topic}")

    if 'quiz_index' not in st.session_state or st.session_state.get("quiz_topic") != topic:
        st.session_state.quiz_index = 0
        st.session_state.quiz_topic = topic
        st.session_state.quiz_submitted = False
        st.session_state.shuffled_questions = random.sample(questions, len(questions))
        st.session_state.selected_option = None
        st.session_state.correct_count = 0
        st.session_state.show_hint = False

    idx = st.session_state.quiz_index
    if idx >= len(st.session_state.shuffled_questions):
        st.success("\U0001F389 Quiz completed!")
        st.info(f"✅ Correct Answers: {st.session_state.correct_count} out of {len(st.session_state.shuffled_questions)}")
        save_progress(topic, st.session_state.correct_count)
        return

    q = st.session_state.shuffled_questions[idx]

    st.markdown(f"**Question {idx + 1}:** {q['question']}")

    if not st.session_state.show_hint:
        if st.button("\U0001F4A1 Show Hint"):
            st.session_state.show_hint = True
            st.rerun()
    else:
        st.info(f"\U0001F4A1 **Hint:** {q['hint']}")

    st.session_state.selected_option = st.radio(
        "Choose an answer",
        q['options'],
        index=None,
        key=f"radio_{idx}"
    )

    if not st.session_state.quiz_submitted:
        if st.button("Submit"):
            if st.session_state.selected_option is None:
                st.warning("Please select an option before submitting.")
            else:
                st.session_state.quiz_submitted = True
                if st.session_state.selected_option == q['answer']:
                    st.success("✅ Correct!")
                    st.session_state.correct_count += 1
                else:
                    st.error("❌ Incorrect.")
    if st.session_state.quiz_submitted:
        st.markdown(f"\U0001F9E0 **Explanation:** {q['explanation']}")
        show_resource_recommendations(topic)
        btn_label = "Submit Quiz" if idx == len(st.session_state.shuffled_questions) - 1 else "Next Question"
        if st.button(btn_label):
            st.session_state.quiz_index += 1
            st.session_state.quiz_submitted = False
            st.session_state.selected_option = None
            st.session_state.show_hint = False
            st.rerun()

def show_progress():
    st.subheader("\U0001F4CA Your DSA Progress")
    progress = load_progress()
    if not progress:
        st.info("No progress yet. Take a quiz!")
        return

    dates = list(progress.keys())
    topics = set()
    for daily in progress.values():
        topics.update(daily.keys())

    topics = sorted(topics)

    topic_data = {t: [] for t in topics}
    for d in dates:
        for t in topics:
            topic_data[t].append(progress[d].get(t, 0))

    st.write("### Progress Over Time")
    fig, ax = plt.subplots(figsize=(10, 5))
    for t in topics:
        ax.plot(dates, topic_data[t], marker='o', label=t)
    ax.set_xlabel("Date")
    ax.set_ylabel("Questions Solved")
    ax.set_title("DSA Progress (Topic-wise)")
    ax.legend()
    st.pyplot(fig)

def show_interactive_progress():
    st.subheader('📈 Interactive Progress Visualizations')
    progress = load_progress()
    data = load_questions()
    topics = sorted(data.keys())
    # Pie chart for topic coverage
    topic_counts = []
    for topic in topics:
        count = 0
        if isinstance(progress, dict):
            for day in progress.values():
                if isinstance(day, dict):
                    count += day.get(topic, 0)
        topic_counts.append(count)
    fig = go.Figure(data=[go.Pie(labels=topics, values=topic_counts, hole=.3)])
    fig.update_layout(title_text='Questions Solved by Topic')
    st.plotly_chart(fig, use_container_width=True)
    # Heatmap for activity (date vs. topic)
    if progress:
        dates = list(progress.keys())
        z = []
        for topic in topics:
            row = []
            for d in dates:
                row.append(progress[d].get(topic, 0))
            z.append(row)
        heatmap = go.Figure(data=go.Heatmap(z=z, x=dates, y=topics, colorscale='Blues'))
        heatmap.update_layout(title='Activity Heatmap (Questions Solved)')
        st.plotly_chart(heatmap, use_container_width=True)

def show_scheduler():
    st.subheader("\U0001F4C5 Smart Study Scheduler")
    schedule = load_schedule()

    task = st.text_input("Enter a new task")
    study_date = st.date_input("Select study date", value=date.today())
    study_time = st.time_input("Time to study")

    if st.button("Add Task"):
        task_entry = {
            "task": task,
            "date": str(study_date),
            "time": str(study_time),
            "reminded": False
        }
        schedule.setdefault("tasks", []).append(task_entry)
        save_schedule(schedule)
        st.success(f"Task added: {task} on {study_date} at {study_time}")
        send_email_alert("\U0001F4DA Study Reminder Added", f"New task: {task} on {study_date} at {study_time}")

    tasks = schedule.get("tasks", [])
    tasks.sort(key=lambda x: (x["date"], x["time"]))

    today = str(date.today())
    current_time = datetime.now().strftime("%H:%M:%S")

    if tasks:
        st.write("### \U0001F4C4 Your Scheduled Tasks")
        for i, t in enumerate(tasks):
            col1, col2 = st.columns([6, 1])
            with col1:
                st.write(f"**{t['task']}** on `{t['date']}` at `{t['time']}`")
            with col2:
                if st.button("🗑️", key=f"delete_{i}"):
                    tasks.pop(i)
                    schedule['tasks'] = tasks
                    save_schedule(schedule)
                    st.success("Task deleted.")
                    st.rerun()

            if t.get("date") == today and not t.get("reminded", False) and current_time >= t["time"]:
                st.info(f"⏰ Reminder: {t['task']} scheduled for {t['time']}")
                send_email_alert("📌 Study Reminder", f"Reminder: {t['task']} is scheduled today at {t['time']}")
                t['reminded'] = True
                save_schedule(schedule)
def show_chatbot():
    st.subheader("🤖 DSA Doubt-Resolving Chatbot (Gemini)")

    # Load your Gemini API Key
    genai.configure(api_key="")

    user_question = st.text_area("💬 Ask your DSA doubt (e.g., What is memoization in DP?)")

    if st.button("Ask Chatbot"):
        if not user_question.strip():
            st.warning("Please type a valid question.")
            return

        try:
            model = genai.GenerativeModel(model_name="gemini-2.0-flash")
            response = model.generate_content(user_question)
            st.success("✅ Here's the explanation:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"❌ Gemini API Error: {e}")                

# --- Daily Challenge & Streaks ---

def get_daily_challenge():
    data = load_questions()
    all_questions = []
    for topic, questions in data.items():
        for q in questions:
            all_questions.append((topic, q))
    random.seed(str(date.today()))
    return random.choice(all_questions) if all_questions else (None, None)

def update_streak():
    streak_file = f"progress/{st.session_state['username']}_streak.json"
    today = str(date.today())
    streak = {"current": 0, "last_date": None, "max": 0}
    if os.path.exists(streak_file):
        with open(streak_file, 'r') as f:
            streak = json.load(f)
    if streak["last_date"] == today:
        return streak["current"], streak["max"]
    elif streak["last_date"] == (date.today() - timedelta(days=1)).isoformat():
        streak["current"] += 1
    else:
        streak["current"] = 1
    streak["last_date"] = today
    streak["max"] = max(streak["max"], streak["current"])
    with open(streak_file, 'w') as f:
        json.dump(streak, f)
    return streak["current"], streak["max"]

def show_daily_challenge():
    st.subheader("🔥 Daily DSA Challenge")
    topic, q = get_daily_challenge()
    if not q:
        st.info("No questions available.")
        return
    st.markdown(f"**Topic:** {topic}")
    st.markdown(f"**Question:** {q['question']}")
    user_answer = st.radio("Your Answer", q['options'], key="daily_challenge")
    if st.button("Submit Daily Challenge"):
        if user_answer == q['answer']:
            st.success("Correct! +1 streak!")
            cur, mx = update_streak()
            st.info(f"Current Streak: {cur} | Max Streak: {mx}")
            add_badge_if_earned(cur)
        else:
            st.error("Incorrect. Try again tomorrow!")
            update_streak()  # resets streak if wrong

# --- Badges & Gamification ---
BADGES = {
    "Quiz Master": "Completed 10 quizzes!",
    "Streak King": "5-day answer streak!",
    "Early Bird": "Answered before 8AM!"
}

def get_badges():
    badge_file = f"progress/{st.session_state['username']}_badges.json"
    if os.path.exists(badge_file):
        with open(badge_file, 'r') as f:
            return json.load(f)
    return []

def add_badge_if_earned(streak):
    badge_file = f"progress/{st.session_state['username']}_badges.json"
    badges = get_badges()
    if streak >= 5 and "Streak King" not in badges:
        badges.append("Streak King")
        st.balloons()
        st.success("🏆 New Badge: Streak King!")
    # Add more badge logic as needed
    with open(badge_file, 'w') as f:
        json.dump(badges, f)

def show_badges():
    st.subheader("🏅 Your Badges")
    badges = get_badges()
    if not badges:
        st.info("No badges yet. Keep learning!")
    else:
        for b in badges:
            st.success(f"🏅 {b}: {BADGES.get(b, '')}")

# --- Peer-to-Peer Doubt Solving (Mini-Forum) ---
DOUBT_FILE = 'data/doubts.json'

def load_doubts():
    if not os.path.exists(DOUBT_FILE):
        return []
    with open(DOUBT_FILE, 'r') as f:
        return json.load(f)

def save_doubts(doubts):
    with open(DOUBT_FILE, 'w') as f:
        json.dump(doubts, f, indent=2)

def show_doubt_forum():
    st.subheader('💬 Peer-to-Peer DSA Doubt Forum')
    doubts = load_doubts()
    st.markdown('**Post your DSA doubt or help others!**')
    with st.form('post_doubt'):
        new_doubt = st.text_area('Your DSA Doubt')
        topic = st.selectbox('Topic', ['Arrays', 'Dynamic Programming', 'Graph', 'Linked List', 'Stack', 'Queue', 'Trees', 'Binary Search Tree'])
        if st.form_submit_button('Post Doubt'):
            if new_doubt.strip():
                doubts.append({
                    'user': st.session_state['username'],
                    'doubt': new_doubt,
                    'topic': topic,
                    'answers': [],
                    'upvotes': 0
                })
                save_doubts(doubts)
                st.success('Doubt posted!')
                st.rerun()
    if doubts:
        for i, d in enumerate(doubts[::-1]):
            st.markdown(f"**{d['user']}** asked about **{d['topic']}**:")
            st.info(d['doubt'])
            st.write(f"👍 Upvotes: {d.get('upvotes', 0)}")
            if st.button('Upvote', key=f'upvote_{i}'):
                d['upvotes'] = d.get('upvotes', 0) + 1
                save_doubts(doubts)
                st.rerun()
            st.markdown('**Answers:**')
            for ans in d['answers']:
                st.success(f"{ans['user']}: {ans['answer']}")
            with st.form(f'answer_{i}'):
                answer = st.text_input('Your Answer')
                if st.form_submit_button('Submit Answer'):
                    if answer.strip():
                        d['answers'].append({'user': st.session_state['username'], 'answer': answer})
                        save_doubts(doubts)
                        st.success('Answer submitted!')
                        st.rerun()

def show_topic_mastery():
    st.subheader('📊 Topic Mastery Progress')
    progress = load_progress()
    data = load_questions()
    topics = sorted(data.keys())
    topic_scores = {}
    for topic in topics:
        total = len(data[topic])
        # Sum all progress for this topic
        count = 0
        if isinstance(progress, dict):
            for day in progress.values():
                if isinstance(day, dict):
                    count += day.get(topic, 0)
        percent = min(100, int((count / total) * 100)) if total > 0 else 0
        topic_scores[topic] = percent
    for topic, percent in topic_scores.items():
        st.write(f"**{topic}**")
        st.progress(percent)
        st.write(f"{percent}% mastery")

RESOURCE_RECOMMENDATIONS = {
    "Arrays": [
        {"type": "YouTube", "title": "Arrays in DSA - CodeHelp", "url": "https://www.youtube.com/watch?v=Z0zB3C2p2lA"},
        {"type": "LeetCode", "title": "LeetCode Array Problems", "url": "https://leetcode.com/tag/array/"},
        {"type": "Article", "title": "GeeksforGeeks Array Data Structure", "url": "https://www.geeksforgeeks.org/array-data-structure/"}
    ],
    "Dynamic Programming": [
        {"type": "YouTube", "title": "DP Playlist - Aditya Verma", "url": "https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go"},
        {"type": "LeetCode", "title": "LeetCode DP Problems", "url": "https://leetcode.com/tag/dynamic-programming/"},
        {"type": "Article", "title": "GeeksforGeeks DP", "url": "https://www.geeksforgeeks.org/dynamic-programming/"}
    ],
    "Graph": [
        {"type": "YouTube", "title": "Graph Theory - WilliamFiset", "url": "https://www.youtube.com/playlist?list=PL2_aWCzGMAwLLTJfQPn4VgA1p_3b5hAaS"},
        {"type": "LeetCode", "title": "LeetCode Graph Problems", "url": "https://leetcode.com/tag/graph/"},
        {"type": "Article", "title": "GeeksforGeeks Graph Data Structure", "url": "https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/"}
    ],
    # ...add more topics as needed...
}

def show_resource_recommendations(topic):
    st.subheader(f"🔗 Recommended Resources for {topic}")
    resources = RESOURCE_RECOMMENDATIONS.get(topic, [])
    if not resources:
        st.info("No resources available for this topic yet.")
    for r in resources:
        st.markdown(f"- [{r['type']}: {r['title']}]({r['url']})")

FLASHCARDS = {
    "Arrays": [
        {"front": "What is the time complexity of accessing an element in an array by index?", "back": "O(1)"},
        {"front": "Which algorithm is best for finding the maximum subarray sum?", "back": "Kadane's Algorithm"}
    ],
    "Dynamic Programming": [
        {"front": "What is memoization?", "back": "Storing results of expensive function calls and returning the cached result when the same inputs occur again."}
    ],
    # ...add more topics and flashcards as needed...
}

def show_flashcards():
    st.subheader('🃏 Flashcards Mode')
    topic = st.selectbox('Choose Topic', list(FLASHCARDS.keys()))
    cards = FLASHCARDS.get(topic, [])
    if not cards:
        st.info('No flashcards for this topic yet.')
        return
    idx = st.session_state.get('flashcard_idx', 0)
    card = cards[idx % len(cards)]
    st.markdown(f"**Q:** {card['front']}")
    if st.button('Show Answer'):
        st.markdown(f"**A:** {card['back']}")
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Previous'):
            st.session_state.flashcard_idx = (idx - 1) % len(cards)
            st.rerun()
    with col2:
        if st.button('Next'):
            st.session_state.flashcard_idx = (idx + 1) % len(cards)
            st.rerun()
GROUPS_FILE = 'data/groups.json'

def load_groups():
    if not os.path.exists(GROUPS_FILE):
        return []
    with open(GROUPS_FILE, 'r') as f:
        return json.load(f)

def save_groups(groups):
    with open(GROUPS_FILE, 'w') as f:
        json.dump(groups, f, indent=2)

def show_group_study():
    st.subheader('👥 Group Study & Challenges')
    groups = load_groups()
    username = st.session_state['username']
    st.markdown('**Create or join a study group!**')
    with st.form('create_group'):
        group_name = st.text_input('Group Name')
        if st.form_submit_button('Create Group'):
            if group_name and not any(g['name'] == group_name for g in groups):
                groups.append({'name': group_name, 'members': [username], 'challenges': []})
                save_groups(groups)
                st.success('Group created and joined!')
                st.rerun()
    group_names = [g['name'] for g in groups if username not in g['members']]
    if group_names:
        join_group = st.selectbox('Join a Group', group_names)
        if st.button('Join Selected Group'):
            for g in groups:
                if g['name'] == join_group:
                    g['members'].append(username)
                    save_groups(groups)
                    st.success('Joined group!')
                    st.rerun()
    my_groups = [g for g in groups if username in g['members']]
    if my_groups:
        st.write('**Your Groups:**')
        for g in my_groups:
            st.write(f"- {g['name']} (Members: {', '.join(g['members'])})")
            with st.form(f'challenge_{g["name"]}'):
                challenge = st.text_input('New Challenge')
                if st.form_submit_button('Add Challenge'):
                    if challenge.strip():
                        g['challenges'].append({'challenge': challenge, 'by': username})
                        save_groups(groups)
                        st.success('Challenge added!')
                        st.rerun()
            if g['challenges']:
                st.write('**Group Challenges:**')
                for ch in g['challenges']:
                    st.info(f"{ch['challenge']} (by {ch['by']})")
def main():
    # Animated Title with enhanced UI
    st.markdown('''
        <h1 class="animated-title">
            <span class="emoji">👨‍💻</span> DSA_CodeMastery <span class="club">Club.AI🤖</span>
        </h1>
        <div class="animated-caption">Your AI-Powered DSA Learning Hub🚨</div>
        <style>
        .animated-title {
            font-size: 3.2em;
            font-family: 'Montserrat', 'Segoe UI', sans-serif;
            font-weight: 900;
            letter-spacing: 2px;
            margin-bottom: 0.1em;
            background: linear-gradient(90deg, #6366f1, #f472b6, #34d399, #fbbf24, #6366f1);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
            animation: rainbowText 4s ease-in-out infinite, titlePopIn 1.2s cubic-bezier(.68,-0.55,.27,1.55) 1;
            text-shadow: 0 0 18px #fff7, 0 2px 24px #a5b4fc55;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .animated-title .emoji {
            font-size: 1.2em;
            margin-right: 0.18em;
            filter: drop-shadow(0 0 8px #fee14088);
            animation: emojiBounce 2.2s infinite;
        }
        .animated-title .club {
            background: linear-gradient(90deg, #fbbf24, #6366f1, #fa709a, #43e97b);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            color: transparent;
            animation: clubGradient 3.5s ease-in-out infinite;
            text-shadow: 0 0 12px #fee14055;
        }
        @keyframes rainbowText {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        @keyframes clubGradient {
            0% {background-position: 0% 50%;}
            100% {background-position: 100% 50%;}
        }
        @keyframes emojiBounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-12px) scale(1.12); }
        }
        @keyframes titlePopIn {
            0% { opacity: 0; transform: scale(0.7) translateY(-40px); }
            80% { opacity: 1; transform: scale(1.08) translateY(6px); }
            100% { opacity: 1; transform: scale(1) translateY(0); }
        }
        </style>
    ''', unsafe_allow_html=True)
    
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'email' not in st.session_state:
        st.session_state.email = ""

    if not st.session_state.logged_in:
        auth_ui()
        return

    st.sidebar.write(f"👤 Logged in as: `{st.session_state.username}`")
    st.sidebar.write(f"📧 Email: `{st.session_state.email}`")
    AI_path = "AI.png"  # Ensure this file is in the same directory as your script
    try:
        st.sidebar.image(AI_path)
    except FileNotFoundError:
        st.sidebar.warning("AI.png file not found. Please check the file path.")

    menu = ["Take Quiz", "Track Progress", "📈 Interactive Progress", "📊 Topic Mastery", "🃏 Flashcards", "🔥 Daily Challenge", "🏅 My Badges", "💬 Doubt Forum", "👥 Group Study", "\U0001F4C5 Smart Study Scheduler","🤖 Ask DSA Doubt", "💻 Live Coding Playground", "\U0001F512 Logout"]
    choice = st.sidebar.radio("Select", menu)
    
    developer_path = "pic.jpg"  # Ensure this file is in the same directory as your script
    try:
        st.sidebar.image(developer_path)
    except FileNotFoundError:
        st.sidebar.warning("pic.jpg file not found. Please check the file path.")

    st.sidebar.markdown("👨👨‍💻Developer:- Abhishek💖Yadav")

    if choice == "Take Quiz":
        data = load_questions()
        topics = sorted(data.keys())
        selected_topic = st.selectbox("Choose a topic", topics)
        topic_questions = data[selected_topic]
        quiz_interface(selected_topic, topic_questions)

    elif choice == "Track Progress":
        show_progress()

    elif choice == "📈 Interactive Progress":
        show_interactive_progress()

    elif choice == "📊 Topic Mastery":
        show_topic_mastery()

    elif choice == "🔥 Daily Challenge":
        show_daily_challenge()

    elif choice == "🏅 My Badges":
        show_badges()

    elif choice == "\U0001F4C5 Smart Study Scheduler":
        show_scheduler()
    elif choice == "🤖 Ask DSA Doubt":
        show_chatbot()
    elif choice == "💬 Doubt Forum":
        show_doubt_forum()

    elif choice == "🃏 Flashcards":
        show_flashcards()
    elif choice == "👥 Group Study":
        show_group_study()

    elif choice == "\U0001F512 Logout":
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.email = ""
        st.success("Logged out successfully.")
        st.rerun()

    elif choice == "💻 Live Coding Playground":
        show_code_playground()

def get_weak_topics():
    progress = load_progress()
    data = load_questions()
    topics = sorted(data.keys())
    topic_scores = {}
    for topic in topics:
        total = len(data[topic])
        count = 0
        if isinstance(progress, dict):
            for day in progress.values():
                if isinstance(day, dict):
                    count += day.get(topic, 0)
        percent = (count / total) if total > 0 else 0
        topic_scores[topic] = percent
    # Weak topics: lowest %
    weak_topics = sorted(topic_scores, key=lambda t: topic_scores[t])[:2]  # Suggest 2 weakest
    return weak_topics

def show_recommendations_section():
    st.subheader('🎯 Next Best Step: Personalized Recommendations')
    weak_topics = get_weak_topics()
    if not weak_topics:
        st.info('No recommendations yet. Take a quiz to get started!')
        return
    st.write('Based on your progress, focus on:')
    for topic in weak_topics:
        st.markdown(f'- **{topic}**')
        show_resource_recommendations(topic)
        # Suggest a random question from this topic
        data = load_questions()
        if data.get(topic):
            q = random.choice(data[topic])
            st.markdown(f'> _Sample Question_: {q["question"]}')

def show_code_playground():
    st.subheader('💻 Live Coding Playground')
    st.write('Write and test your Python code for DSA problems below!')
    code = st.text_area('Your Code', height=200, key='code_playground')
    sample_input = st.text_area('Sample Input (optional)', key='sample_input')
    run_btn = st.button('Run Code')
    if run_btn:
        import sys
        import io
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        try:
            # Prepare input if provided
            if sample_input.strip():
                sys.stdin = io.StringIO(sample_input)
            exec(code, {})
            sys.stdout = old_stdout
            output = redirected_output.getvalue()
            st.success('Output:')
            st.code(output)
        except Exception as e:
            sys.stdout = old_stdout
            st.error(f'Error: {e}')
        finally:
            sys.stdout = old_stdout
            sys.stdin = sys.__stdin__
if __name__ == "__main__":
    main()