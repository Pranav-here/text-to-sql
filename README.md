# Natural-Language to SQL Playground

A simple Streamlit app that converts plain-English queries into SQL commands and runs them against a SQLite database.  
This tool is database-agnostic—you can swap out the example with any table and schema you prefer.

## Features

- **Natural Language → SQL**: Leverage an LLM (e.g. Groq’s `gemma2-9b-it`) to translate English questions into SQL.
- **Lightweight**: Uses SQLite under the hood; no heavy RDBMS setup.
- **Interactive UI**: Built with Streamlit for quick experiments.
- **Customizable**: Adjust the system prompt to match your database schema.

## Example

Given a table called `CRICKETER`:
| PLAYER_NAME        | TEAM        | ROLE         | RUNS  | WICKETS |
|--------------------|-------------|--------------|-------|---------|
| Virat Kohli        | India       | Batter       | 27599 | 9       |
| Mitchell Starc     | Australia   | Bowler       |  2986 | 718     |
| Ben Stokes         | England     | All-rounder  | 10829 | 318     |
| …                  | …           | …            |   …   | …       |

Ask: **“List each team’s total runs across all its players, ordered from highest to lowest total.”**  
→ SQL:
```sql
SELECT TEAM, SUM(RUNS) AS total_runs
FROM CRICKETER
GROUP BY TEAM
ORDER BY total_runs DESC;
```

Query Results:

| TEAM        | total_runs |
|-------------|------------|
| India       |      72048 |
| Australia   |      55589 |
| England     |      50228 |
| New Zealand |      28154 |
| Pakistan    |      12888 |
| Sri Lanka   |       2154 |
| South Africa|       1161 |

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/pranav-here/text-to-sql.git
   cd your-repo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Groq API key:
   ```bash
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run main.py
```

- Open the URL shown in your browser.
- Type a plain-English question about your database schema.
- Hit **Run Query** to see the generated SQL and results.

## Configuration

- **Prompt Tuning**: Modify the system prompt in `main.py` to reflect your own table names and columns.
- **Database**: Swap `cricket.db` for any other SQLite file, or adapt `get_data_from_database()` to point at a different RDBMS.

## Contributing

1. Fork the repo  
2. Create your feature branch (`git checkout -b feature/YourFeature`)  
3. Commit your changes (`git commit -m 'Add feature'`)  
4. Push to the branch (`git push origin feature/YourFeature`)  
5. Open a Pull Request  

## License

MIT © Your Name
