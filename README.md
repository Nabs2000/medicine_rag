# Medicine RAG Project
This project is dedicated to obtaining insights from medicine data using a RAG approach.
## Preliminary Steps
1. Clone the repository
```bash
git clone https://github.com/Nabs2000/medicine_rag.git
```

2. Download the data from the following links and store them in the `data` directory: 
- [Medicine Data (CSV)](https://www.kaggle.com/datasets/ujjwalaggarwal402/medicine-dataset)
- [Amoxicillin Data (PDF)](https://en.wikipedia.org/wiki/Amoxicillin)

3. Install the necessary libraries using the following command:
```bash
pip install -r requirements.txt
```
4. Create an `.env` file in the root directory and add an `OPENAI_API_KEY` variable with your OpenAI API key.
```env
OPENAI_API_KEY=your_openai_api_key
```