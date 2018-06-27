# 智能合約操作說明

## 流程
```
1. 察看進貨 (GetNotice)
  $ python3 function.py gmeal GetNotice

2. 收貨 (FillItem)
  $ python3 function.py gmeal FillItem QmV9QCiePCQQzqK3UdaDs3XF7Fgz4v9RcLrsGnCiUhriMV

// 製作新物件 (不在鏈上)

3. 登錄 (PushItem)
  $ python3 function.py supplier PushItem QmaWK5yfXVQbYK8A3RoyQnza2ThaXTuuJHZREEJ9jQcKLA

4. 出貨 (SendNotice)
  $ python3 function.py supplier SendNotice QmV9QCiePCQQzqK3UdaDs3XF7Fgz4v9RcLrsGnCiUhriMV 0xe6ab871f860d9f28764d5d2e0672396a7643710e
```

## 查詢
```
1. 查詢物件 (GetStringInfo)
  $ python3 function.py supplier GetStringInfo

2. 查詢物件流向 (GetStringItemFlow)
  $ python3 function.py gmeal GetStringItemFlow QmV9QCiePCQQzqK3UdaDs3XF7Fgz4v9RcLrsGnCiUhriMV
```
