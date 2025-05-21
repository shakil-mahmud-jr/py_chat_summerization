import re
from collections import Counter

def parse_chat_log(file_path):
    """
    Reads a chat log file and parses messages by speaker.
    """
    messages = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    speaker_match = re.match(r'(User|AI):\s*(.*)', line)
                    if speaker_match:
                        speaker = speaker_match.group(1)
                        message = speaker_match.group(2)
                        messages.append({'speaker': speaker, 'message': message})
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    return messages

def analyze_message_statistics(messages):
    """
    Calculates total messages and messages per speaker.
    """
    total_messages = len(messages)
    user_messages = sum(1 for msg in messages if msg['speaker'] == 'User')
    ai_messages = total_messages - user_messages

    return {
        'total': total_messages,
        'User': user_messages,
        'AI': ai_messages
    }