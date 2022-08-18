CREATE TABLE IF NOT EXISTS `m_sms`
(
    `sms_id`    bigint(20)   NOT NULL AUTO_INCREMENT,
    `type`      tinyint(1)   NOT NULL comment '类型',
    `number`    VARCHAR(20)  NOT NULL COMMENT '收件人姓名',
    `text`      VARCHAR(255) NOT NULL COMMENT '收件人姓名',
    `timestamp` bigint(20)   NOT NULL comment '卖家id',
    `smsc`      VARCHAR(20)  NOT NULL COMMENT '收件人姓名',
    PRIMARY KEY (`sms_id`),
    KEY `status` (`number`),
    KEY `timestamp` (`timestamp`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE utf8mb4_unicode_ci COMMENT ='短信';
