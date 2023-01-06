import pandas as pd
import efinance as ef

stock_concepts = pd.read_csv("stock_concept.csv")
concept_dic = {}
for _, row in stock_concepts.iterrows():
    t, n, c = row['板块类型'], row['板块名称'], row['板块代码']
    if t not in concept_dic:
        concept_dic[t] = {}
    if n not in concept_dic[t]:
        concept_dic[t][n] = c

for concept_type in concept_dic:
    codes = list(concept_dic[concept_type].values())
    daily_quota_history = ef.stock.get_quote_history(codes)
    print()

a = ef.stock.get_history_bill("BK0485")
b = ef.stock.get_quote_history('BK0485')

print(a)