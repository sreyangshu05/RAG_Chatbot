import pandas as pd
from langchain.schema import Document

def load_csv(filepath: str) -> pd.DataFrame:
    """Load CSV file into DataFrame."""
    return pd.read_csv(filepath)

def dataframe_to_documents(df: pd.DataFrame) -> list:
    """Convert DataFrame rows into LangChain Documents."""
    return [
        Document(page_content=row["description"], metadata={"title": row["title"]})
        for _, row in df.iterrows()
    ]
