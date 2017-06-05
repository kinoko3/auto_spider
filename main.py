import xlrd, os
from login import login
from xlutils.copy import copy

filename = input('输入Excel文件名:')
data = xlrd.open_workbook(filename)
sheet_name = data.sheet_names()
table = data.sheets()[0]
ncols = table.ncols
ID = table.col_values(0)
user_name = table.col_values(2)
ID_card = table.col_values(4)
long = len(ID)
data_list = []


for a in range(1, long):
    Login = login(ID=int(ID[a]), user_name=user_name[a], ID_card=ID_card[a])
    text = Login.main()
    data_list.append(text)



for b in range(1, long):
    new_data = xlrd.open_workbook('gjf.xlsx')
    wb = copy(new_data)
    ws = wb.get_sheet(0)
    ws.write(b, 5, data_list[b-1])  # 行,列，列写死
    wb.save('gjf.xlsx')



files = os.listdir(".")
for filename in files:
    portion = os.path.splitext(filename)
    print(portion[1])
    if portion[1] == '.xlsx':
        newname = portion[0]+".xls"
        os.rename(filename, newname)







