import re
from youtube_transcript_api import (
    YouTubeTranscriptApi, 
    TranscriptsDisabled, 
    NoTranscriptFound, 
    VideoUnavailable
)
from groq import Groq
import streamlit as st 

# Regular Expression for YouTube URL
def get_id(url):
    match = re.search(
        r"^https?://(www\.|m\.)?(youtube.com/|youtu.be/)(watch\?.*v|shorts|embed|live)?(=|/)?(?P<id>[a-zA-Z0-9_-]{11}).*",
        url,
    )
    return match.group("id") if match else "Failed to find ID"

# Initialize attempts
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

st.title("YouTube Summarizer 🎬")

# If attempts are maxed out, show reset option
if st.session_state.attempts >= 3:
    st.error("You have reached the limit of 3 errors. Please reset to try again.")
    if st.button("🔄 Reset Application"):
        st.session_state.attempts = 0
        st.rerun() # This command reloads the page perfectly!
else:
    url = st.text_input("Enter YouTube URL")

    if st.button("Summarize"):
        try:
            # 1. Validate ID
            video_id = get_id(url)
            if video_id == "Failed to find ID" or not url:
                raise ValueError("URL not valid or not found.")

            # 2. Fetch Transcript
            ytt_api = YouTubeTranscriptApi()
            data = ytt_api.fetch(video_id)
            whole_data = [sentence.text for sentence in data.snippets]
            long_paragraph = " ".join(whole_data)[:15000]

            # 3. AI Summary
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            my_prompt = f"""
You are an expert content analyzer. Read the following YouTube video transcript and automatically detect its genre and tone (e.g., educational, comedy, sports, religious, etc.). 

CRITICAL RULE: Write your entire response using **the simplest English possible**. Use short sentences, common everyday words, and clear explanations. Avoid difficult or fancy vocabulary so that anyone can easily understand it.

Adapt your style to match the vibe of the video:
- If it's funny, keep it light and fun.
- If it's educational, keep it clear and easy to follow.
- If it's sports, keep it energetic.
- If it's religious, keep it respectful and calm.

Please organize your response into:
1. **The Vibe & Overview:** What kind of video this is and a quick, simple summary.
2. **Key Highlights / Takeaways:** Bullet points using easy words matching the tone of the video.
3. **The Best Moment:** The most standout part of the video explained simply.

Transcript:
{long_paragraph}
"""
           
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": my_prompt}]
            )

            st.success("Summary Generated!")
            st.write(response.choices[0].message.content)

        # Increment attempts ONLY when an error occurs
        except (ValueError, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
            st.session_state.attempts += 1
            st.warning(f"⚠️ {e} (Errors: {st.session_state.attempts}/3)")
            
        except Exception as e:
            st.session_state.attempts += 1
            st.error(f"An unexpected error occurred: {e}")