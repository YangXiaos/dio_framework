# **1. 采集系统需求**
## 1.1 爬虫任务场景
多爬虫分布式采集系统。
1. 满足监控任务场景。
2. 满足异步任务场景。
  1. 项目管理异步任务场景。`
3. 满足界面化配置爬虫。
4. 爬虫状态监控信息。
5. 集群/Runner监控状态。
## 1.2 术语定义
站点：某些依赖于同一个站点的爬虫集合。
任务：定期或一次性的跑数任务。
监控任务：对某个站点某个板块的定时监控任务。
异步任务：利用分布式集群的一次性跑数任务。
任务种子（Job）：调度中心产生的爬虫作业种子。
爬虫项目：多个异步执行的任务的集合。
爬虫模板：针对某种特定页面的爬虫配置。
爬虫种子：爬虫产生的种子。
#
# 2. 数据库配置
## 2.1 redis系统配置
### 2.1.1 Scheduler用生产队列
Scheduler 监控任务 种子调度队列：
| key名 | dio.scheduler.job.seeds.queue |
|
| 类型 | List |
| 元素 | json形式的种子字符串 |


Scheduler 异步任务 异步任务种子调度队列：
| key名 | dio.scheduler.async.seeds.queue |
|
| 类型 | List |
| 元素 | json形式的种子字符串 |


Scheduler 监控任务时间运行记录表：
| key名 | dio.scheduler.task.inc.record |
|
| 类型 | Hash |
| 元素 | {"task_id" : "20141208122120"} |


### 2.2.2 Runner用生产队列

site级别的去重队列，根据站点id下的队列进行去重：
| key名 | dio.crawler.site.seeds.set.{site_id} |
|
| 类型 | Set |
| 元素 | String形式的 url |


task级别的去重队列，根据任务id进行去重：
| key名 | dio.crwaler.task.seeds.set.{task_id} |
|
| 类型 | Set |
| 元素 | String形式的 url |


Gobal级别的去重库：
| key名 | dio.crwaler.global.seeds.set |
|
| 类型 | Set |
| 元素 | url的MD5加密字符串 |


job用的线程状态队列：
| key名 | dio.crawler.job.{job_id} |
|
| 类型 | Hash |
| 元素 | { "thread_id": 0, "thread_id": 2 } |


runner 状态表
| key名 | dio.crawler.runner |
|
| 类型 | Hash |
| 元素 | { "runner_id": 0, "runner_id": 1 } |


Runner的对应的工作job状态表 runnerId: job_id
| key名 | dio.crawler.runner.job |
|
| 类型 | Hash |
| 元素 | job_id |


async异步任务 seeds队列
| key名 | dio.crawler.async.seeds.{job_id} |
|
| 类型 | List |
| 元素 | 种子json 字符串队列 |


## 2.2 Mysql 系统配置
>站点配置表(dio.site.config)：站点信息，用于整合爬虫。
| 字段名 | 类型 | 备注 | 默认 |
|
| id | int |    | 自增 |
| desc | varchar | 站点备注 |    |
| domain | varchar | 域名 |    |
| parent_id | varchar | 父级站点id | null |
| tag | varchar | 标签 |    |
| status | int | 是否可用 | 0 |
| db_config | varchar | 数据库配置 |    |


>爬虫任务配置表(dio.task.config)：爬虫任务配置
| 字段名 | 类型 | 备注 | 默认 |
|
| id | int |    | 自增 |
| site_ids | varchar | 站点列表 | -1 |
| message_processor_config | varchar | 爬虫处理器配置 |    |
| job_processor_params | varchar | 作业处理器 |    |
| scheduler_params | varchar | 调度参数 |    |
| is_available | int | 状态，0为正常，1为gg |    |
| template_ids | varchar | 爬虫模板id列表 |    |
| desc | varchar | 任务名 |    |
| type | varchar | 任务类型 |    |
| cycle_time | int | 运行周期，分钟 |    |


>爬虫模板配置表(dio.template.config)：爬虫模板配置
| 字段名 | 类型 | 备注 | 默认 |
|
| id | int |    | 自增 |
| desc | varchar | 模板名 |    |
| type | varchar | 模板类型 |    |
| site_ids | varchar | 站点列表 | -1 |
| template_component_config | varchar | 处理器配置 |    |
| message_match_strategy_config | varchar | 匹配策略配置 |    |


>爬虫作业表(dio.job)：用于记录爬虫的任务信息
| 字段名 | 类型 | 备注 | 默认 |
|
| id | int |    | 自增 |
| task_id | int | 任务id | -1 |
| template_ids | varchar | 模板ids |    |
| report | varchar | 报告 |    |
| state | varchar | 爬虫状态，0为success，1 为 fail |    |
| crawl_num | int | 抓取数据量 | 0 |
| fail_num | int | 失败数据量 | 0 |
| link_num | int | 链接种子数据量 | 0 |
| content_num | int | 内容种子数据量 | 0 |


>处理器(dio.job)：种子写入数据库的工具类
| 字段名 | 类型 | 备注 | 默认 |
|
| id | int |    | 自增 |
| name | varchar | 写入数据库工具类 | -1 |
| desc | varchar | 工具类备注 |    |


>dio.processor：处理器表，种子处理器的工具类
| 字段名 | 类型 | 备注 | 默认 |
|
| id | int |    | 自增 |
| class_path | varchar | 种子处理器的工具类路径 |    |
| desc | varchar | 工具类备注 |    |


>dio.template.processor：模板处理器表，爬虫模板种子处理器的工具类
| 字段名 | 类型 | 备注 | 默认 |
|
| id | int |    | 自增 |
| class_path | varchar | 种子处理器的工具类路径 |    |
| desc | varchar | 工具类备注 |    |


>dio.table：爬虫的写入数据库配置表
| 字段名 | 类型 | 字段定义 | 默认 |
>dio.tag：爬虫站点的分类标签
| 字段名 | 类型 | 字段定义 | 默认 |
|
| id | int |    | 自增 |
| name | varchar(20) | 标签 |    |


# 3. 项目架构
项目架构配置
  * DioCore：采集系统base，集成Network，Units核心工具类
  * DioFramework：采集系统服务架构，爬虫架构
  * DioCrawler: 采集运作sdk
  * DioScheduler：采集系统任务调度
  * DioWebApp：采集系统后台应用
  * DioWebFront：采集系统界面前端
## 3.1 Core（基础核心包）
dio_core（采集系统核心）
* DB
  * Mongodb
    * createConnect：Mongodb创建链接工具
  * Mysql
    * createConnect：Mysql创建链接工具
  * Redis
    * createConnect：Redis创建链接工具
* Network
  * Downloader：下载器
* Units
  * JsonUnits：json处理工具
  * ModuleUnits：模块加载工具
  * DateUnits：时间处理工具
  * UrlUnits：url处理器
  * ThreadUnits：线程工具
## 3.2 Framework（服务依赖）
* Dao
  * TaskConfigDao：任务配置接口
  * SiteConfigDao：站点配置接口
  * TemplateDao：爬虫模板配置接口
* SpiderProcessor
  * Reader（Seed读取工具类）
    * RedisReader：Redis读取工具类
  * ReaderSeedsFilter（读取种子过滤器）
  * TpSpider（模板跑数类）
    * TpSpiderComponent（模板处理器）
      * Downloader（下载处理器）
      * LinkExtractor（链接抽取器）
      * ContentExtractor（内容抽取器）
      * ScriptExtractor（脚本抽取器）
  * WriterSeedsFilter（写入种子过滤器）
  * Writer（数据库种子写入工具类）
    * MongodbWriter：Mongodb数据库写入类
    * MysqldbWriter：Mysql数据库写入类
    * RedisWriter：Redis 数据库写入类
* Base
  * Processor（处理器）
    * SpiderProcessor（2级处理器/爬虫数据处理器）
    * JobProcessor （1级处理器/爬虫作业处理器）
    * TpSpiderComponent（4级处理器/爬虫模板组件）
    * TpSpider（3级处理器/爬虫组件加载处理器）
  * Runner（任务跑数类）
  * RunnerQuque（跑数队列）
  * FilterSet（过滤集合）
  * Seed（爬虫跑数种子）
  * Spider（爬虫类）
  * Middleware（中间件）
## 3.3 Scheduler（Job调度器）
* Scheduler
  * IncrScheduler（监控任务调度中心，Crawler主动消费）
  * AysncScheduler （异步任务调度中心）
## 3.4 Crawler（采集平台执行脚本）
* SchedulerStart
* RunnerStart
## 3.5 WebApp（Dio后端）
## 3.6 WebFront（Dio前端）
#
# 4. 系统设计
## 4.1 项目依赖
* Framework 依赖于Core。
* Scheduler 依赖于 Core，Framework。
* Crawler 依赖于 Core，Framework。
* WebApp 依赖于 Core，Framework。
* WebFront 依赖于 WebApp。
## 4.2 流程图
### 4.2.1 任务调度流程图。

### 4.2.2 job处理流程图。

### 4.2.3 Seeds处理流程图。
##
## 4.3 Base
### 4.3.1 Runner
**MetaClass：**
DioFramework.Base.Processor.Processor.Processor

**Attributes：**
* runner_id
* processorList

**Methods 方法**：
* finish：（结束释放资源函数）
* execute：（入口）

**默认爬虫配置处理器**
* JobReader（Job种子读取及初始化）
* JobMultiThreadProcessor（线程进行爬虫跑数）
* JobFinishProcessor（Job结束处理器，记录job，处理更新runner机器状态）
### 4.3.2 **Job**
**Attribute：**


**Methods：**


### 4.3.3 **Message**
爬虫数据流消息。

**Attribute：**
* info：爬虫抓取的数据Hash
* type：爬虫的类型
* depth：深度
* crawlerId：当前模板id。
* taskId：任务id
* siteId：站点id
* nextIds：后续模板id


### 4.3.4 Spider
标准爬虫类
**参数配置：**
* task_id：（任务id）
* site_id：（站点id）
* after_ids：（模板ids）
* depth：（默认）

**方法Methods:**
* crawl：（爬虫方法）
* incDepth：（增加深度）
* getAfterIds：（获取后续模板id列表）
* getInfo：（获取数据）



### 4.3.6 RunnerQuque
跑数队列。

方法Methods：
* pull：（获取）
* push：
* size
* isEmpty

RedisQueue
redis 连接的队列

参数：
* runner
* keyName

CacheQueue
参数：
* runner
* queue

### 4.3.5 Processor
处理器，处理某类对象列表

**参数配置：**
* **id:**

处理器id

* **config:**

配置参数

**方法Methods:**
* run（传递数据跑数）

* start:

### 4.3.9 JobProcessor设计
job处理组件。

方法配置：
* run：（跑数方法，返回种子列表）
  * seeds：种子列表
*


### 4.3.7 JobProcessor设计
爬虫处理器，用于处理爬虫种子。

参数配置：
* config：（配置参数）

方法配置：
* run：（跑数方法，返回种子列表）

### 4.3.8 TemplateComponent设计
爬虫组件，用于处理爬虫种子。

**MetaClass:**
* Processor

**Attributes**:
* tpId：模板id
* desc：模板desc
* type：模板类型

**Methods**：
* __init__：设置cfg，tpId，desc，type
  * kwrags：
    * config：组件配置
    * tpId：模板id
    * desc：模板desc
    * type：模板类型
* execute：（跑数方法，返回种子列表）
  * kwargs:
    * job：爬虫作业
    * messages：消息


### 4.3.10 TemplateLoader设计
模板封装类，封装数据库获取的模板信息，调用模板进行爬虫跑数

**MetaClass**:
* Processor

**Attributes**:
* componentsConfig：组件配置参数
* messageMatchStrategyConfig：匹配策略配置参数
* componentList：组件列表
* messageMatchStrategy：匹配策略
* tpId：模板id
* desc ：模板desc
* type：模板类型

**Methods**:
* __init__：初始化 componentList，matchStrategy
  * kwargs：
    * componentConfig：（dict）模板组件配置参数
    * messageMatchStrategyConfig：（dict）匹配策略配置参数
    * tpId：模板id
    * desc：模板desc
    * type：模板类型
* execute：迭代compentList，执行函数处理messages
  * kwargs：
    * message：爬虫消息
    * job：作业
  * return：list<Message>
* match：调用strategy，判定message是否匹配模板
  * return：True or False
* getTemplateId ：获取模板id
### 4.3.11 MessageMatchStrategy
模板匹配策略，用于根据message字段选择匹配模板

**MetaClass:**
* abc.ABCMeta

**Attributes：**
* config ：list 参数，列表元素为某个字段或多个字段组合的匹配规则。

**Methods：**
* __init__：初始化策略
  * kwargs：
    * strategyParams：（dict）json化策略参数
* match：根据参数匹配message
  * kwargs：
    * message：
  * return：True or False

>**匹配函数：**

**partialRegex**
部分正则匹配函数
* kwargs：
  * rule：匹配的正则
  * value：message 用于匹配的值
* return：True/False

**perfectRegex**
全匹配函数
* kwargs：
  * rule：匹配的正则
  * value：message用于匹配的值
* return：True/False

**equal**
全等匹配函数
* kwargs：
  * rule：匹配规则
  * value：message用于匹配的值
* return：True/False

**contain**
在范围内
* kwargs：
  * rule：值列表
  * value：message 用于匹配的值
* return：True/False

**OrTpMatchStrategy：**
或匹配策略，一个字段匹配成功返回True

**AndTpMatchStrategy：**
且匹配策略，所有字段的匹配规则必须匹配成功返回True

**MixTpMatchStrategy：**
条件匹配策略。。。

```
// 且匹配策略，或匹配规则
{
  "class_name": ""
  "params": [
    // enter_url 的匹配规则
    {
      "enter_url": {
        "regex": ".*"
      }
    },
    {
      "spider_ids": {
        "equals": "12321"
      }
    }
  ]
}
// 条件匹配策略
```

### 4.3.12 Distributor
Distributor
```
[
  {
    "message_match_strategy": {

    },
    "writer": {
      "class_"
    }
  },
  {

  }
]
```


**MetaClass:**
object

**Methods:**
* distribute：（分发 Message 至目标）
  * kwargs：
    * Messages

分发器
* JobQueueDistributor：(作业队列分发器)
* MongodbDistributor：(mongodb 分发器)



4.3.13 Writer




# 5. 处理器设计
## 5.1 JobProcessor设计
### 5.1.1 JobSeedReader：
循环读取爬虫作业种子reader，用于从redis中读取任务种子。
| id | 1 |
|
| class_path | DioFrame.Processor.JobProcessor.JobSeedReader |


Runner配置
```
// 增量任务配置,设置job种子读取队列
[{"id": "1", "key_name": "dio.scheduler.incr.seeds.queue"}]

// 异步任务配置,设置job种子读取队列
[{"id": "1", "key_name": "dio.scheduler.aynsc.seeds.queue"}]
```

Methods:



### 5.1.2 JobInitProcessor：
爬虫作业初始化处理器，初始化各种任务作业配置
* 读取数据库message_processor_config配置。
* 读取数据库job_config配置。
* 初始化爬虫种子队列/redis队列。
* 初始化Message种子，插入任务队列。
* 设置Runner状态。
| id | 2 |
|
| class_path | DioFrame.Processor.JobProcessor.JobInitProcessor |

Runner配置
```
// 增量任务配置
// 线程状态设置
[{"id": "2", "queue_type": "cache", "wait_time": "15"}]

// 异步任务配置
[{"id": "2", "queue_type": "redis", "key_name_format": "dio.crwaler.job.{job_id}", "wait_time": "15"}]
```

| 参数 | 参数说明 |
|
| thread | 线程类型，"cache"为内存队列，"redis"为rediskey |
| key_name_format | redis的key 格式化字符串 |
| wait_time | 读取job种子的等待时间 |


### 5.1.3 ThreadCrawler
| id | 3 |
|
| class_path | DioFrame.Processor.JobProcessor.ThreadCrawler |

Runner配置
```
# 线程状态设置，设置默认线程为4
[{"id": "3"， "thread_num": 4}]
```

task_config表 job_config配置
```
# job设置，设置线程数为5
{"3":{"thread_num": 5}}
```

| 参数 | 参数说明 |
|
| thread_num | 线程数 |

爬虫多线程跑数处理器，生成多线程处理器进行跑数。


### 5.1.4 JobFinishProcessor：
更新数据库数据，记录跑数任务情况。
| id | 4 |
|
| class_path | DioFrame.Processor.JobProcessor.JobFinishProcessor |

* 保存信息至数据库
  * state: job状态
  * insertTime: job插入时间
  * startTime: job开始时间
  * endTime: job结束时间
  * record: 记录Hash
* 设置runner作业状态为空
* 设置runner状态
* 释放Key资源
  * 设置 runnner 状态
  * 设置  job 状态
## 5.2 MessageProcessor设计
### 5.2.1 MessageReader
从job.queue，设置线程状态，读取 Msg返回。

**Attributes:**
* waitingTime:  等待时间

**Methods:**
* __init__：设置属性waiting_time
* run：执行处理器
  * kwargs：
    * job：爬虫作业
| id | 5 |
|
| class_path | DioFrame.Processor.MessageProcessor.MessageReader.MessageReader |

msg_processor_config配置：
```
// 内存队列配置
{
  "id": 6,
  "params": {
    "waiting_time": 10
  }
}
```

### 5.2.2 TemplateSpider
**Attribute**:
templateLoaderList:  {[TemplateLoader]} templateLoader对象列表

**Methods:**
* __init__：调用 job.taskConfig.getTpLoaderList 设置属性templateLoaderList
* execute：迭代templateLoaderList，匹配模板跑数
  * kwargs：
    * job：爬虫作业
    * Messages：msg列表

msg_processor_config配置：
```
// 选择匹配模板的规则。
{
  "id": 6
}
```

### 5.2.3 SeedFilter
选择content类型的seed，选择过滤队列，进行过滤。

**Attribute**:
filterSet:  {DioCore.DB.RedisClient.Set} 过滤集合

**Methods:**
* __init__：设置filterSet属性
* run：迭代templateLoaderList，匹配模板跑数
  * kwargs：
    * job：爬虫作业
    * Messages：msg列表

**msg_processor_config：**
```
// level: "GLOBAL"/"TASK"/"SITE"
{
  "id": 7,
  "level": "TASK"
}
```


### 5.2.4 MessageDistributor
种子分发处理器，负责分发至数据库
* JobQueueDistributor
* MongodbDistributor

**MetaClass:**
MessageProcessor

**Methods:**
* __init__：设置distributors 设置job Distributor
  * kwargs:
    * cfg：处理器配置
    * job：作业
* execute：迭代 job.distributors，判断是否匹配message， 匹配成功分发message
  * kwargs：
    * job：作业
    * messages：消息列表

msg_processor_config配置：
```
// 根据类型进行分发，0为种子类型，1为内容类型
{
  "id": "5",
  "params": {
    // mongodb 分发
    "MongodbDistributor-1": {
      // 类名
      "class_path": "MongodbDistributor",
      // 参数
      "params": {
        "table": "xxx",
        "db": "db",
        // 匹配分发规则
        "distribute_rules": {
          "type": "content",
          "toIds": ""
        }
      }
    },
    // job 队列分发
    "JobQueueDistributor-1": {
      // 类名
      "class_path": "JobQueueDistributor",
      // 参数
      "params": {
        // 匹配分发规则
        "distribute_rules": {
          "type": "link",
          "toIds": ""
        }
      }
  }
}
```

## 5.3 TpSpider设计
### 5.3.1 TpSpider
模板爬虫加载类，用于加载爬虫组件。

template参数配置：
```
[{
  "id": "12", // Component id
  "tp_id": 1
}]
```

## 5.4 TemplateComponent设计
### 5.4.1 ScriptSpider
脚本爬虫类
| id | 13 |
|
| class_path | DioFrame.Processor.TpSpiderComponent.ScriptSpider |

msg_processor_config参数配置：
```
{
  "id": "13", // Component id
  "params":   {"class_path":"DioFrame.Processor.TpSpiderComponent.ScriptSpider"}
  // Component参数
}
```

### 5.4.2 FinshCrawlProcessor
结束爬虫，对message做收尾处理
1. 设置nextIds。
2.
msg_processor_config参数配置：
```
{
  "id": "14"，
  "params": {
    ""
  }
}
```

# 5. 系统配置
## 5.1 任务配置
spider_config 配置：
```
[{"id" : 1,
"readerType": 2 }]
// 使用SeedsReader处理器
```

**任务数据库配置：**
```
[1, 2, 3]
```

## 5.2 模板配置
message_processor_config 配置
```
[
  {
    "id": 5,

  }
]
```

# 6. 处理器
## 6.1 SeedsReader
从runner的seeds队列中或redis队列中读取Seeds
###
### 6.1.1 CacheSeedsReader
从Runner的生成队列读取种子：
数据库spider_config字段配置：
```
// 配置
[{"id": 1}]

// 配置方法2
[1]
```

### 6.1.2 RedisSeedsReader
从Redis读取种子：
数据库spider_config字段配置：
```
// 配置
[{"id": 2},...]
[2,...]

// 指定 队列名
[{"id": 2, "key_name": "dio.crawler.task.seeds.job"}]

```

6.2 JobRecorder
记录处理种子情况：



感悟：
流程化处理对象
Runner  处理对象 -> task
ThreadRunner 处理对象 -> Seeds





# 7. Job类相关
Job Runner 线程状态
* RUNNING
* OVER

## **7.1 ThreadStateHash**
线程状态hash


## 7.2 ThreadStateManager
线程状态manager

**MetaClass**:
* abc.ABCMeta

**Attributes:**
* logger： logger

**GlobalAttributes**:
* format：{str} "{runnerId}_{jobId}" 键名

**Methods**:
* __init__: 初始化，打logger
  * kwargs
    * curRunnerId：当前runner 状态
    * jobId：作业 id
    * format: 字典key 渲染
* getState：获取当前线程job状态
  * return: RUNNING/OVER
* setRunning：设置threadState 当前线程状态为RUNNING
* setOver：设置threadState  当前线程为OVER。
* isAllThreadsOver：迭代StateHash判断所有线程是否结束。
  * return: True/False
* getKeyName：根据format 设置键名
  * return：{str}


### 7.2.1 CacheThreadStateManager
内存 基于dict 的线程状态Manager

**Attributes**:
* threadState：{dict} 记录线程状态
* curRunnerId：{str} 当前runner的runnerId
* jobId：{str} jobId
* format：{str} "{runnerId}_{jobId}" 键名

**Methods**:
* __init__: 初始化
  * kwargs
    * threadState：设置为空字典
    * curRunnerId：当前runner 状态
    * jobId：作业 id
* getState：获取当前线程job状态。
* setRunning：设置threadState 当前线程状态为RUNNING。
* setOver：设置threadState 线程状态为OVER。
* isAllThreadsOver：判断所有线程是否结束。

### 7.2.2 RedisThreadStateManager
基于 redis 的 线程状态 manager

**MetaClass:**
ThreadStateManager

**Attributes:**
* threadState：{DioCore.DB.RedisClient.Hash} redis 状态Hash

**Methods：**
* __init__: 初始化redis Hash
* getState：hget，获取当前线程状态。
* setRunning：hset，设置当前线程状态为RUNNING。
* setOver：hset，设置当前线程状态为OVER。
* isAllThreadsOver：hgetall，判断所有线程是否结束。


## 7.3 Writer
```
{
  "class_name": "DioFramework.DB.Writer.MongodbWriter",
  "params": {
    "cache_size": 20
  }
}
```
7.3.1 BaseWriter
接口类

Methods:
* __init__:  根据job和其他参数初始化
  * job：job实体
  * params：其他参数
* write：分发种子
  * kwargs:
    * Messages
# Problem
获取job