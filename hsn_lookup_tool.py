from google.adk.tools import FunctionTool
import pandas as pd
from typing import Tuple

# Load the Excel file once when the module loads
df = pd.read_excel("data/HSN_SAC.xlsx", sheet_name="HSN_MSTR")
df.columns = df.columns.str.strip()
df['HSNCode'] = df['HSNCode'].astype(str).str.strip()
df['Description'] = df['Description'].astype(str).str.strip()

def validate_format(code: str) -> Tuple[bool, str]:
    """Check if the HSN code format is valid."""
    if not code.isdigit():
        return False, "Invalid format: code must be numeric"
    if len(code) < 2 or len(code) > 8:
        return False, "Invalid format: length must be 2 to 8 digits"
    return True, ""

@FunctionTool
def hsn_lookup(hsn_codes: str) -> str:
    """
    Look up one or more HSN codes (comma or space separated) and return
    validation and description results.
    """
    codes = [c.strip() for c in hsn_codes.replace(",", " ").split()]
    results = []

    for code in codes:
        # Format validation
        valid_format, err_msg = validate_format(code)
        if not valid_format:
            results.append(f"❌ HSN code {code}: {err_msg}")
            continue

        # Existence validation
        match = df[df['HSNCode'] == code]
        if not match.empty:
            desc = match.iloc[0]['Description']
            results.append(f"✅ HSN code {code} is valid: {desc}")
        else:
            results.append(f"❌ HSN code {code} is not found in the dataset.")

    return "\n".join(results)
