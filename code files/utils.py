import json
import re
from typing import Optional

def clean_text(text: str) -> str:
    """Clean and normalize whitespace, newlines."""
    return re.sub(r'\s+', ' ', text).strip()

def validate_title(title: Optional[str]) -> Optional[str]:
    if title and isinstance(title, str) and len(title) > 1:
        return clean_text(title)
    return None

def validate_year(year_text: Optional[str]) -> Optional[int]:
    if not year_text:
        return None
    # Extract year as 4 digits number
    match = re.search(r'(\d{4})', year_text)
    if match:
        year = int(match.group(1))
        if 1900 <= year <= 2025:
            return year
    return None

def validate_rating(rating_text: Optional[str]) -> Optional[float]:
    try:
        rating = float(rating_text)
        if 0.0 <= rating <= 10.0:
            return rating
    except (ValueError, TypeError):
        return None

def save_to_json(data: list, file_path: str):
    """Append list of dicts to a JSON file."""
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            for entry in data:
                json.dump(entry, f, ensure_ascii=False)
                f.write('\n')
    except Exception as e:
        print(f"Error saving JSON: {e}")
