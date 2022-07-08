import tabula
import pandas as pd

def out_columns(column, limite):
    out_column = []
    for item in column[1:limite]:
        out_column.append(item)
    
    return out_column

pdf_path =  "SPA.BULK.CA.2_reduced.pdf"

dfs = tabula.read_pdf(pdf_path, pages='1')

df = pd.DataFrame(dfs[1])
print(df)

lista = df['Per Batch Total Qty.']
column = df['Unnamed: 0']
#print(len(lista))
start = 1
end = len(lista) -1
quantities = []
qty_pick = []
for item in lista[start:end]:
    qty, units = item.split(' ')
    final_amount = float(qty) * 20
    final_amount = f"{final_amount:,.2f}"
    quantities.append(qty)
    qty_pick.append(final_amount)

out_column = out_columns(column, end)

data = {
    '| Item |': out_column,
    '| Per Batch Qty |': quantities,
    '| Qty to Pick |': qty_pick
}
index = range(101, 110)
df_output = pd.DataFrame(data, index=index)

print(f"\n\n{df_output}")