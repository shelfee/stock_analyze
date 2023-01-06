import pandas as pd
import efinance as ef
from efinance.common import get_realtime_quotes_by_fs


def get_stock_info_df() -> pd.DataFrame:
    concept = '概念板块'
    industry = '行业板块'
    bk = {
        concept: ef.stock.get_realtime_quotes(concept).set_index('股票代码', drop=False),
        industry: ef.stock.get_realtime_quotes(
            industry).set_index('股票代码', drop=False)
    }

    rows = []
    for bk_type, bk_df in bk.items():
        for bk_id, row in bk_df.iterrows():
            df = get_realtime_quotes_by_fs(f'b:{bk_id}').rename(columns={
                '代码': '股票代码',
                '名称': '股票名称',
            })
            for row2 in df.iloc:
                rows.append({
                    '股票代码': row2['股票代码'],
                    '股票名称': row2['股票名称'],
                    '板块类型': bk_type,
                    '板块名称': row['股票名称'],
                    '板块代码': bk_id,
                })
    stock_info_df = pd.DataFrame(rows)
    stock_info_df.index = stock_info_df['股票代码'].values
    return stock_info_df


# 这个函数调用一次就行 会汇总全部股票板块分布信息
df = get_stock_info_df()
df.to_csv("./stock_concept.csv", index=True, header=True)
