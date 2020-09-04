/*
 Navicat Premium Data Transfer

 Source Server         : 10.96.11.13-5.7
 Source Server Type    : MySQL
 Source Server Version : 50728
 Source Host           : 10.96.11.13:3307
 Source Schema         : auto_test

 Target Server Type    : MySQL
 Target Server Version : 50728
 File Encoding         : 65001

 Date: 03/07/2020 17:25:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for api_test
-- ----------------------------
DROP TABLE IF EXISTS `api_test`;
CREATE TABLE `api_test`  (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `project_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '项目名称',
  `api_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '接口名称',
  `api_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '接口地址',
  `api_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '接口描述',
  `test_script_path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '测试脚本路径',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for script_exec_record
-- ----------------------------
DROP TABLE IF EXISTS `script_exec_record`;
CREATE TABLE `script_exec_record`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `api_test_id` bigint(20) NULL DEFAULT NULL,
  `script_text` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `exec_result` int(1) NULL DEFAULT NULL,
  `exec_result_msg` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `excec_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `access_token` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nick_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `password_hash` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `email_hash` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `create_time` datetime(0) NOT NULL,
  `state` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, NULL, 'tiezhu.liu@wetax.com.cn', '刘铁柱', 'pbkdf2:sha256:150000$U6OwyRmd$c047dafbd66bf22fd1ace373461553a55038aefbe97ae3b4b2f1f2c5d5f49f06', 'fac59e48de39a5f0ff3eebe6f3e98f30', '2020-06-29 11:03:46', 0);
INSERT INTO `user` VALUES (2, NULL, 'wzw@wetax.com.cn', '王中王', 'pbkdf2:sha256:150000$chMqBaQi$2bc4a8f835a132eb0cea9aa3707febde048187b13aa9dd05539906aa72098ad7', '9a500342ca9b09882633d9eb98972772', '2020-06-29 11:12:59', 0);

SET FOREIGN_KEY_CHECKS = 1;
