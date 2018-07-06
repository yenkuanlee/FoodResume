# 筆記
## SQL 語法
```
create table IF NOT EXISTS item(IID text, NAME text, composition text, other text);
insert into item values('1','apple pie','apple','');
insert into item values('1','apple pie','pie','');
insert into item values('2','mango pie','mango','');
insert into item values('2','mango pie','pie','');

SELECT md5(array_agg(md5((t.*)::varchar))::varchar)  FROM ( SELECT * FROM item where IID = '1' ORDER BY 1) AS t;
	703867ee26cd6bd87f6f2e4e3bf7de4f
SELECT md5(array_agg(md5((t.*)::varchar))::varchar)  FROM ( SELECT * FROM item where IID = '2' ORDER BY 1) AS t;
	0bc54b2b66a9173aa41f15be693d4bb0
	
create table transaction(TID text, IID text, Ihash text, Ufrom text, Uto text, Date text, other text);
insert into transaction values('101','1','703867ee26cd6bd87f6f2e4e3bf7de4f','A','B','20180706','');
insert into transaction values('101','2','0bc54b2b66a9173aa41f15be693d4bb0','A','B','20180706','');

SELECT md5(array_agg(md5((t.*)::varchar))::varchar)  FROM ( SELECT * FROM transaction where TID = '101' ORDER BY 1) AS t;
	ccc94d06cc4c333cf5f335f661d4244f
	
上區塊鏈欄位
	TID
	Thash
	Ufrom
	Uto
	Date
```
	
## 執行方法
```
# 登錄成品
python record_item.py 1 "apple pie" apple null
python record_item.py 1 "apple pie" pie null
python record_item.py 2 "mango pie" mango null
python record_item.py 2 "mango pie" pie null

# 登錄出貨
python record_transaction.py 101 1 A B 20180706 null
python record_transaction.py 101 2 A B 20180706 null

# 上區塊鏈
python push_to_chain.py 101
```
