# Text_Summarization
This text summarization app is designed for extracting concise summaries from YouTube videos or website content. 

1) **URL Input:** Users provide the URL of a YouTube video or a website along with their Groq API key.
2) **Content Extraction:** The app retrieves the content from the provided URL. For websites, it uses BeautifulSoup to extract textual data, ensuring only meaningful content is processed.
3) **Document Conversion:** The extracted content is converted into a structured document format using LangChain, making it compatible for further processing.
4) **Prompt Preparation:** A PromptTemplate is created specifically for summarization. The template ensures the summarization task is clear and concise, typically generating a summary within 300 words.
5) **LLM (Large Language Model):** The app employs the Llama3-8b-8192 model for performing the summarization task.
6) **Summarization Chain:** A summarization chain is created using LangChain’s stuff document chain method. This chain processes the documents and generates summaries by combining them efficiently.
7) **Generating Summary:** The app utilizes the prepared chain to generate a precise and well-structured summary of the input content, providing users with an easily digestible version of the original information.

