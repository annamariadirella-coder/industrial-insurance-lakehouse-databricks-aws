def explain_with_title(df, title):
    print("=" * 100)
    print(title)
    print("=" * 100)
    df.explain(True)
