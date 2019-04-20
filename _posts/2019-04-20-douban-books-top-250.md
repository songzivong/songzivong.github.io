---
layout: post
title: "如何使用 Python 抓取豆瓣书籍数据并制作书籍排行榜"
date: 2019-04-20 19:35:04 +0800
categories: Notes
tags: douban python
math: true
---

豆瓣书籍的排序方式真的是一个迷，因此我决定自己写一个 Python 脚本去抓取豆瓣书籍数据，并根据[贝叶斯平均](https://en.wikipedia.org/wiki/Bayesian_average)得出一个 Top 250 排行榜。

## 算法

贝叶斯平均公式：

$$
\bar{x}=\frac{Cm+\sum^{n}_{i=1}x_i}{n+C}
$$

其中 $C$ 是一个反应数据集大小的数。对比一下贝叶斯平均和通常的算术平均 $\frac{\sum^{n}_{i=1}x_i}{n}$，可以发现贝叶斯平均相当于给每个项目增加 $C$ 张选票，每张票的面值为 $m$。它的意义是为了防止某些项目因为投票人数太少而使得评分不太可信。

我们可以设 $C$ 为每个项目的平均投票人数，$m$ 为每张选票的平均值。相信这是一个合理的设定。

下面是 Python 实现：

```python
aters = 0
rating = 0
for book in books:
    raters += book.raters
    rating += book.avg_rating * book.raters
avg_raters = raters / len(books)
avg_rating = rating / raters
for book in books:
    book.bayes_avg = (avg_raters * avg_rating + book.avg_rating * book.raters) / (book.raters + avg_raters)
```

## 数据抓取

我们使用[豆瓣 Open API](https://github.com/xsbailong/douban-api)去抓取数据。

例如搜索 `python`，则访问 [`https://api.douban.com/v2/book/search?q=python`](https://api.douban.com/v2/book/search?q=python)，它可能会返回一条错误信息：

```json
{"msg":"invalid_apikey","code":104,"request":"GET \/v2\/book\/search"}
```

此时我们可以带上 apikey 去访问 URL：[`https://api.douban.com/v2/book/search?apikey=0b2bdeda43b5688921839c8ecb20399b&q=python`](https://api.douban.com/v2/book/search?apikey=0b2bdeda43b5688921839c8ecb20399b&q=python)。

我们可以简单看一看它返回的数据结构：

```json
{
    "count":20,
    "start":0,
    "total":2108,
    "books":[
        {
            "rating":{
                "max":10,
                "numRaters":1523,
                "average":"9.1",
                "min":0
            },
            ...
            "alt":"https://book.douban.com/subject/26829016/",
            ...
            "title":"Python编程",
            ...
        },
        ...
    ]
}
```

`count` 表示该页的项目数量，即 `books` 的长度；`start` 表示该页数据的起始项索引；`total` 表示总的项目数量。如果我们要获取第二页的数据，可以访问 [`https://api.douban.com/v2/book/search?apikey=0b2bdeda43b5688921839c8ecb20399b&q=python&start=20`](https://api.douban.com/v2/book/search?apikey=0b2bdeda43b5688921839c8ecb20399b&q=python&start=20)，以此类推。

### Python 实现

我们可以使用 `urllib.request` 模块去获取 URL 返回的内容。

```python
import urllib
from urllib import parse
from urllib import request

def search(url, text, start=0):
    fp = request.urlopen(url + '&q=' + parse.quote(text) + '&start=' + str(start))
    content = fp.read().decode("utf8")
    fp.close()
    return content
```

然后就是用 `json` 模块解析返回的数据。

```python
import json

def parse_data(data, records):
    for b in data['books']:
        raters = b['rating']['numRaters']
        rating = float(b['rating']['average'])
        if raters > 0:
            book = Book()
            book.avg_rating = rating
            book.raters = raters
            book.title = b['title']
            book.url = b['alt']
            records.append(book)
    return data['start'], data['count'], data['total']

def search_and_parse(url, records, text, start=0):
    return parse_data(json.loads(search(url, text, start)), records)
```

## 全部代码

[`top_books.py`](https://github.com/songzivong/hello-world/blob/master/douban/top_books.py)
