import pandas as pd


def import_data(filename: str) -> pd.DataFrame:
    df = pd.read_excel(filename)
    return df
#print(import_data("Online Retail.xlsx"))


def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    filter1 = df["CustomerID"].isna()
    filter2 = df["Quantity"] < 0
    filter3 = df["UnitPrice"] < 0
    filter_data = df[~filter1 & ~filter2 & ~filter3]
    return filter_data

    # df = df[~df["CustomerID"].isna()]
    # df = df[(df["Quantity"] >=0 ) & (df["UnitPrice"] >= 0 )]
    # return df


def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    customer_loyalty = df.groupby("CustomerID").size().reset_index(name="Quantity")
    loyal_customers = customer_loyalty[customer_loyalty['Quantity'] >= min_purchases]
    loyal_customers.columns = ["CustomerID", "Quantity"]
    return loyal_customers

    # df["TotalSpending"] = df["Quantity"] * df["UnitPrice"]
    # customer_spending = df.groupby("CustomerID")["TotalSpending"].sum()
    # min_customers_df = customer_spending.sort_values(ascending=True).head(min_purchases).reset_index()
    # return min_customers_df

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df["date"])
    df["quarter"] = df["date"].dt.to_period("Q")
    result = df.groupby("quarter")["revenue"].sum().reset_index()
    result.columns = ["quarter", "total_revenue"]
    return result

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    product_sales = df.groupby("ProductID")["Quantity"].sum().reset_index()
    top_products = product_sales.sort_values(by="Quantity", ascending=False).head(top_n)
    top_products.columns = ["ProductID", "Quantity"]
    return top_products

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    purchase_patterns = df.groupby("ProdectID").agg(
        avg_quantity=("Quantity", "mean"),
        avg_unit_price=("UnitPrice", "mean")
    ).reset_index()
    purchase_patterns.columns = ["ProductID", "avg_quantity", "avg_unit_price"]
    return purchase_patterns

def answer_conceptual_questions() -> dict:
    answers = {
        "Q1": {"A"},
        "Q2": {"B"},
        "Q3": {"C"},
        "Q4": {"A"},
        "Q5": {"A"},
    }
    return answers