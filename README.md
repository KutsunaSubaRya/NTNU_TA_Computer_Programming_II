# 111-2 NTNU_TA_Computer_Programming_II

## HW01

* [題目連結](https://drive.google.com/file/d/1GtQG4ZFi-GkuAun4insExypWhXxStdR9/view)
* [講解此次作業的 Blog 連結](https://blog.subarya.me/2023/04/06/%5B2023%20NTNU%20%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E4%BA%8C%5D%20%E5%8A%A9%E6%95%99%E6%89%B9%E6%94%B9%E8%A7%A3%E9%87%8B%20-%20%E4%BD%9C%E6%A5%AD%E4%B8%80/)

整體我使用 `recvSignal` 和 `handle_alarm` 去判斷是否有 `SIGSEGV` (segmentation fault) 和 `SIGALRM` (例如 infinie loop) 的問題導致無法繼續評測其他筆測資。
撰寫上述功能主要是在維護同學們的評分權益(可以想成您有其中一筆測資或其中一支 function 出現上述情況，可能導致 `hw010x.c` 無法繼續對其他筆測資或 function 評測，進而導致後面的測資和辛苦實作完的 function 無法評測到。但使用上述的方法可以繞過這些問題並針對您有撰寫且正確的部分評分)
### hw0101

自行評測時需要 `str1~3.txt`、`subaryaString.h`、`subaryaStrtokAnsOther.txt`、`subaryaStrtokAnsSunny.txt`、`hw0101.c` 放入到跟您實作的 .h 檔同目錄層下，接著就可以編譯並執行囉。

### hw0102

自行評測時需要 ans 資料夾、otherCase 資料夾、sunnyCase 資料夾、、`hw0102.c` 、放入到跟您實作的 .h 檔同目錄層下，接著就可以編譯並執行囉。

## HW02

* [題目連結](https://drive.google.com/file/d/1dDL0CW_nSeGBl32YkNlW6scxllj2rXta/view)

## hw0205

這份的 jsonLog 是透過 [jc](https://github.com/kellyjonbrazil/jc) parse 出的 jsonLog.json，再使用 Python 將 [題目](https://drive.google.com/file/d/1dDL0CW_nSeGBl32YkNlW6scxllj2rXta/view) 所指定的部分以 list 過濾出來並寫進 `contribution.txt`

如果有要自行測試 git log 其他專案並使用 [jc](https://github.com/kellyjonbrazil/jc) parse to json 的，這裡注意一點，[jc](https://github.com/kellyjonbrazil/jc) 目前的 `1.23.1` 版本 git log parse 是有問題的，我也有提出 [issue](https://github.com/kellyjonbrazil/jc/issues/395) 並收到下個 release 會 fix 的回覆，因此這裡再特地提醒想自行測試的同學們。
* 使用 [jc](https://blog.kellybrazil.com/2022/05/17/easily-convert-git-log-output-to-json/) 將 git log parse 成 json 的方法。
``` bash
# in your repo directory layer and you will get jsonLog.json
$ git log --format=fuller --stat | jc --git-log -p > jsonLog.json
```