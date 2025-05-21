Chat Log Summarizer
=================

This Python script analyzes chat logs between a User and an AI, providing a concise summary of the conversation.

Features
--------
- Parses chat logs with User and AI messages
- Calculates message statistics (total messages, messages per speaker)
- Extracts most common keywords from the conversation
- Generates a comprehensive summary of the chat

Requirements
-----------
- Python 3.x
- No additional packages required (uses standard library only)

How to Run
---------
1. Make sure Python is installed on system
2. Place your chat log file in the same directory as the script
3. The chat log should be in the following format:
   ```
   User: Hello, how are you?
   AI: I'm doing well, thank you for asking.
   User: Can you help me with something?
   AI: Of course, I'd be happy to help.
   ```
4. Run the script using Python:
   ```
   python task.py
   ```

Sample Output
------------
```
Summary:
- The conversation had 4 exchanges.
- User sent 2 messages and AI sent 2 messages.
- Most common keywords: help, hello, well, thank, happy
- Nature of the conversation: help, hello, well, thank, happy.
```

File Structure
-------------
- task.py: Main script containing the chat analysis code
- chat.txt: Input file containing the chat log (we need to create this)
- README.md: This documentation file

Notes
-----
- The script assumes the chat log file is named "chat.txt"
- Messages must be prefixed with either "User:" or "AI:"
- The script will automatically filter out common English stop words
- By default, it extracts the top 5 most frequent keywords

Error Handling
-------------
- If the chat file is not found, the script will display an error message
- The script handles basic file reading errors gracefully

Customization
------------
You can modify the following parameters in the code:
- Number of keywords to extract (default: 5)
- Stop words list (can be customized)
- Input file name (in the main block) 