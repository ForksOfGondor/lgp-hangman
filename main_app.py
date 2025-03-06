# Hangman Game - for La Gxoia Projekto
#
#

import streamlit as st
import random

# DEVNOTE: "code complete"
# DEVNOTE: "code complete" has been declared. Now, we can proceed to launch this app on to the cloud.

# "Faux" list of words
WORDS2 = ["python", "streamlit", "developer", "hangman", "opensource", "coding"]

# Actual list of words
WORDS = [
    "joy", "smile", "laughter", "harmony", "serenity", "delight", "bliss", "kindness", 
    "cheerful", "radiance", "sunshine", "optimism", "warmth", "compassion", "gratitude", 
    "friendship", "happiness", "peace", "love", "contentment", "hope", "positivity", 
    "celebration", "ecstasy", "euphoria", "jubilation", "glee", "elation", "merriment", 
    "exuberance", "zest", "vivacity", "wonder", "blessing", "enchantment", "fulfillment", 
    "breeze", "uplifting", "inspiration", "cheer", "gleaming", "bright", "serendipity", 
    "carefree", "affection", "lively", "sparkle", "tenderness", "wholesome", "satisfaction", 
    "jovial", "hilarity", "miracle", "tranquility", "rejoice", "exhilaration", "playfulness", 
    "lighthearted", "hopeful", "charming", "bountiful", "vibrance", "nirvana", "flourish", 
    "positivity", "kindhearted", "gentleness"
]

# you can replace this list of words with your own list of words
# just do
# WORDS = [ my_list_of_words ]


def get_display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed_letters = set()
    st.session_state.attempts = 12
    st.session_state.message = ""

#st.title("🎭 The LGP Hangman Game -- for Desktop Computers")
st.title("// 🎭 The LGP Hangman Game // 🎭")



# Display word with blanks
display_word = get_display_word(st.session_state.word, st.session_state.guessed_letters)
st.write(f"Word: {display_word}")
st.write(f"Remaining Attempts: {st.session_state.attempts}")

# Input for guessing letters
guessed_letter = st.text_input("Guess a letter:", max_chars=1).lower()

if st.button("Submit Guess"):
    if guessed_letter and guessed_letter.isalpha():  # Validate input
        if guessed_letter in st.session_state.guessed_letters:
            st.session_state.message = "You already guessed that letter!"
        elif guessed_letter in st.session_state.word:
            st.session_state.guessed_letters.add(guessed_letter)
            if set(st.session_state.word).issubset(st.session_state.guessed_letters):
                st.session_state.message = "🎉 Congratulations! You guessed the word!"
        else:
            st.session_state.guessed_letters.add(guessed_letter)
            st.session_state.attempts -= 1
            if st.session_state.attempts == 0:
                st.session_state.message = f"😢 Game Over! The word was '{st.session_state.word}'."
        
        # Rerun the app to update the display word
        st.rerun()


#if st.button("Submit Guess") and guessed_letter:
#    if guessed_letter in st.session_state.guessed_letters:
#        st.session_state.message = "You already guessed that letter!"
#    elif guessed_letter in st.session_state.word:
#        st.session_state.guessed_letters.add(guessed_letter)
#        if set(st.session_state.word).issubset(st.session_state.guessed_letters):
#            st.session_state.message = "🎉 Congratulations! You guessed the word!"
#    else:
#        st.session_state.guessed_letters.add(guessed_letter)
#        st.session_state.attempts -= 1
#        if st.session_state.attempts == 0:
#            st.session_state.message = f"😢 Game Over! The word was '{st.session_state.word}'."

# Display message
if st.session_state.message:
    st.write(st.session_state.message)
    if st.session_state.attempts == 0 or "Congratulations" in st.session_state.message:
        if st.button("Play Again"):
            st.session_state.word = random.choice(WORDS)
            st.session_state.guessed_letters = set()
            st.session_state.attempts = 12
            st.session_state.message = ""

# Show guessed letters
st.write(f"Guessed Letters: {', '.join(sorted(st.session_state.guessed_letters))}")

st.title("[~]")
st.title("// 🎭 Game's For Desktop Computers Only // 🎭")
