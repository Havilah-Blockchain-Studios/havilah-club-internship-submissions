# Day 14 Assignment: Python API & JSON Processing Data Engine

A command-line interface (CLI) application built in Python that interfaces with the **Open Food Facts API** to look up global grocery items and brands. The application features persistent user querying via loops and handles complex data structures through dictionary mapping.

# Features

- **Persistent Query Engine**: Utilizes a interactive `while` loop allowing continuous searches without restarting the script.
- **Robust Exception Handling**: Captures network-level interruptions including custom tracking for connection failures, timeouts, and `503 Server Unavailable` statuses.
- **Explicit Dictionary Data Extraction**: Transforms JSON payload elements into customized local dictionary keys (`item_name`, `brand_name`, `net_quantity`, `nutrition`) for structured tracking.
- **No Credentials Required**: Uses optimized request headers and an open-access public database configuration completely bypassing the need for a `.env` API file setup.

---

# Prerequisites & Installation

Make sure you have Python 3 installed on your machine. You will need the standard third-party library `requests` to manage API handshakes.

1. **Install required dependencies** via your terminal:
   ```bash
   pip install requests
   ```

2. **Run the script**:
   ```bash
   python your_script_name.py
   ```

---

# How to Use

1. Launch the application inside your system terminal or IDE window.
2. Enter any valid grocery item name or major global brand (e.g., *Nutella*, *Oreo*, *Soda*).
3. The engine will retrieve up to 3 matches and cleanly map out their manufacturing brand, net volume, and nutritional ratings.
4. Type **`exit`** at any query prompt to gracefully close out the session.

---

# Sample Visual Terminal Output

```text
--- Open Food Facts Catalog Query Engine ---

Available options: Type a grocery item, or type 'exit' to quit.
Enter a grocery item or brand (e.g., Nutella, Oreo): Oreo

=== Found 423 Global Products (Displaying Top 3) ===

[1] Item: Oreo Original
    • Manufacturer/Brand: Oreo, Nabisco
    • Net Quantity: 154 g
    • Nutrition Grade: E
--------------------------------------------------

[2] Item: Oreo Double Stuf
    • Manufacturer/Brand: Oreo
    • Net Quantity: 432g
    • Nutrition Grade: E
--------------------------------------------------

[3] Item: Oreo Minis
    • Manufacturer/Brand: Nabisco, Oreo
    • Net Quantity: 115g
    • Nutrition Grade: E
--------------------------------------------------

Available options: Type a grocery item, or type 'exit' to quit.
Enter a grocery item or brand (e.g., Nutella, Oreo): exit
Exiting search engine. Goodbye!
```
