USE dio;


# 站点配置表
CREATE TABLE `dio.site.config`
(
  `id`        INT PRIMARY KEY AUTO_INCREMENT
  COMMENT '唯一标志',
  `desc`      VARCHAR(100) COMMENT '站点备注',
  `domain`    VARCHAR(200) COMMENT '站点域名',
  `parend_id` INT COMMENT '父级站点id',
  `tag`       INT COMMENT '站点标签',
  `status`    INT             DEFAULT 0
  COMMENT '站点状态'
);



# 任务配置表
CREATE TABLE `dio.task.config`
(
  `id`        INT PRIMARY KEY AUTO_INCREMENT
  COMMENT '唯一标志',
  `desc`      VARCHAR(100) COMMENT '任务备注',
  `domain`    VARCHAR(200) COMMENT '任务域名',
  `parend_id` INT COMMENT '父级站点id',
  `tag`       INT COMMENT '站点标签',
  `status`    INT             DEFAULT 0
  COMMENT '站点状态'
);