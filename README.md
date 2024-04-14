
https://github.com/MikeDong2023/Full-Stack-AI-Integration/assets/138845168/666117e2-14a3-4bc2-8c18-20cb176e4a41

Inspiration: 
It's easy to lose files when you don't remember their name, or if they were named something non-descriptive in the first place (img01232139???). If your file is a video, image, or audio recording, you can't search for words in your file either. Archive solves this problem.

What it does: 
Using Gemini, Archive stores embeddings that describe the content of each file in your Drive. When you provide Archive with a simple description of the file you're searching (e.g., "that time I was playing soccer"), Archive returns all relevant files -- video, image, audio included -- in order of how strongly they match your query. With Archive, never lose a file again!

How we built it / How it works: 
Gemini is the most important part of our tool. For any image, video, or audio file in a user's Drive, Gemini first provides a detailed summary of what's going on in the file. Then, our tool prompts Gemini to generate word embeddings of its own summary, and we store these embeddings in a database. Finally, when a user provides a semantic description of what they're searching, we compare the query to these stored embeddings (using cosine similarity) and return the strongest matching results.

Challenges we ran into: 
Some challenges included figuring out performant summarization prompts for image, video, and audio file types, figuring out how to use the Google Drive API, and so forth.

What we learned: 
We learned so much in this project. We learned how to use Gemini's powerful video, image, and text summarization features, and we learned how text embeddings can be used for content search and semantic matching. But most of all, we learned how to have fun with AI!

What's next for Archive: 
We believe there are several possible futures for Archive, either as a standalone tool compatible with a variety of file environments (Drive, desktop, local, etc.) or as a feature adopted by Google itself to become natively integrated into Drive. Not only that, but there are plenty of more ideas we have for additional functionalities, like conversational file searching or related-file recommendations. With Gemini, the sky is the limit.

Built With: 
colab, 
flask, 
gemini, 
python, 
react.

SUBMITTED TO Google x MHacks AI Hackathon

