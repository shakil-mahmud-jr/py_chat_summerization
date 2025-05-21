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


def extract_keywords(messages, num_keywords=5, stop_words=None):
    """
    Extracts the top most frequent words from messages, excluding stop words.
    """
    if stop_words is None:
        stop_words = set([
            'the', 'a', 'an', 'is', 'it', 'in', 'of', 'and', 'to', 'for', 'with',
            'on', 'by', 'as', 'at', 'this', 'that', 'be', 'have', 'i', 'you',
            'he', 'she', 'it', 'we', 'they', 'what', 'where', 'when', 'why',
            'how', 'can', 'will', 'would', 'should', 'could', 'do', 'does',
            'did', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'say', 'says', 'said',
            'go', 'goes', 'went', 'get', 'gets', 'got', 'make', 'makes',
            'made', 'know', 'knows', 'knew', 'think', 'thinks', 'thought',
            'take', 'takes', 'took', 'see', 'sees', 'saw', 'come', 'comes',
            'came', 'want', 'wants', 'wanted', 'look', 'looks', 'looked',
            'use', 'uses', 'used', 'find', 'finds', 'found', 'give', 'gives',
            'gave', 'tell', 'tells', 'told', 'ask', 'asks', 'asked', 'work',
            'works', 'worked', 'seem', 'seems', 'seemed', 'feel', 'feels',
            'felt', 'leave', 'leaves', 'left', 'call', 'calls', 'called',
            'about', 'above', 'after', 'again', 'against', 'all', 'any',
            'around', 'because', 'before', 'below', 'between', 'both', 'but',
            'by', 'down', 'from', 'here', 'into', 'more', 'most', 'other',
            'out', 'over', 'same', 'some', 'such', 'than', 'then', 'there',
            'these', 'they', 'this', 'those', 'through', 'until', 'up',
            'very', 'what', 'when', 'where', 'which', 'while', 'who', 'whom',
            'why', 'with', 'you', 'your'
        ])

    all_text = ' '.join(msg['message'] for msg in messages)
    words = re.findall(r'\b\w+\b', all_text.lower())
    word_counts = Counter(word for word in words if word not in stop_words)

    return [word for word, count in word_counts.most_common(num_keywords)]




def generate_summary(statistics, keywords):
    """
    Generates a summary string based on statistics and keywords.
    """
    summary = "Summary:\n"
    summary += f"- The conversation had {statistics['total']} exchanges.\n"
    summary += f"- User sent {statistics['User']} messages and AI sent {statistics['AI']} messages.\n"
    summary += f"- Most common keywords: {', '.join(keywords)}\n"
    summary += "- Nature of the conversation: " + ", ".join(keywords) + ".\n"

    return summary



if __name__ == "__main__":
    chat_file = "chat.txt"
    messages = parse_chat_log(chat_file)

    if messages:
        stats = analyze_message_statistics(messages)
        keywords = extract_keywords(messages)
        summary = generate_summary(stats, keywords)

        print(summary)
    else:
        print("Could not process chat log.")
